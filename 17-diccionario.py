diccionario = {}
diccionario = {
    "python":1,
    "java":2,
    "javascript":3
}
print(diccionario)
print('len(diccionario)=', len(diccionario))
print("diccionario['python']=", diccionario['python'])
diccionario['c++'] = 4
print("diccionario['c++']=4=", diccionario)
diccionario['c++'] = 5
print("diccionario['c++']=5=", diccionario)
del(diccionario['c++'])
print("del(diccionario['c++'])=", diccionario)
diccionario['c/c++'] = [4,5]
print("diccionario['c/c++']=[4,5]=", diccionario)
#diccionario['c/c++'] = (4,5)
#print("diccionario['c/c++']=(4,5)=", diccionario)
diccionario['otros'] = {100,101,102}
print("diccionario['otros']={100,101,102}=", diccionario)