
def realizar_login (senha_correta, max_tentativa):
    for i in range(1, max_tentativa + 1):
        chute = input(f"Tentativa {i}/{max_tentativa}: ")

        if chute == senha_correta:
            return True
    return False 

sucesso = realizar_login("raposa123", 5)

if sucesso:
    print("Acesso concedido!")
else:
    print("Acesso bloqueado!")
