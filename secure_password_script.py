import secrets
import string

# Funktion: Generera ett säkert lösenord

def generate_secure_password(length=12):
    """
    Skapar ett säkert lösenord som ALLTID innehåller:
    - minst 1 liten bokstav
    - minst 1 stor bokstav
    - minst 1 siffra
    - minst 1 specialtecken

    """

    if length < 4:
        raise ValueError("Lösenordets längd måste vara minst 4 tecken.")

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

    # Slå ihop alla tillåtna tecken
    all_characters = lowercase + uppercase + digits + special

    # Fyll resten av lösenordet slumpmässigt
    for _ in range(length - 4):
        password_characters.append(secrets.choice(all_characters))

    # Blanda tecknen så ordningen blir helt slumpmässig
    secrets.SystemRandom().shuffle(password_characters)

    # Gör listan till en sträng
    password = ''.join(password_characters)
    return password

# Run:

def main():
    password = generate_secure_password(12)
    print(password)

if __name__ == "__main__":
    main()
