score = 99

if score >= 90:
    print("youxiu")
elif score >= 80:
    print("lianghao")

fruits = ["1","2","3","4","5","6","7","8","9"]
for fruit in fruits:
    print(fruit)

a=range(5)
aa=type(a).__name__
print(aa)
s = "Python"
print(f"'Python'[1:4]   = {s[0:2:]!r}")  # yth
print(f"'Python'[::2]   = {s[::2]!r}")  # Pto
print(f"'Python'[::-1]  = {s[::-1]!r}")  # nohtyP
lst = [0, 1, 2, 3, 4, 5]
print(f"lst[-2:] = {lst[-2:]}")
print(f"lst[:4]  = {lst[:4]}")