# Soal 1 - Fungsi Pangkat

def pangkat(x, y):
    z = x
    if y == 0:
        return 1
    else:
        for i in range(y-1):
            z = z * x
        return z

print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))