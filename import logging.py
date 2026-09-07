import logging

logging.basicConfig(level=logging.ERROR)

while True:
    try:
        edad = input("Ingresa tu edad: ")

        # Validación de datos
        if not edad.isdigit():
            raise ValueError("La edad debe ser un número.")

        edad = int(edad)

        # Assert
        assert edad <= 120, "La edad no puede ser mayor a 120."

        # Raise
        if edad < 1:
            raise ValueError("La edad debe ser mayor a 0.")

        print("Edad registrada correctamente:", edad)
        break

    except ValueError as error:
        print("Error:", error)
        logging.error("Error en el registro de edad: %s", error)

    except AssertionError as error:
        print("Error:", error)
        logging.error("Error de validación: %s", error)

print("Proceso terminado.")