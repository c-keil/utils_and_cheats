# OpenCV Notes
There is a lot to say here, but here are a few comments

## Non-Local Install
I have found that I often need more than one version of opecv for different c++ projects. For example, I found that I needed opencv 3.x, not 4.x to open a very large vocabulary for DBoW2. To install a second version in a specific location, I could did the following:
1. Download the OpenCV version
2. Build it with
    - cd opencv-3x; mkdir build; cd build
    - `cmake -DCMAKE_INSTALL_PREFIX=install ..` this puts the `install` dir in (relative to) the build `folder`. You can do an absolute path
    - `cmake --build . --target install` builds and installs in the target install path
3. You can point DBoW2 to the correct version by changing `find_package(OpenCV REQUIRED)` to 
`find_package(OpenCV 3.4 REQUIRED PATHS /home/colin/Software/opencv-3.4.16/build/install)` in CMAKE
