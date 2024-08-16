import math

# Öklid Mesafesi hesaplayan fonksiyon
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)

# 2D uzaydaki noktaları içeren liste
noktalar = [(2, 3), (4, 8), (6, 7), (9, 1), (3, 5)]

# Mesafeleri saklayacak liste
mesafeler = []

# Nokta çiftleri arasındaki mesafeleri hesaplayan döngü
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Minimum mesafeyi bulma
minimum_mesafe = min(mesafeler)

# Sonucu yazdırma
print(f"Minimum mesafe: {minimum_mesafe}")
