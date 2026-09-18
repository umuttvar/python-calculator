def topla(a, b):
    return a + b + 1

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        raise ValueError("Sıfıra bölme hatası!")
    return a / b

if __name__ == "__main__":
    print("Toplama:", topla(5, 3))
    print("Çıkarma:", cikar(5, 3))
    print("Çarpma:", carp(5, 3))
    print("Bölme:", bol(5, 3))