import re


def is_prime(number):
    # Verifica daca numarul este mai mic decat 2
    if number < 2:
        return False

    # Verifica daca numarul este divizibil cu un numar mai mic decat el
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def largest_prime_from_string(text):
    # Gaseste toate secventele de cifre din sir
    numbers = re.findall(r"\d+", text)

    # Verifica fiecare numar si pastreaza pe cel mai mare prim
    largest_prime = -1
    for number_str in numbers:
        number = int(number_str)
        if is_prime(number) and number > largest_prime:
            largest_prime = number

    return largest_prime


# Exemplu de utilizare
print(largest_prime_from_string("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"))
