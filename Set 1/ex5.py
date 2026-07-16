def contains_special_characters(text):
    # Defineste caracterele speciale de verificat
    special_chars = {'\r', '\t', '\n', '\a', '\b', '\f', '\v'}

    # Parcurge fiecare caracter din sir
    for char in text:
        # Verifica daca caracterul este unul dintre cele speciale
        if char in special_chars:
            return True

    return False


# Exemplu de utilizare
print(contains_special_characters("Hello\nWorld"))
