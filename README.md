# 🛡️ Manejo de Errores en Python

## 📌 Descripción

Este proyecto es un ejemplo sencillo de **manejo de errores en Python**.
El programa solicita al usuario su edad y utiliza diferentes herramientas para detectar y controlar datos incorrectos.

La idea principal es evitar que el programa se cierre cuando el usuario introduce un dato inválido y permitirle intentarlo nuevamente.

---

## ⚙️ ¿Qué se utilizó?

En el programa se utilizaron varias herramientas para el manejo de errores:

* 🧩 **`try-except`** → Permite detectar y controlar errores.
* 🔎 **Validación de datos** → Comprueba que la edad introducida sea válida.
* 🚨 **`raise`** → Permite generar errores cuando se encuentra un dato incorrecto.
* ✅ **`assert`** → Comprueba que la edad no sea mayor a 120 años.
* 📝 **`logging`** → Registra los errores que ocurren durante la ejecución.
* 🔄 **`while`** → Hace que el programa continúe funcionando después de un error.

---

## 💻 ¿Cómo funciona?

El programa pide al usuario que introduzca su edad.

Por ejemplo:

```text
Ingresa tu edad: hola
Error: La edad debe ser un número.

Ingresa tu edad: 150
Error: La edad no puede ser mayor a 120.

Ingresa tu edad: 21
Edad registrada correctamente: 21

Proceso terminado.
```

Cuando se introduce un dato incorrecto, el programa **no se cierra**. En lugar de eso, muestra el error y vuelve a solicitar la edad.

---

## 🎯 Objetivo

El objetivo de este ejercicio es demostrar cómo se pueden utilizar diferentes herramientas de manejo de errores para crear un programa más **seguro, controlado y fácil de utilizar**.

---

## 📂 Archivo

```text
manejo_errores.py
```

El archivo contiene todo el código necesario para ejecutar el ejemplo.

---

## ▶️ Ejecución

Para ejecutar el programa se necesita tener **Python** instalado.

Desde una terminal, dentro de la carpeta del proyecto:

```bash
python manejo_errores.py
```

---
