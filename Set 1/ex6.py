def camel_to_snake(text):
    # Initializeaza rezultatul cu primul caracter
    result = text[0].lower()

    # Parcurge restul caracterelor
    for char in text[1:]:
        # Daca caracterul este mare, adauga un underscore si il transformă in litera mica
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


# Exemplu de utilizare
print(camel_to_snake("UpperCamelCase"))
