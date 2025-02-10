medida = float(input("Digite a medida em metros: "))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
centimetros = medida * 100
milimetros = medida * 1000

# km - hm - dam - m - dm - cm - mm

print(f"{medida} metro em Km corresponde a: ", km)     
print(f"{medida} metro em Hm corresponde a: ", hm)     
print(f"{medida} metro em Dam corresponde a: " ,dam)     
print(f"{medida} metro em Dm corresponde a:" ,dm)     
print(f"{medida} metro em Cm corresponde a: " ,centimetros)     
print(f"{medida} metro em Mm corresponde a: " ,milimetros)     
