project(PackageTest CXX)

cmake_minimum_required(VERSION 3.2.0)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_compile_options(
    "$<$<CXX_COMPILER_ID:MSVC>:/wd4251>"
)

add_executable(example example.cpp)
conan_target_link_libraries(example)
