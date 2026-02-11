
senha = "pato123"
tolerancia = 1
acessado = False

while tolerancia <= 5 and not acessado:

    tentativa = input("Digite a senha corretamente:")

    if tentativa == senha:
        print("Senha validada.")
        acessado = True
    else: 
        print("Senha incorreta.")
        tolerancia += 1
    

if not acessado:
 print("Tentativas excessivas. Entrada bloqueada.")
