# Calling Python from C++
There are lots of ways to use python in c++. This is a very basic example of the standard embedding python system with cmake.

## Virtual Enviroments and Conda
I was able to make this example work with a venv virtual environment just by activating the env in the terminal where the executable was run. Activating the environment sets the `PATH` environemnt variable so that python can import libraries. Note that venv often uses the system python installation so I did not need to actually change the python libraries found by cmake. Conda, by contrast, typically does install a standalone python installation. To use a conda python installation, I think you need to set the `Python3_ROOT_DIR` cmake variable. This is included on in the cmake example.