'''
RODANDO A PRIMEIRA VEZ (PyCharm)
[1] No terminal instale as bibliotecas, PySimpleGUI, webbrowser, os, numpy (e mais alguma se eu esqueci - aparecerá como
erro acusando a falta do módulo)
[2] Rode o arquivo mestre.py

GERANDO UM EXECUTÁVEL .EXE (PyCharm)
[1] Para gerar um arquivo executável coloque todos os arquivos em um mesmo diretório.
[2] No terminal digite
   [2.1] pip install pyinstaller
   [2.2] pyinstaller --onefile mestre.py
[3] O arquivo exe encontra-se na pasta dist
'''


import PySimpleGUI as sg
import webbrowser
import os


def f_mestre():
    layout = [
        [sg.Text('                                   Funcionalidade Disponíveis')],
        [sg.Text('-------------------------------------------Zeros de Funções-------------------------------------------\n'
                 '1 - Localização de Zeros\n'                   
                 '2 - Método da Bissseção\n'
                 '3 - Método do Ponto Fixo\n'
                 '4 - Método da Secante\n'
                 '5 - Método de Newton\n'
                 '6 - Delimitação de Zeros de Polinômios\n'
                 '-----------------------------------------------Interpolação-----------------------------------------------\n'
                 '7 - Polinômio Interpolador (falta ajustar)\n'
                 '-----------------------------------------Mínimos Quadrados------------------------------------------\n'
                 '8 - Ajuste Linear Via Mínimos Quadrados (falta ajustar)\n'
                 '9 - Ajuste Exponencial Via Mínimos Quadrados falta ajustar\n'
                 '------------------------------------------------Integração------------------------------------------------\n'
                 '10 - Regra do Trpézio\n'
                 '11 - Regra de Simpson\n'
                 '12 - Quadratura Gaussiana\n'
                 '---------------------------------------Equações Diferenciais-----------------------------------------\n'
                 '13 - Método de Euler\n'
                 '14 - Método do Ponto Médio\n'
                 '15 - Método de Runge-Kutta de Ordem 4\n'
                 '-----------------------------------------Sistemas Lineares-------------------------------------------\n'
                 '16 - Eliminação Gaussiana\n'
                 '17 - Decomposição LU\n'
                 '18 - Método de Jacobi\n'
                 '19 - Método de Gauss-Seidel\n'
                 '20 - Condicional de Uma Matriz\n',
                 font='defalut 9')],
        [sg.Output(visible=False)],
        [sg.Text('Digite uma das opções acima e aperte seguir:',font='defalut 9')],
        [sg.Input(key='-escolha-', size=(10,1)),
         sg.Button('Seguir', bind_return_key=True)],
        [sg.Text('Autoria: Allan de Sousa Soares, professor do Instituto Federal de Educação, \n'
                 'Ciência e Tecnologia da Bahia - Campus Vitória da Conquista - IFBAVDC',font='defalut 9')],
        [sg.Text('Links Úteis:', font='defalut 9'),
         sg.Button('+Links', bind_return_key=True, font='defalut 9')],
    ]

    window = sg.Window('Cálculo Numérico - youtube: @prof_allanIFBA', layout)


    event = 0

    while True:

        event, values = window.read()


        escolha = values['-escolha-']

        if event == 'Seguir' and escolha == '1':
            from localizacao_zeros import f_localizacao_zeros
            f_localizacao_zeros()

        if event == 'Seguir' and escolha == '2':
            from bissecao import f_bissecao
            f_bissecao()


        if event == 'Seguir' and escolha == '3':
            from ponto_fixo import f_ponto_fixo
            f_ponto_fixo()

        if event == 'Seguir' and escolha == '4':
            from secante import f_secante
            f_secante()

        if event == 'Seguir' and escolha == '5':
            from newton import f_newton
            f_newton()

        if event == 'Seguir' and escolha == '6':
            from delimitacao_zeros import f_demilitacao_zeros
            f_demilitacao_zeros()

        if event == 'Seguir' and escolha == '7':
            from interpolacao import f_interpolacao
            f_interpolacao()

        if event == 'Seguir' and escolha == '8':
            from ajuste_linear import f_ajuste_linear
            f_ajuste_linear()

        if event == 'Seguir' and escolha == '9':
            from ajuste_exponencial import f_ajuste_exponencial
            f_ajuste_exponencial()

        if event == 'Seguir' and escolha == '10':
            from trapezio import f_trapezio
            f_trapezio()

        if event == 'Seguir' and escolha == '11':
            from simpson import f_simpson
            f_simpson()

        if event == 'Seguir' and escolha == '12':
            from quadratura import f_quadratura
            f_quadratura()

        if event == 'Seguir' and escolha == '13':
            from euler import f_euler
            f_euler()

        if event == 'Seguir' and escolha == '14':
            from ponto_medio import f_ponto_medio
            f_ponto_medio()

        if event == 'Seguir' and escolha == '15':
            from runge_kutta_4 import f_runge_kuta_4
            f_runge_kuta_4()

        if event == 'Seguir' and escolha == '16':
            from eliminacao_gaussiana import f_eliminacao_gaussiana
            f_eliminacao_gaussiana()

        if event == 'Seguir' and escolha == '17':
            from decomposicao_LU import f_decomposicao_LU
            f_decomposicao_LU()

        if event == 'Seguir' and escolha == '18':
            from jacobi import f_jacobi
            f_jacobi()

        if event == 'Seguir' and escolha == '19':
            from gauss_seidel import f_gauss_seidel
            f_gauss_seidel()

        if event == 'Seguir' and escolha == '20':
            from condicional import f_condicional
            f_condicional()

        if event == '+Links':
            from links import f_links
            f_links()

while True:

    f_mestre()

