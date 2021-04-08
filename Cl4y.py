# Criador do Gerador #Cl4y#
#!/bin/bash
#!/usr/bin/env python3
import random 
from random import randint
from time import sleep
import random 
import getpass
from time import sleep
clear = lambda: os.system('clear')

opcao = 0
# Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

task = ("ℂ𝕝𝟜𝕪 ",  " ʎߤʅϽ ", " C̶l̶4̶y̶ ", " C͔̟͇l̡̻͉4̙̺͜y̡͙͍ ", " C͊̐͒l͆̓͘4͋̾y̔͝ ", " 𝖢𝗅𝟦𝗒 ", " 𝘊𝘭4𝘺 ", " C̵͎̞̾̀̐l̵͕͚͓̓̐̔4̴̺͚͆͊́y̴͎͖̝͐͌̚ ", " C̷l̷4̷y̷ ", " C̲l̲4̲y̲ ", " C⃨l⃨4⃨y⃨ ", " C̳l̳4̳y̳ ", " C̅l̅4̅y̅ ", " 𝐶𝑙4𝑦 ", " 𝘾𝙡4𝙮 ", " 𝕮𝖑4𝖞 ", " ℭ𝔩4𝔶 ", " 𝒞𝓁4𝓎 ", " 🅲🅻4🆈 ", " 🅒🅛➍🅨 ", " Ⓒⓛ④ⓨ ", " 𝄴ₗ₄y ", " 🇨​​​​​🇱​​​​​4🇾​​​​​ ", )
askli = random.choice(task)

print(f'''{G}[!] isenção de responsabilidade legal: o uso de ferramentas Cl4y para gerar algo sem consentimento mútuo prévio é ilegal. É responsabilidade do usuário final obedecer a todas as leis locais, estaduais e federais aplicáveis. Os desenvolvedores não assumem nenhuma responsabilidade e não são responsáveis ​​por qualquer uso indevido por este programa.
                ''')
sleep(3)

print(f''' {B}╔════•ೋೋ•════╗''') 
print(f''' {R}                 ''', askli)
print(f''' {B}╚════•ೋೋ•════╝
             ''')
sleep(2)
       
print(f'''
{R}Data            :       {G} 2021-04-08 {R} Quinta {G} 12:44:46
{R}Link            :       {G} https://github.com/Hack-Cl4y
{R}Cidade          :       {B} SP
{R}País            :       {G} Brasil
{R}Região          :       {B} Sudeste
{R}Agente do Usuário:       {G} Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
''')
sleep(1)
print(f'''{R}Desenvolvedor  :{B}''', askli)
sleep(5)
print(f'''                   
{R}████████╗ ██████╗  ██████╗ ██╗     ███████╗
{B}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{C}   ██║   ██║   ██║██║   ██║██║     ███████╗
{Y}   ██║   ██║   ██║██║   ██║██║     ╚════██║
{RT}   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{R}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {G}V.Beta.1
{G} Obrigado a todos, pelo o uso dessa ferramenta{C} !'''
)

def cpf_validate(numbers):
    #Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9,11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def cpf_generate():
    #  Gera os primeiros nove dígitos (e certifica-se de que não são todos iguais)
    while True:
        cpf = [randint(0,9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    #  Gera os dois dígitos verificadores
    for i in range(9,11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    #  Retorna o CPF como string
    result = ''.join(map(str, cpf))
    return result

print (f'''{B}                 [ 1{G} ✓{B} ] {G} Validar.{C}''')
sleep(1)
print()
print (f'''{B}                 [ 2{G} ✓{B} ] {G} Gerar CPF. {C}''')
sleep(1)


opcao = int(input(f''' {G}[ + ]Opcao:--> {C} '''))

if opcao == 1:
    cpf = input(f'''{Y} [ + ] Digite o CPF sem pontos e traços:{G} ''')
    if cpf_validate(cpf):
        print(f'''{G} [ + ]  {B}[ {G} ✓ {B} ] {G} CPF Válido:-->{C}    ''')
        

        sleep(1)
    else:
        print(f'''{R} [ - ]  {R}[ x ] CPF Inválido:-->{C}      ''')
       

elif opcao == 2:
    cpf = cpf_generate() 
    if cpf_validate(cpf):
        print(f'''{Y}[ + ] ############# {G} CPF Gerado:--> {B} {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} ''')






