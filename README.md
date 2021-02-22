# modules test

### Aclaraciones

El progrma funciona sobre Python 3.
Los únicos módulos que se importan son _os_ y _json_ que están incluídos en la librería estándard de python, por lo que no es necesario el uso explícito de un archivo de requirements ni entornos virtuales.
No doy garantía de que el programa funcione correctamente en un sistema que no sea Linux.

## Correr el programa

La entrada del programa son los archivos _.json_ que se encuentren en la carpeta _data_.

Para correr el programa y generar las salidas esperadas en función de tales archivos, en el directorio raíz de este repositorio ejecutar:
```
python modules_test.py
```
La salida del programa se hará en forma de dos archivos:
* _users_by_module.json_: Son los usuarios agrupados por los módulos que usan.
* _minimum_users_for_testing_modules.txt_: Es el mínimo conjunto de usuarios con los que, de probar sus módulos, se estarían probando todos.