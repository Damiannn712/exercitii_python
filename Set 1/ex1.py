def gcd_multiple(*numbers):
    # Verifica daca exista cel putin un numar
    if not numbers:
        return None

    # Initializeaza gcd-ul cu primul numar
    result = numbers[0]

    # Calculeaza gcd-ul pentru toate numerele
    for number in numbers[1:]:
        while number != 0:
            result, number = number, result % number

    return result


# Exemplu de utilizare
print(gcd_multiple(24, 36, 60))
