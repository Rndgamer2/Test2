import random

def moneda():
    x = random.choice(["Cara", "Cruz"])
    return x

print(moneda())