k = 3
nb_poissons = 1
for n in range(36):
    if k == 0:
        nb_poissons += 1
        k = 6
    else:
        k -= 1
    print(k, nb_poissons)
print(nb_poissons)