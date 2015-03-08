def count_vowels_consonants(word):
    vow_con = {
        "vowels": 0,
        "consonants": 0
    }

    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    for char in word:
        if char in vowels:
            vow_con["vowels"] += 1
        elif char in consonants:
            vow_con["consonants"] += 1

    return vow_con

print(count_vowels_consonants("aaaAcccD"))
