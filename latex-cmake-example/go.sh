#!/bin/sh
mkdir out
cd out
cmake .. -DPDFLATEX_COMPILER=$(which xelatex)
make VERBOSE=1
cd -
