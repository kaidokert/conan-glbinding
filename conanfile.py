#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class GlBindingConan(ConanFile):
    name = "glbinding"
    version = "3.0.2"
    description = "Cross platform C++ binding for the OpenGL API."
    url = ""
    homepage = "https://github.com/cginternals/glbinding"
    author = "fishbupt <fishbupt@gmail.com>"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    extracted_dir = "glbinding-" + version
    no_copy_source = True
    generators = "cmake"
    requires = ("glfw/[^3.2.1]@fishbupt/latest")

    def source(self):
        source_url = "https://github.com/cginternals/glbinding"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))

        tools.replace_in_file("{}/CMakeLists.txt".format(self.extracted_dir), "project(${META_PROJECT_NAME} C CXX)",
                              '''project(${META_PROJECT_NAME} C CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.extracted_dir)
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["glbinding"]
