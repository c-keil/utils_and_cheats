# CMake Tips

## General Workflow
The usual workflow for installing for source with CMake is something like:
```
git clone <project_name>.git # or whatever
cd project_name
mkdir build
cd build
cmake .. #with optional cmake options
make -j8
make install # to actually install, not necessarily required usually system wide by default
```

## Non Standard Install Path
To install in a custom location, you can use the `-DCMAKE_INSTALL_PREFIX=<install_dir>` option. For Pushyami's slam code, the general pattern is to use a local install folder like:
```
cmake .. -DCMAKE_INSTALL_PREFIX=../install
```

## Directly Supplying CMake with a dependancy path
You can directly supply a path to project binaries using a cmake command line option with the form `-D<library_name>_DIR`. For a project that uses opencv this might look like:
```
CMake .. -DOpenCV_DIR=/<path_to_opencv>/opencv/build
```

## Build Type
Some projects support different build options that can be activated with the pattern `-DCMAKE_BUILD_TYPE=Release`

## Figuring out what library CMake finds
I had a hard time with this for some reason. I found using `ldd` and `lddtree` to be very helpful for figuring out what was using what.