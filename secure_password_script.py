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

    # Ser till att minst ett av olika tecken används
    all_characters = lowercase + uppercase + digits + special

    # Fyll resten av lösenordet slumpmässigt
    for _ in range(length - 4):
        password_characters.append(secrets.choice(all_characters))

    # Blanda tecknen så ordningen blir helt slumpmässig
    secrets.SystemRandom().shuffle(password_characters)

    # Gör listan till en sträng (från 0,1,2,3 til 0123)
    password = ''.join(password_characters)
    return password

# Kör Programmet

def main():

    while True:
        user_input = input("\nAnge önskad lösenordslängd (minst 10): \n")

        try:
            length = int(user_input)

            if length < 10:
                print("\nLängden på lösenordet måste innehålla minst 10 tecken.\n")
                continue

            # Korrekt input → bryt loopen
            break

        except ValueError:
            print("\nFelaktig inmatning. Ange ett heltal.\n")

    # Generera lösenordet
    password = generate_secure_password(length)

    #Skriver ut lösenordet
    print(f"Här är ditt säkra lösenord: {password}")

if __name__ == "__main__":
    main()