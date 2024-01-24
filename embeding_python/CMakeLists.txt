cmake_minimum_required(VERSION 3.10)
project(test_python_integration VERSION 0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED true)

# The below commands seem to not be necessart, but note, the venv needs to be
# activated in the terminal where the c++ executable is called
# set(Python3_ROOT_DIR /home/colin/Research/ir/GlueStick/venv/)
# set(Python3_FIND_VIRTUALENV FIRST)

find_package(Python3 REQUIRED Development Interpreter)
message(STATUS "Found python : ${Python3_FOUND}")
message(STATUS "Python libraries : ${Python3_LIBRARIES}")
message(STATUS "Python executable : ${Python3_EXECUTABLE}")
message(STATUS "Python_INCLUDE_DIR : ${_Python3_INCLUDE_DIR}")

add_executable(basic_integration src/test_python.cpp)
target_link_libraries(basic_integration Python3::Python)
