from auto import Auto
import random

auto1 = Auto('Toyota','Corola',2015)
auto2 = Auto('Ford','Focus',2018)
auto3 = Auto('Audi','E-Tron GT',2020)
auto4 = Auto('Ford','Mustang',2008)


# print(auto1)
# # print(auto1.marka)
# print(auto2)

# auto1.gyorsit(150)
# print(auto1)
# auto2.gyorsit(150)
# print(auto2)
# auto3.gyorsit(150)
# print(auto3)
# auto4.gyorsit(150)
# print(auto4)


autok = [auto1, auto2, auto3, auto4]
for auto in  autok:
    print(auto)

print('\nGyorsítás\n')
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

ossz_eletkor = 0

autok_szama = len(autok)

for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor / autok_szama

print(f'Az autók átlagéletkora: {atlag_eletkor} év')

legidosebb_auto = None
legidosebb_auto_kora = 0

for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    if kor > legidosebb_auto_kora:
        legidosebb_auto_kora = kor
        legidosebb_auto = auto

print(f'A legidősebb autó kora: {legidosebb_auto_kora} ')
print(f'A legidősebb autó adatai: {legidosebb_auto} ')


# Hrdcore

# gyartasi_evek = []

# for auto in autok:
#     gyartasi_evek.append(auto.gyartasi_ev)
# gyartasi_evek = [auto.gyartasi_ev for auto in autok]

# for auto in autok:
#     if auto.gyartasi_ev == min(gyartasi_evek):
#         print(f'A legidősebb autó adatai: {auto}')

auto_6=Auto('BMW', '320d', 2019, 6.5)
print(auto_6)
auto_6.utazik(200)
print(auto_6)
auto_6.tankol(10)
print(auto_6)
