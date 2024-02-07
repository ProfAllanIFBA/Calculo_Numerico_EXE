import PySimpleGUI as sg
from numpy import*

def f_trapezio():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def trapezio(f, a, b, n):

        F = lambda x: eval(f)
        a = float(a)
        b = float(b)
        n = int(n)

        h = (b - a) / n
        x = linspace(a, b, n + 1)

        I_trap = (h / 2) * (F(x[0]) + 2 * sum(F(x[1:n])) + F(x[n]))
        return print(f'____________________________________________RESPOSTA_____________________________________________\n'
                     f'A regra do trapézio, para n = {n}, aplicada a f(x) = {f}, no intervalo [{round(a, 13)},{round(b, 13)}] '
                     f'é igula a {I_trap}.')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Regra do Trapézio')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('f(x):'),
         sg.Input(key='-f-', do_not_clear=True,size=(40,1)),
         sg.Text('a:'),
         sg.Input(key='-a-', do_not_clear=True,size=(10,1)),
         sg.Text('b:'),
         sg.Input(key='-b-', do_not_clear=True,size=(10,1)),
         sg.Text('n:'),
         sg.Input(key='-n-', do_not_clear=True,size=(10,1))],
        [sg.Button('Calcular', bind_return_key=True),
         sg.Button('Tutorial', bind_return_key=True),
         sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Cálculo Numérico - youtube: @prof_allanIFBA', layout)


    event = 0

    while event != 'Voltar':

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        f = values['-f-']
        a = values['-a-']
        b = values['-b-']
        n = values['-n-']

        if event == 'Calcular':
            try:
                f_lambda = eval('lambda x: ' + f)
                f_lambda(1 / pi + e)
            except:
                print("Função inválida.\n")
                continue
            try:
                a = float(a)
            except:
                print("Valor inválido para o extremo inferior do intervalo de integração.\n")
                continue
            try:
                b = float(b)
            except:
                print("Valor inválido para o extremo superior do intervalo de integração.\n")
                continue
            try:
                n = int(n)
                if n < 1:
                    raise ValueError()
            except:
                print("Valor inválido para o número de trapézios.\n")
                continue

            trapezio(f, a, b, n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para aplicar a regra do trapézio com n = 2 (2 trapézios que equivale a 3 pontos) a '
                  'função f(x) = exp(x) de no intervalo [0,1], digite exp(x) na primeira entrada, 0 na segunda, 1 na '
                  'terceira e 2 na quarta. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                 f'A regra do trapézio, para n = 2, aplicada a f(x) = exp(x), no intervalo [0.0,1.0] é igula a '
                  '1.7539310924648253.\n'
                  '___________________________________________________________________________________________________\n')

    window.close()








