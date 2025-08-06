# Definindo a função com parâmetro perfil
def loginUsuario(perfil):
    # Verificando se o perfil é 'admin', ignorando maiúsculas/minúsculas
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas da função com valor
loginUsuario('Admin')
