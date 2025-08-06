# Inicializando a variável como string vazia
entrada_idade = ''

# Enquanto o valor convertido para string for diferente de '0'
while str(entrada_idade) != '0':
    # Solicita entrada do usuário
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Exibe o número digitado
    print('Número digitado:', entrada_idade)