# NOTAS DEL LIBRO MASTERING PYTHON

**Usamos python3**

## Chapter 1 - Getting Started – One Environment per Project


#### Creating a virtual Python environment using venv


#### Bootstrapping pip using ensurepip


#### Installing C/C++ packages

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


## Chapter 2. Pythonic Syntax, Common Pitfalls, and Style Guide

El desarrollo de Python siempre ha estado en manos de su creador Guido van Rossum, quien es llamado
Benevolent Dictator For Life (BDFL).

Para ayudar al DBFL en el mantenimiento y desarrollo de Python se creo el proceso: **Python Enhancement Proposal (PEP)**
(Propuesta de mejora de Python). Este proceso permite a cualquier persona enviar un PEP con una
especificación técnica de la característica y una justificación para defender su utilidad.
Después de una discusión sobre las listas de correo de Python y posiblemente algunas mejoras,
la BDFL tomará la decisión de aceptar o rechazar la propuesta.

#### Code style – or what is Pythonic code?

La filosofía del PEP 20 dice que el código debe ser:
- Limpio
- Simple
- Lindo
- Explicito
- Legible

#### Formatting strings – printf-style or str.format?

Python ha sido compatible con los estilos:

	printf-style (%)

y

	str.format

En general la mayoria de las personas recomiendan *str.format*, pero esto esta sujeto a las preferencias
de cada persona. *printf-style* es mas simple, pero *str.format* es mas poderoso.

**Para aprender más acerca de PyFormat visitar https://pyformat.info/**

#### PEP20, the Zen of Python

#### Maximum line length

Para mantener la regla de los 79 caracteres hay que pensar en refactorizar el código de forma que se vea mejor
y de una forma más 'pythonic'. Ejemplos:

- Usando el backslash:

	with open('/path/to/some/file/you/want/to/read') as file_1, \
        	open('/path/to/some/file/being/written', 'w') as file_2:
    	file_2.write(file_1.read())

- En lugar de backslash:

	filename_1 = '/path/to/some/file/you/want/to/read'
	filename_2 = '/path/to/some/file/being/written'
	with open(filename_1) as file_1, open(filename_2, 'w') as file_2:
    	file_2.write(file_1.read())

- O puede ser:

	filename_1 = '/path/to/some/file/you/want/to/read'
	filename_2 = '/path/to/some/file/being/written'
	with open(filename_1) as file_1:
	    with open(filename_2, 'w') as file_2:
	        file_2.write(file_1.read())

No siempres es una opción, pero es bueno tenerlo en cuenta y mantener el código corto y legible.

#### Verifying code quality, pep8, pyflakes, and more

Algunas herramientas que verificán el código son:
	
1. flake8
2. PEP8
3. pyflakes
4. McCabe
5. Pylint

### Common pitfalls

#### Scope matters!
Con la función:
	
	def spam(key, value, list_=[], dict_={}):
	    list_.append(value)
	    dict_[key] = value

	    print('List: %r' % list_)
	    print('Dict: %r' % dict_)

	spam('key 1', 'value 1')
	spam('key 2', 'value 2')

se espera obtener:
	
	List: ['value 1']
	Dict: {'key 1': 'value 1'}
	List: ['value 2']
	Dict: {'key 2': 'value 2'}

Pero se obtiene:
	
	List: ['value 1']
	Dict: {'key 1': 'value 1'}
	List: ['value 1', 'value 2']
	Dict: {'key 1': 'value 1', 'key 2': 'value 2'}

La razón es que list_ y dict_ en realidad se comparten entre varias llamadas. Por lo tanto
se debe evitar usar objetos mutables como parámetros predeterminados en una función.

La forma segura es la siguiente:
    
    def spam(key, value, list_=None, dict_=None):
        if list_ is None:
            list_ = []

        if dict_ is None:
            dict_ = {}

        list_.append(value)
        dict_[key] = value
