carro1 = {
    "modelo": "Renegade",
    "ano": 2021 
}
carro2 = {
    "modelo": "Dobro", "ano": 2006 
}
carro3 = {
    "modelo": "Uno", "ano": 2004 
}

print( carro1 )
for chave, valor in carro2.items():
    print( chave , " - " , valor)

print("------------------------------------")
for chave in carro1.keys():
    print( chave , " - " , carro1[chave])
    
frota = carro1, carro2
print( frota )
# frota[1] = carro3
carro2["modelo"] = "fusca"
print("===================================")
print( frota )
