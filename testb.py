f=open('archivos/archivo.txt',"r")
while(True):
    fila = f.readline()
    print(fila)
    if not fila:
        break
f.close()