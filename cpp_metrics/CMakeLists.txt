cmake_minimum_required(VERSION 3.12)
project(indicators)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find pybind11 package (requires pybind11 installed)
add_subdirectory(pybind11)

# Create Python extension module named "indicators"
pybind11_add_module(indicators
    sma.cpp

)