#!/usr/bin/env python
"""
Calcuate checksum for .text section of a given elf file.
"""

from __future__ import print_function
import argparse
import hashlib
import os
import re
import subprocess
# import pdb


def calculate_checksum(elf_file, section_name=".text"):
    """
    Calculate and print the checksum.
    """
    if not os.path.isfile(elf_file):
        return ""

    section_content = get_section_content(elf_file, section_name)

    if section_content:
        checksum = hashlib.md5(section_content)
        return checksum.hexdigest()
    else:
        return ""


def get_section_info(elf_file, section_name=".text"):
    """
    Return (offset, length) of the elf section.
    """
    if not is_elf(elf_file):
        return 0, 0
    hex_rgx = "[0-9a-fA-F]+"
    rgx = re.compile(r"\s+\[\s*\d+\] " + section_name +
                     "\s+[_a-zA-Z0-9]+\s+" + hex_rgx +
                     "\s+(?P<offset>" + hex_rgx + ")" +
                     "\s+(?P<length>" + hex_rgx + ").*")

    out = subprocess.check_output([
        "readelf", "--sections", "--wide", elf_file])
    for line in out.splitlines():
        match = rgx.match(line)
        if match:
            offset = match.expand(r"\g<offset>")
            length = match.expand(r"\g<length>")
            return int(offset, 16), int(length, 16)
    return 0, 0


def get_section_content(elf_file, section_name=".text"):
    """
    Return the content of the elf section. If any error takes place, return
    an empty string.
    """
    offset, length = get_section_info(elf_file, section_name)
    if length <= 0 or offset < 0:
        return ""

    elf_file_normpath = os.path.normpath(elf_file)
    if offset + length > os.path.getsize(elf_file_normpath):
        return ""

    with file(elf_file, "rb") as _fp:
        _fp.read(offset)
        content = _fp.read(length)
    return content


def is_elf(elf_file):
    """
    Return True if the given file is elf format and False otherwise.
    """
    full_path = os.path.realpath(elf_file)
    if not os.path.isfile(full_path):
        return False
    out = subprocess.check_output(["file", full_path])
    if "elf" in out.lower():
        return True
    else:
        return False


def show_checksum(elf_file):
    """
    Print the checksum.
    """
    if not os.path.isfile(elf_file):
        print("{} : No such file.".format(elf_file))
        return ""
    elif not is_elf(elf_file):
        print("{}: Not an elf-format file".format(elf_file))
    else:
        checksum = calculate_checksum(elf_file)
        print("{} {}".format(checksum, elf_file))


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description="Calculate checksum for elf files."
    )
    parser.add_argument("--elf",
                        nargs="*",
                        default=[],
                        help="Elf files")
    args = parser.parse_args()
    for elf_file in args.elf:
        show_checksum(elf_file)


if __name__ == "__main__":
    main()
