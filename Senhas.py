# -*- coding: utf-8 -*-
'''
Criando Senhas com Python

Exemplo de script Python cria senhas seguras em Python

Artigo: https://www.linkedin.com/pulse/criar-senhas-seguras-python-diego-mendes-rodrigues/

Diego Mendes Rodrigues
'''

import random
import string
import time

# Função que cria a senha
def criarSenha(tamanho=16):
    caracteres = []
    caracteres.extend([i for i in string.ascii_letters])
    caracteres.extend([i for i in string.digits])
    caracteres.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])

    senha = ''

    for i in range(tamanho):
        senha += caracteres[random.randint(0, len(caracteres) - 1)]

        random.seed = int(time.time())
        random.shuffle(caracteres)

    return senha

# Criando uma senha
minhaSenha16 = criarSenha()
minhaSenha08 = criarSenha(8)

#Exibindo
print("Senha com 16 caracteres:", minhaSenha16)
print("Senha com 8 caracteres:", minhaSenha08)