a, b, c = int(input("podaj pierwszą liczę: ")), int(input("podaj druga liczbę: ")), int(input("podaj trecią liczbę: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)


