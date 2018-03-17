cmake_minimum_required(VERSION 2.8)
PROJECT(demo)
INCLUDE(UseLATEX.cmake)
ADD_LATEX_DOCUMENT(main.tex
    BIBFILES ref.bib
    INPUTS CMakeLists.txt go.sh
    DEFAULT_PDF)
