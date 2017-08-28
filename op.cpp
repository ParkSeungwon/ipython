#include <Python.h>
#include<fstream>
#include<iostream>
using namespace std;

const char* run_this = R"(
from time import time,ctime
print('Today is', ctime(time()))
from pylab import *
x=linspace(-2,2,100)
y=x*x
plot(x,y)
show()
)";

int main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }
    Py_SetProgramName(program);  /* optional but recommended */
    Py_Initialize();
    PyRun_SimpleString(run_this);
    Py_Finalize();
    PyMem_RawFree(program);
	system("python with.py");
    return 0;
}

