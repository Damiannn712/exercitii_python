def count_vowels(text):
    # Defineste vocalele
    vowels = "aeiouAEIOU"

    # Initializeaza contorul
    count = 0

    # Parcurge fiecare caracter din sir
    for char in text:
        # Verifica daca caracterul este o vocala
        if char in vowels:
            count += 1

    return count


# Exemplu de utilizare
print(count_vowels("Hello World"))
