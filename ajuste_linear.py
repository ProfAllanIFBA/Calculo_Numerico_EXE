import PySimpleGUI as sg
from numpy import*

def f_ajuste_linear():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def ajuste_linear(x,y):

        x = [float(i) for i in x.split(',')]
        y = [float(i) for i in y.split(',')]

        x = array(x)
        y = array(y)

        A = vstack([x, ones(len(x))]).T
        y = y[:, newaxis]
        alpha = dot((dot(linalg.inv(dot(A.T, A)), A.T)), y)

        if alpha[1,0]>=0:
            sinal = '+'
        else:
            sinal =''

        i = 0
        S = 0
        while i < len(x):
            eq = (y[i] - (alpha[0] * x[i] + alpha[1])) ** 2
            S = S + eq
            i = i + 1
        return print(f'____________________________________________RESPOSTA_____________________________________________\n'
                     f'A reta de regressão é dada por: y={round(alpha[0, 0], 13)}*x{sinal}{round(alpha[1, 0], 13)}. Além disso '
                     f'o erro quadrático é dado por {round(S[0],13)}.')
        #O incremento 10e-15 em ambos os valores garante que não aconteça algo como ax+-0.0 e sim ax+0.0

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Ajuste Linear Via Mínimos Quadrados')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('x1,x2,x3...:'),
         sg.Input(key='-x-', do_not_clear=True, size=(30, 1)),
         sg.Text('y1,y2,y3...:'),
         sg.Input(key='-y-', do_not_clear=True, size=(30, 1))],
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

        x = values['-x-']
        y = values['-y-']

        if event == 'Calcular':
            try:
                if size(ravel(x)) != size(ravel(y)):
                    raise ValueError("")
                ajuste_linear(x, y)
            except:
                print('Cheque os valores inseridos nas coordenadas.')

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter a reta de ajuste que se aproxima dos pontos (1,2.2), (1.5,3.2) e (2,4.3), '
                  'digite na primeira entrada 1,1.5,2 (valores sem espaço e separados por vírgula) e na segunda '
                  '2.2,3.2,4.3. A resposta esperada é: \n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'A reta de regressão é dada por: y=2.1*x+0.0833333333333. Além disso o erro quadrático é dado por '
                  '0.0016666666667.\n'
                  '____________________________________________________________________________________________________\n')

    window.close()