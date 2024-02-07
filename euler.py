import PySimpleGUI as sg
from numpy import*

def f_euler():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def euler(f, a, b, w0, n):

        F = lambda t, y: eval(f)
        a = float(a)
        b = float(b)
        w0 = float(w0)
        n = int(n)

        h = (b - a) / n
        t = a
        w = w0
        i = 1
        print(f'____________________________________________RESPOSTA_____________________________________________\n'
              f'Uma aproximação discreta de {n} passos para o PVI  y´={f},  {a} <= t <= {b},  y({a}) = {w0},  via '
              f'método de Euler, é dada por:')
        print(f'                                                                       i                                        w_i')
        print(f'                                                                      %d                            %0.13f' % (i - 1, w))
        while i <= n:
            w = w + h * F(t, w)
            t = a + i * h
            i = i + 1
            print(f'                                                                      %d                            %0.13f' % (i - 1, w))
        print('')
################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Euler')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text("y'(t)(ou f(t,y)):"),
         sg.Input(key='-f-', do_not_clear=True,size=(40,1)),
         sg.Text('a:'),
         sg.Input(key='-a-', do_not_clear=True,size=(10,1)),
         sg.Text('b:'),
         sg.Input(key='-b-', do_not_clear=True,size=(10,1)),
         sg.Text('y(x0):'),
         sg.Input(key='-w0-', do_not_clear=True,size=(10,1)),
         sg.Text('n:'),
         sg.Input(key='-n-', do_not_clear=True,size=(8,1))],
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
        w0 = values['-w0-']
        n = values['-n-']

        if event == 'Calcular':
            try:
                f_lambda = eval('lambda t, y: ' + f)
                f_lambda(1 / pi + e,1 / pi + e)
            except:
                print("Função inválida.\n")
                continue
            try:
                a = float(a)
            except:
                print("Valor inválido para o extremo inferior do intervalo.\n")
                continue
            try:
                b = float(b)
            except:
                print("Valor inválido para o extremo superior do intervalo.\n")
                continue
            try:
                w0 = float(w0)
            except:
                print("Valor inválido para a condição inicial.\n")
                continue
            try:
                n = int(n)
                if n < 1:
                    raise ValueError()
            except:
                print("Valor inválido para o número de pontos.\n")
                continue
            euler(f, a, b, w0, n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter uma aproximação discreta de 2 passos para o PVI  y´=y-t**2+1,  0.0 <= t <= 0.4,  '
                  'y(0.0) = 0.5,  via método de Euler, digite y-t**2+1 na primeira entrada, 0 na segunda, 0.4 na terceira, '
                  '0.5 na quarta e 2 na quinta. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Uma aproximação discreta de 2 passos para o PVI  y´=y-t**2+1,  0.0 <= t <= 0.4,  y(0.0) = 0.5,  via '
                  'método de Euler, é dada por:\n'
                  '                                                                       i                                        w_i\n'
                  '                                                                      0                            0.5000000000000\n'
                  '                                                                      1                            0.8000000000000\n'
                  '                                                                      2                            1.1520000000000\n'
                  '____________________________________________________________________________________________________\n')

    window.close()