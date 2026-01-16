## Säker Lösenords Generator med Have I Been Pwned Check

Detta projekt är ett enkelt Python-script som genererar ett säkert lösenord och kontrollerar om lösenordet har förekommit i kända dataläckor via tjänsten **Have I Been Pwned**.

Syftet med scriptet är att visa grundläggande kunskap inom:
- säker lösenordsgenerering
- användning av externa API:er
- hashning av lösenord
- grundläggande Python-struktur och felhantering

---

## Funktionalitet

Scriptet gör följande steg:

1. Användaren anger önskad längd på lösenordet  
   - Endast heltal accepteras  
   - Minsta tillåtna längd är 10 tecken  

2. Ett säkert lösenord genereras som alltid innehåller:
   - minst 1 liten bokstav  
   - minst 1 stor bokstav  
   - minst 1 siffra  
   - minst 1 specialtecken  

3. Lösenordet kontrolleras mot **Have I Been Pwned Passwords API**
   - Lösenordet skickas aldrig i klartext
   - SHA-1 hash används tillsammans med k-anonymity

4. Resultatet visas i terminalen
   - Antingen att lösenordet hittats i dataläckor
   - Eller att lösenordet inte finns i kända läckor

---

## Säkerhet

För att skydda lösenordet används:
- `hashlib` för SHA-1-hashning
- Have I Been Pwneds k-anonymity-modell
- Endast de fem första tecknen av hashen skickas till API:t

Detta innebär att hela lösenordet **aldrig exponeras** över nätverket.

---

## Ladda ner Scriptet

1. Öppna terminalen och skriv: git clone https://github.com/arvidjonssoncyberspec/scriptprojektarbete

2. Gå in i projektmappen: cd <scriptprojektarbete>

3. Kör scriptet med en av tre kommandon beroende på vilken path du använder:
   - py secure_password_script.py
   - python secure_password_script.py
   - python3 secure_password_script.py

---

## Example Output

Below is an example of how the script looks when running in the terminal:

![Secure Password Script – Example Output](images/secure_password_script_running.png)

## Krav

- Python 3.x
- Git
- Biblioteket `requests`

Installera `requests` med:

```bash
py -m pip install requests

---