a = 10
b = 15
c = 20
resultado = ((a<b) and (b<c))
print( a<b , " and ", b<c," : ", resultado )
# True and True 
# resultado = True
resultado = ((a>b) and (b<c))
print( a>b, " and ", b<c," : ", resultado )
# Flase and True
# resultado = False
resultado = ((a>b) or (b<c))
print( a>b, " or ", b<c, " : ", resultado )
# False or True
# resultado = True
resultadoNegado = not resultado
print("Not ", resultado,":", resultadoNegado)
# resultado = False 