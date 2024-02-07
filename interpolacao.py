import PySimpleGUI as sg
from numpy import *


def f_interpolacao():
#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def interpolacao(x,y,x0):

        x = [float(i) for i in x.split(',')]
        y = [float(i) for i in y.split(',')]
        x0 = float(x0)

        x1 = ravel(x)
        x2 = ravel(y)

        x = array(x)
        y = array(y)

        pol = polyfit(x, y, len(x) - 1)  # polynomial coefficients
        xx = linspace(min(x), max(x))
        yy = polyval(pol, xx)  # polynomial value in the points contained in xx
        i=len(x)
        print('____________________________________________RESPOSTA_____________________________________________\n'
             f'Os coeficientes do polinômio interpolador de grau {i-1} são: ', end='')
        for coefficient in pol:
            if i>1:
                print(f'a{i-1} = {round(coefficient,13)}', end=', ')
            else:
                print(f'a{i - 1} = {round(coefficient,13)}', end='. ')
            i=i-1
        print(f'Além disso, P({x0}) = {round(polyval(pol, x0),13)}.\n')


#################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Polinômio Interpolador')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('x1,x2,x3,...:'),
         sg.Input(key='-x-', do_not_clear=True, size=(30, 1)),
         sg.Text('y1,y2,y3,...:'),
         sg.Input(key='-y-', do_not_clear=True, size=(30, 1)),
         sg.Text('x0'),
         sg.Input(key='-x0-', do_not_clear=True, size=(10, 1))],
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
        x0 = values['-x0-']

        if (event == 'Calcular'):

            try:
                x0 = float(x0)
                if size(ravel(x)) != size(ravel(y)) or size(ravel(x)) != 1:
                    raise ValueError('')
                interpolacao(x,y,x0)
            except:
                print('Coordenadas ou valor de avaliação inválidos.')

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter os coeficientes do polinômio interpolador de grau 2 que passa pelos pontos '
                  '(0,6), (1,2) e (-1,12) e avaliá-lo em x0 = 1, digite 0,1,-1 na primeira entrada (abscissas), 6,2,12 '
                  'na segunda entrada (ordenadas) e 1 na terceira. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Os coeficientes do polinômio interpolador de grau 2 são: a2 = 1.0, a1 = -5.0, a0 = 6.0. Além disso, '
                  'P(1.0) = 2.0.\n'
                  '___________________________________________________________________________________________________\n')







    window.close()



'''
                          
'''