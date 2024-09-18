# 1 butun son berilgan agar berilgan son musbat bolsa. 1 ga oshirilsin aks xolda ozgartirilmasin. hosil bolgan sonni ekrangga chiqaruvchi programma tuzilsin

# son = int(input("son kiriting: "))

# if son > 9:

#    son += 1

# else:

#    smaller_number = int(input("2chi son: "))

#    son -= smaller_number

# print("natija:", son)
    
    
# 2 butun son  berilgan. agar berilgan son musbat bolsa 1ga oshiring. aks holda 2 ga kamaytring hosil bolgan sonni ekrengga chiqaruvchi programma tuzilsn


# if son > 0 :
#     son +=2
# else:
#     sonlar_kiriting = int(input('son kiriting'))
#     son -= sonlar_kiriting
    
# print('natija',son)

# 3 butun son berilgan. agar berilgan son musbat bolsa 1ga oshring agar manfiy bolsa 2ga kamaytiring agar 0ga teng bolsa 10ni ozlashtirsin hosil bolgan sonni ekranga chiqaruvchi prog tuzing

# son = int(input("1chi son kiriting: "))

# if son > 0:
#    son += 1

# else:

#    smaller_number = int(input("kichik son kiriting: "))

#    son -= smaller_number

# print("natija:", son)

# 4 uchta butun son berilgan shu sonlar orasidan nechta son berilgani aniqlovchi prog tuzilsin
son1 = int(input("1sonni kiriting: "))
son2 = int(input("2sonni kiriting: "))
son3 = int(input("3-sonni kiriting: "))

musbat_sonlar_soni = 0

if son1 > 0:
    musbat_sonlar_soni += 1
if son2 > 0:
    musbat_sonlar_soni += 1
if son3 > 0:
    musbat_sonlar_soni += 1

print(f"Musbat sonlar soni: {musbat_sonlar_soni}")


# 6 2ta butun son berilgan. Shu sonlar kattasini aniqlovchi prog tuzing

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

if a > b:
    print("Kattasi:")
elif b > a:
    print("Kattasi:")
else:
    print("Ikkala son teng.")
    
    
# 7 2 butun son berilgan shu sonning kichik tartib raqamni aniqlovchi prog tuzilsn

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

if a > b:
    print("Kattasi:")
elif b > a:
    print("kichik:")
else:
    print("Ikkala son teng.")


