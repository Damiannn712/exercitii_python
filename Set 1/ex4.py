def count_occurrences(pattern, text):
    # Initializeaza contorul
    count = 0

    # Parcurge textul pentru a gasi toate aparitiile pattern-ului
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1

    return count


# Exemplu de utilizare
print(count_occurrences("ana", "banana"))
