#!/bin/bash
if [[ ! -f $1 ]]; then
    echo "usage: $0 DSO"
    exit 1
fi
readonly local elf=$1

readonly local sec_info=$(readelf -S --wide ${elf} | grep .text)
offset=$(echo $sec_info | awk '{print $5}')
offset=$((16#${offset}))
length=$(echo $sec_info | awk '{print $6}')
length=$((16#${length}))

readonly local temp_file=temp.${RANDOM}
dd if=${elf} bs=1 skip=${offset} count=${length} of=${temp_file} \
    > /dev/null 2>&1
checksum=$(md5sum ${temp_file} | awk '{print $1}')
rm ${temp_file}

echo $checksum $elf
