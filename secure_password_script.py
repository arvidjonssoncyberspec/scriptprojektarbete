import secrets
import string
import hashlib
import requests

# --------------------------------------------------
# Funktion: Generera ett säkert lösenord
# --------------------------------------------------
def generate_secure_password(length=12):
    """
    Skapar ett säkert slumpmässigt lösenord
    med stora bokstäver, små bokstäver,
    siffror och specialtecken.
    """

    # Alla tecken som får användas
    characters = (
        string.ascii_lowercase +   # a-z
        string.ascii_uppercase +   # A-Z
        string.digits +            # 0-9
        string.punctuation         # specialtecken
    )

    # Skapar lösenordet slumpmässigt
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# --------------------------------------------------
# Funktion: Kontrollera lösenord mot Have I Been Pwned
# --------------------------------------------------
def check_password_pwned(password):
    """
    Kontrollerar om lösenordet har förekommit
    i kända dataläckor via Have I Been Pwned API.
    """

    # Skapa SHA-1 hash av lösenordet
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Dela upp hashvärdet enligt k-anonymity
    hash_prefix = sha1_hash[:5]
    hash_suffix = sha1_hash[5:]

    # API-adress
    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"

    # Skicka förfrågan till API:t
    response = requests.get(url)

    # Gå igenom alla hash-suffixar som API:t returnerar
    for line in response.text.splitlines():
        suffix, count = line.split(':')

        # Om hash-suffix matchar -> lösenordet är läckt
        if suffix == hash_suffix:
            return int(count)

    # Om ingen match hittas
    return 0

# --------------------------------------------------
# Huvudprogram
# --------------------------------------------------
def main():
    # Generera lösenord
    password = generate_secure_password(12)

    # Kontrollera mot dataläckor
    leak_count = check_password_pwned(password)

    # Visa resultat (utan att visa lösenordet)
    if leak_count > 0:
        print(f"❌ Lösenordet har förekommit i dataläckor {leak_count} gånger.")
    else:
        print("✅ Lösenordet har INTE hittats i några kända dataläckor.")


# Kör programmet
if __name__ == "__main__":
    main()
