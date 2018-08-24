# NOTAS DEL LIBRO MASTERING PYTHON #

** Usamos python3 **

## Chapter 1 - Getting Started – One Environment per Project ##


## Creating a virtual Python environment using venv ##

## Bootstrapping pip using ensurepip ##

## Installing C/C++ packages ##

Cuando se hacen instalaciones de paquetes de Python que dependen de otras
dependencias y se generan errores como el siguiente:

    x86_64-linux-gnu-gcc: error: build/temp.linux-x86_64-3.4/libImaging/Jpeg2KDecode.o: No such file or directory
    x86_64-linux-gnu-gcc: error: build/temp.linux-x86_64-3.4/libImaging/Jpeg2KEncode.o: No such file or directory
    x86_64-linux-gnu-gcc: error: build/temp.linux-x86_64-3.4/libImaging/BoxBlur.o: No such file or directory
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

    ----------------------------------------
	Command "python3 -c "import setuptools, tokenize;__file__='/tmp/pip-build-_f0ryusw/pillow/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-kmmobum2-record/install-record.txt --single-version-externally-managed --compile --install-headers include/site/python3.4/pillow" failed with error code 1 in /tmp/pip-build-_f0ryusw/pillow

El truco para encontrar el error esta en buscar los mensajes acerca de los 'headers' no encontrados:

	n file included from libImaging/Imaging.h:14:0,
                   from libImaging/Resample.c:16:
  	libImaging/ImPlatform.h:10:20: fatal error: Python.h: No such file or directory
   	#include "Python.h"
                      ^
  	compilation terminated.

En este caso el header **Python.h** no fue encontrado. Este es necesario para la compilación
de paquetes C/C++ dentro de Python. Para solucionar este caso en Ubuntu:

	$ sudo apt-get install python3-dev

48af139