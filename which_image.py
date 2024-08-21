def ucgen_mi(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def dortgen_tipi(a, b, c, d):
    if a == b == c == d:
        return "Kare"
    elif a == c and b == d:
        return "Dikdörtgen"
    else:
        return "Sıradan Dörtgen"

def ucgen_tipi(a, b, c):
    if a == b == c:
        return "Eşkenar Üçgen"
    elif a == b or a == c or b == c:
        return "İkizkenar Üçgen"
    else:
        return "Sıradan Üçgen"

def main():
    sekil = input("Üçgen mi Dörtgen mi?: ").capitalize()

    if sekil == "Dörtgen":
        a = float(input("1. Kenar uzunluğunu girin: "))
        b = float(input("2. Kenar uzunluğunu girin: "))
        c = float(input("3. Kenar uzunluğunu girin: "))
        d = float(input("4. Kenar uzunluğunu girin: "))

        tip = dortgen_tipi(a, b, c, d)
        print("Bu dörtgen:", tip)

    elif sekil == "Üçgen":
        a = float(input("1. Kenar uzunluğunu girin: "))
        b = float(input("2. Kenar uzunluğunu girin: "))
        c = float(input("3. Kenar uzunluğunu girin: "))

        if ucgen_mi(a, b, c):
            tip = ucgen_tipi(a, b, c)
            print("Bu üçgen:", tip)
        else:
            print("Bu kenarlar bir üçgen belirtmiyor.")

    else:
        print("Geçersiz giriş! Lütfen 'Üçgen' veya 'Dörtgen' olarak cevap verin.")

if __name__ == "__main__":
    main()
