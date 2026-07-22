import random

zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
passwort = ""

antwort = input("Sonderzeichen benutzen? (ja/nein):")
if antwort == "ja":
    zeichen += "@&€?!$£¥#%"
    
for i in range(12):
    passwort += random.choice(zeichen)
    
print("Dein Passwort:", passwort)
