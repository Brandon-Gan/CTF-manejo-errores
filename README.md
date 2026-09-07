# 🛠️ Manejo de errores en Python

## Descripción

Este proyecto contiene un ejemplo de **manejo de errores en Python**. El programa solicita al usuario su edad y comprueba que el dato introducido sea válido.

Si se introduce un valor incorrecto, se muestra un mensaje de error y el programa permite intentarlo nuevamente en lugar de cerrarse.

## 🔧 Herramientas utilizadas

El programa utiliza diferentes herramientas para manejar los posibles errores:

* **Try - Except:** detecta y controla los errores.
* **Validación de datos:** comprueba que la edad introducida sea un número.
* **Raise:** genera un error cuando se encuentra un dato no válido.
* **Assert:** comprueba que la edad no sea mayor a 120 años.
* **Logging:** registra los errores que ocurren durante la ejecución.
* **While:** permite que el programa continúe funcionando hasta recibir un dato correcto.

## 💻 Funcionamiento

Al ejecutar el programa, se solicita la edad:

```text
Ingresa tu edad: 150
Error: La edad no puede ser mayor a 120.

Ingresa tu edad: 21
Edad registrada correctamente: 21

Proceso terminado.
```

Cuando se introduce un dato incorrecto, el programa muestra el error y vuelve a solicitar la edad.

## ▶️ Ejecución

Para ejecutar el programa es necesario tener Python instalado. Desde la terminal, dentro de la carpeta del proyecto, se utiliza:

```bash
python manejo_errores.py
```

## 📁 Archivo

El proyecto contiene el siguiente archivo:

```text
manejo_errores.py
```
