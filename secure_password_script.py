#!/usr/bin/env python3
import secrets
import string
import hashlib
import requests

# --------------------------------------------------
# Funktion: Generera ett säkert lösenord
# --------------------------------------------------
def generate_secure_password(length=12):
    """
    Skapar ett säkert lösenord som ALLTID innehåller:
    - minst 1 liten bokstav
    - minst 1 stor bokstav
    - minst 1 siffra
    - minst 1 specialtecken
    """

    if length < 4:
        raise ValueError("Fel vid generering av lösenord, kontakta administratör.")

    # Teckengrupper
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Tvinga fram minst ett tecken från varje grupp
    password_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Alla tillåtna tecken
    all_characters = lowercase + uppercase + digits + special

    # Fyll resten av lösenordet slumpmässigt
    for _ in range(length - 4):
        password_characters.append(secrets.choice(all_characters))

    # Blanda tecknen
    secrets.SystemRandom().shuffle(password_characters)

    # Gör listan till en sträng
    password = ''.join(password_characters)
    return password


# def funktion som Kontrollerar lösenord mot Have I Been Pwned

def check_pwned(password):
    """
    Kontrollerar om lösenordet har förekommit i kända dataläckor
    via Have I Been Pwned API (k-anonymity).
    """

    # Skapar hash av lösenordet
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    # Dela upp hashen
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]

    # API-endpoint
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"

    # Skicka förfrågan
    response = requests.get(url)

    # Gå igenom svarsraderna
    for line in response.text.splitlines():
        suffix, count = line.split(":")

        # Match hittad → lösenordet är läckt
        if suffix == hash_suffix:
            return int(count)

    # Ingen match → lösenordet är inte läckt
    return 0


# Huvudprogrammet

def main():

    while True:
        user_input = input("\nAnge önskad lösenordslängd (minst 10): \n")

        try:
            length = int(user_input)

            if length < 10:
                print("\nLängden på lösenordet måste innehålla minst 10 tecken.\n")
                continue

            break

        except ValueError:
            print("\nFelaktig inmatning. Ange ett heltal.\n")

    # Generera lösenordet
    password = generate_secure_password(length)

    # Visa lösenordet
    print(f"\nHär är ditt säkra lösenord:\n{password}\n")

    # Kontrollera mot Have I Been Pwned
    leak_count = check_pwned(password)

    if leak_count > 0:
        print(f"Lösenordet har hittats i dataläckor {leak_count} gånger.")
        print("Rekommendation: använd INTE detta lösenord.\n")
    else:
        print("Lösenordet har INTE hittats i några kända dataläckor.")
        print("Lösenordet ska vara säkert.\n")


if __name__ == "__main__":
    main()
