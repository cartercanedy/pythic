cmake_minimum_required(VERSION 3.10)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)
set(CMAKE_C_FLAGS "-fno-semantic-interposition -Wall -Wextra -O3")
set(CMAKE_EXPORT_COMPILE_COMMANDS True)

project(pythic)
add_subdirectory(src/pythic/_core)