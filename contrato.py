from docx import Document
import automação

def forma_pagamento(on=False):
    global a , b , c     
    print('forma de pagamento')
    x = str(input("Cartão digite[1] / A vista[2] / Financiamento[3]: "))    
    if x == '1':
        a = 'X'
    elif x == '2':
        b = 'X'
    elif x == '3':
        c = 'X'
    return 


documento_contrato = Document('Modelo.docx')
nome = str(input("Nome: "))
cpf = str(input("CPF: "))
cep = str(input("Cep:"))
endereco = str(input("Endereço: "))
email = str(input('Email: '))
telefone = str(input('Telefone: '))
data_entrega = str(input('Data entrega: '))
kwp = str(input('KWP: '))
valor = str(input("Valor: "))
a = ''
b = ''
c = ''
forma_pagamento(on=True)
local = str(input('Local: '))

dados = {
     'NOME': nome,
     'YYYY': cpf,
     'CEP': cep,
     'END': endereco,
     'EMAIL': email,
     'TEL': telefone,
     'DD': data_entrega,
     'XXXX': valor,
     'AAAA': a,
     'BBBB': b,
     'CCCC': c,
     'KWP': kwp,
     'LOCAL': local,
}

for linha in documento_contrato.paragraphs:
    for informacao in dados:
        linha.text = linha.text.replace(informacao , dados[informacao])


contratado = str(input("Nome do Contratado: "))
documento_contrato.save(f'Contrato - {contratado}.docx')

automação.enviar_zap(contratado , 'Laiz' , True)
