cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)


project(pythic)
set(SOURCES pythic/pythic.c)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY src/pythic)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY src/pythic)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY src/pythic)
set(CMAKE_C_FLAGS "-fno-semantic-interposition -Wall -Wextra -O3")

add_library(pythic SHARED ${SOURCES})
set_target_properties(pythic PROPERTIES PREFIX "")
target_include_directories(pythic PUBLIC include)
target_include_directories(pythic PUBLIC "${PYTHON_DIR}")
target_include_directories(pythic PUBLIC "${PROJECT_BINARY_DIR}")

configure_file(include/pythicConfig.h.in include/pythicConfig.h)

