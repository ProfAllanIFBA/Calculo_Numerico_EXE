import PySimpleGUI as sg
from numpy import*

def f_simpson():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def simpson(f, a, b, n):

        F = lambda x: eval(f)
        a = float(a)
        b = float(b)
        n = int(n)

        h = (b - a) / (2 * n)
        x = linspace(a, b, 2 * n + 1)

        I_simp = (h / 3) * (F(x[0]) + 2 * sum(F(x[2:(2 * n) - 1:2])) + 4 * sum(F(x[1:(2 * n):2])) + F(x[(2 * n)]))
        return print(f'____________________________________________RESPOSTA_____________________________________________\n'
                     f'A regra do simpson, para n = {n} ({n} parábolas ou {2 * n + 1} pontos), aplicada a f(x) = {f}, no '
                     f'intervalo [{round(a, 13)},{round(b, 13)}] é igula a {I_simp}.')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Regra do Simpson')],
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
                print("Valor inválido para o número de parábolas.\n")
                continue

            simpson(f, a, b, n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para aplicar a regra de Simpson com n = 2 (2 parábolas que equivalem a 5 pontos) a '
                  'função f(x) = exp(x) de no intervalo [0,1], digite exp(x) na primeira entrada, 0 na segunda, 1 na '
                  'terceira e 2 na quarta. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  f'A regra do simpson, para n = 2 (2 parábolas ou 5 pontos), aplicada a f(x) = exp(x), no intervalo '
                  f'[0.0,1.0] é igula a 1.718318841921747.\n'
                  '__________________________________________________________________________________________________\n')

    window.close()








