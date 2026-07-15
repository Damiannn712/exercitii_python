import re


def count_words(text):
    # Imparte textul in cuvinte folosind spatii si semne de punctuatie
    words = re.split(r"[ ,;?! .]+", text)

    # Elimina cuvintele goale create de separatorii multipli
    words = [word for word in words if word]

    return len(words)


# Exemplu de utilizare
print(count_words("Salut, lume! Ce faci?"))
