#Ralkulator v 1.0


import math
import colorama

init()

print(Back.CYAN)


what = input("Шо робимо? (+, -): " )

a = float( input("ВВеди прерше число: ") )
b = float( input("ВВеди друге число: ") )

if what == "+":
    c = a + b
    print("Результат" + str(c)),
elif what == "-":
    print("Результат" + str(c))
else:
   print("Вибрана невірна операція!")

   input()






