import random

ps = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cr = int(input("Elige el numero de caracteres de tu contraseña "))
am = " "
for i in range(cr):
    am += random.choice(ps)
print(am)