# LÓGICA E (and)
# é a lógica do login
# email e senha sejam True

verifica_email = True
verifica_senha = False

verifica_login = verifica_senha and verifica_email
print(verifica_login)

if verifica_login:
    print('Entrar no programa')

# LÓGICA OU (or)
# SOL NO DOM    JOGO BR     CHURRAS NO DOM
# False         True        True

logica_ou = False or False or False
print(logica_ou)

# NOT
negacao = not True
print(negacao)

if not verifica_senha:
    print('Senha incorreta')