# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1", "3", "2"],
        # Outputs
        ["Ingresa el coeficiente a: ", "Ingresa el coeficiente b: ", "Ingresa el coeficiente c: ", "Raiz positiva es : -1.0" , "Raiz negativa es : -2.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda que se deben añadir (  ) / (  )"
    ),
    (
        # Inputs
        ["3", "0", "-12"],
        # Outputs
        ["Ingresa el coeficiente a: ", "Ingresa el coeficiente b: ", "Ingresa el coeficiente c: ", "Raiz positiva es : 2.0" , "Raiz negativa es : -2.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda que se deben añadir (  ) / (  )"
    ),
    (
        # Inputs
        ["3", "0", "-3"],
        # Outputs
        ["Ingresa el coeficiente a: ", "Ingresa el coeficiente b: ", "Ingresa el coeficiente c: ", "Raiz positiva es : 1.0" , "Raiz negativa es : -1.0"],
        # Error message
        "Revisa los tipos de dato de tus variables. Revisa la prioridad de operadores. Recuerda que se deben añadir (  ) / (  )"
    ),
]
