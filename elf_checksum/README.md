## Introduction ##

The scripts in this repository calculate the checksum of the sections of
elf-format files. The purpose is to check the consistency of executables and
shared libraries.

In normal circumstances, you can use
```
ld --build-id=md5
```
or
```
gcc -Wl,--build-id=md5
```
to embed checksum into the elf files.
Only in particular situations the scripts here fit your need.

## Motivation ##

It is important to make sure we have the same program as our software
testers do. If not, we may waste time, discussing what a real bug is. Using
the checksum of the program is one possible way to achieve this.

However, I ran into a situation where generated elf files have different
checksum, with the same code and with the same build commands. The reason is
that the build system insert source code paths into elf files. As a result,
the elf files are slightly different (though they work the same way).

People use the md5 checksum of the whole file to decide two versions of elf
files are identical. Unfortunately their method cannot apply in such a case.
Therefore I write this script to generate only the checksum of the .text
section of an elf file, where .text section is the machine instructions
store. In such a way I can show that two elf files are consistent.
