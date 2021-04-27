import random

subjects = ["k", "n", "p"]
poz = ["ano", "yes", "si", "jo", "jop", "jasně"]
nep = ["ne", "nene", "no", "nope", "nein"]

print("Vítejte ve hře: k = kámen, n = nůžky, p = papír. Pojďme začít! :) ")
user_choose = input("Zde napiš svou první volbu: ")
pc_choose = random.choice(subjects)


if user_choose == pc_choose:
    print(f"Je to remíza! Pc vybral: {pc_choose}, uživatel: {user_choose}")

elif (user_choose == "k" and pc_choose== "n")or(user_choose == "p" and pc_choose == "k")or(user_choose == "n" and pc_choose == "p"):
    print(f"Hráč vyhrál. Hráč zvolil: {user_choose} a Pc zvolil: {pc_choose}.")


else:

    print(f"Počítač vyhrál a vybral {pc_choose}. Ty jsi měl: {user_choose}")




















