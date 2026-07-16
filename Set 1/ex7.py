def follows_chain(char_len, *strings):
    # Verifica daca exista cel putin doua siruri
    if len(strings) < 2:
        return True

    # Parcurge fiecare pereche de siruri vecine
    for first, second in zip(strings, strings[1:]):
        # Verifica daca al doilea sir incepe cu ultimele caractere ale primului
        if not second.startswith(first[-char_len:]):
            return False

    return True


# Exemplu de utilizare
print(follows_chain(2, "cat", "tiger", "rabbit"))
