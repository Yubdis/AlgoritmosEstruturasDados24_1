carros ="Uno", "Doblo", "Renegade", "Hilux"

print( carros )
print( carros[2] )
print( carros[1:3] )
print( carros[1:-1] )
print( carros[1:-2] )
print( carros[1:-3] )
print( carros[2:] )

# carros[1] = "Fusca"

def calcular(x, y):
    return x+y, x-y, x*y, x/y

print( calcular(10, 5) )

a, b, c, d = calcular(9, 10)
print("Soma: " , a)
print("Subtração: " , b)
print("Mulitplicação: " , c)
print("Divisão: " , d)

resultados = calcular(15, 5)
for x in resultados:
    print(x)