import secrets
import string

# Funktion som genererar ett säkert lösenord

def generate_secure_password(length=12):
    """
    Skapar ett säkert slumpmässigt lösenord
    med:
    - stora bokstäver
    - små bokstäver
    - siffror
    - specialtecken
    """

    # Alla tillåtna tecken i lösenordet
    characters = (
        string.ascii_lowercase +   # a-z
        string.ascii_uppercase +   # A-Z
        string.digits +            # 0-9
        string.punctuation         # !@#$% osv
    )

    # Bygger lösenordet tecken för tecken
    password = ''.join(
        secrets.choice(characters) for _ in range(length)
    )

    return password

# Huvudprogram

def main():
    # Skapar ett lösenord med minst 12 tecken
    password = generate_secure_password(12)

    print(f"Här är ditt säkra lösenord: {password}")


# Kör programmet
if __name__ == "__main__":
    main()
