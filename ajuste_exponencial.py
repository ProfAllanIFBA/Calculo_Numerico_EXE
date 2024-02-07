import PySimpleGUI as sg
from numpy import*

def f_ajuste_exponencial():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################

    def ajuste_exponencial(x, y):

        x = [float(i) for i in x.split(',')]
        y = [float(i) for i in y.split(',')]

        x = array(x)
        y = array(y)

        A = vstack([x, ones(len(x))]).T
        beta, log_alpha = linalg.lstsq(A, log(y), rcond=None)[0]
        alpha = exp(log_alpha)

        i = 0
        S = 0
        while i < len(x):
            eq = (y[i] - alpha * exp(beta * x[i])) ** 2
            S = S + eq
            i = i + 1

        print(f'____________________________________________RESPOSTA_____________________________________________\n'
              f'A exponencial de ajuste é dada por: y = {round(alpha,13)}e**({round(beta,13)}x). Além disso o erro quadrático é dado por'
              f'o erro quadrático é dado por {round(S,13)}.\n')

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
                ajuste_exponencial(x,y)
            except:
                print('Cheque os valores inseridos nas coordenadas.')

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter a exponencial de ajuste que se aproxima dos pontos (1,2.1), (3,6.0) e '
                  '(5,12.2), digite na primeira entrada 1,3,5 (valores sem espaço e separados por vírgula) e na segunda 2.1,6.0,12.2. A resposta esperada é: \n'
                  'A exponencial de ajuste é dada por: \n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'A exponencial de ajuste é dada por: y = 1.4315440733456e**(0.4398746517525x). Além disso o erro '
                  'quadrático é dado poro erro quadrático é dado por 0.9350241515017.\n'
                  '___________________________________________________________________________________________________\n')



    window.close()