#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <iostream>

int main()
{
    std::cout << "Hello world" << std::endl;
    Py_Initialize();
    PyRun_SimpleString("print('Hello World ... from python')\nimport cv2\nprint('OpenCV Version: {}'.format(cv2.__version__))\nimport sys\nprint(sys.executable)");
    Py_Finalize();
    
    return 0;
}

