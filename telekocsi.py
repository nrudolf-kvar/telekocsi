# 1. feladat
with open('autok.csv', encoding='latin2') as fajl:
    fejlec = fajl.readline().strip(';').split()
    autok = [sor.strip().split(';') for sor in fajl]
for auto in autok:
    auto[4] = int(auto[4])

# 2. feladat
print(f'2. feladat\n\t{len(autok)} autós hirdet fuvart.')

# 3. feladat
budapest_miskolc = list(filter(lambda x: x[0] == 'Budapest' and x[1] == 'Miskolc', autok))
print(f'3. feladat\n\tÖsszesen {sum(list(map(lambda x: x[4], budapest_miskolc)))} férőhelyet hirdettek az autosok Budapestről '
      f'Miskolcra')

# 4. feladat
legtobb_ferohely = max(autok, key=lambda x: x[4])
print(f'4. feladat\n\tA legtöbb férőhelyet ({legtobb_ferohely[4]}) a(z) {legtobb_ferohely[0]}-{legtobb_ferohely[1]}'
      f' útvonalon ajánlották fel a hirdetők.')

# 5. feladat
with open('igenyek.csv', encoding='latin2') as fajl:
    fejlec_igeny = fajl.readline().strip(';').split()
    igenyek = [sor.strip().split(';') for sor in fajl]
for igeny in igenyek:
    igeny[3] = int(igeny[3])
print('5. feladat')
for az, indulas, cel, szemely in igenyek:
    telekocsi = list(filter(lambda x: x[0] == indulas and x[1] == cel and x[4] >= szemely, autok))
    if len(telekocsi) > 0:
        for kocsi in telekocsi:
            print(f'\t{az}=>{kocsi[2]}')

# 6. feladat
with open('utasuzenetek.txt', 'w', encoding='windows-1252') as fajl:
    for az, indulas, cel, szemely in igenyek:
        telekocsi = list(filter(lambda x: x[0] == indulas and x[1] == cel and x[4] >= szemely, autok))
        if len(telekocsi) > 0:
            print(f'\t{az}: Rendszám: {telekocsi[0][2]} Telefonszám: {telekocsi[0][3]}', file=fajl)
        else:
            print(f'\t{az}: Sajnos nem sikerült autót találni', file=fajl)


