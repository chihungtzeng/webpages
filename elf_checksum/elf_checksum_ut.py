#!/usr/bin/python
"""
unit test for elf_checksum.py.
Usage:
    python elf_checksum_ut.py
"""

import os
import unittest
import elf_checksum


class ELFCheckSum(unittest.TestCase):
    """
    unittest class for elf_checksum.py
    """

    def test_calculate_checksum(self):
        """
        Check the toy program a.out has the expected checksum.
        """
        ut_script_path = os.path.normpath(os.path.join(__file__, ".."))
        elf_file = os.path.join(ut_script_path, "test_data", "a.out")
        self.assertEqual(
            "f7f94b1b0ba8c349ac3a3de5d1f1c78f",
            elf_checksum.calculate_checksum(elf_file))

    def test_calculate_checksum_non_elf(self):
        """
        calcuate_checksum returns "" for non-elf files
        """
        self.assertEqual("", elf_checksum.calculate_checksum("/etc/passwd"))

    def test_calculate_checksum_non_existent(self):
        """
        calcuate_checksum returns "" for non-existent files
        """
        self.assertEqual("", elf_checksum.calculate_checksum("/etc/kkkaaa"))

    @unittest.skipIf(not os.path.isfile("/bin/ls"), "/bin/ls is required.")
    def test_get_section_info_bin_ls(self):
        """
        A regular elf file should have positive offset and length
        """
        offset, length = elf_checksum.get_section_info("/bin/ls")
        self.assertGreater(offset, 0)
        self.assertGreater(length, 0)

    def test_get_section_info_non_existent(self):
        """
        For a non-existent file, get_section_info returns offset = 0 and
        length = 0.
        """
        offset, length = elf_checksum.get_section_info("/etc/non_exist")
        self.assertEqual(offset, 0)
        self.assertEqual(length, 0)

    def test_get_section_content_non_existent(self):
        """
        get_section_content returns an empty string for a non-existent file.
        """
        content = elf_checksum.get_section_content("/etc/non_exist")
        self.assertEqual(content, "")

    @unittest.skipIf(
        not os.path.isfile("/etc/passwd"),
        "/etc/passwd is required.")
    def test_get_section_info_non_elf(self):
        """
        For a non-elf file, get_section_info returns both offset and length
        = 0.
        """
        offset, length = elf_checksum.get_section_info("/etc/passwd")
        self.assertEqual(offset, 0)
        self.assertEqual(length, 0)

if __name__ == "__main__":
    unittest.main()
