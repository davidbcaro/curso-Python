#Con do while
'''
while True:
    letra = input("Usuario digita la letra 'a': ")
    if letra == 'a':
        break
print("Usuario digitaste una letra diferente a 'a'")
'''
#Con while
letra = input("Usuario digita la letra 'a': ")
while letra == 'a':
    letra = input("Usuario digita la letra 'a': ")
print("Usuario digitaste una letra diferente a 'a'")