import PySimpleGUI as sg
from numpy import*

def f_bissecao():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def bissecao(f,a,b,tol,n):
        a = float(a)
        b = float(b)
        tol = float(tol)
        n = int(n)

        i = 0
        F = lambda x: eval(f)
        delta = float('inf')

        if F(a) * F(b) > 0:
            return print(f'____________________________________________RESPOSTA_____________________________________________\n'
                         f'O método da bisseção não pode ser aplicado a f(x) = {f} no intervalo [{a},{b}], pois '
                         f'f({a}) = {F(a)} e f({b}) = {F(b)} têm sinais iguais.\n')

        else:
            print(f'____________________________________________RESPOSTA_____________________________________________\n'
                  f'Note que f(x) = {f} é tal que f({a}) = {F(a)} e f({b}) = {F(b)}. Portanto f satisfaz a condição '
                  f'f(a)*f(b) < 0. Sendo f contínua no intervalo [{a},{b}], temos que o método da bissecção pode ser '
                  f'aplicado a este intervalo. A tabela a seguir mostra as iterações e o erro.')

            # Exibe os elementos do título da tabela
            print('                                                                 n               pn                            en')

            while tol < delta:
                if i==n:
                    print('O método atingiu a quantidade máxima de iterações.\n')
                    break
                Fa = F(a)
                p = (a + b) / 2
                i = i + 1
                delta = abs(p - a)
                print(f'                                                                 %0.0f   %0.13f    %0.13f' % (i, p, (b - a) / 2))
                if F(a) * F(p) < 0:
                    b = p
                else:
                    a = p
            return print(f'Resultado: {p} \n')


################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método da Bisseção')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('f(x):'),
         sg.Input(key='-f-', do_not_clear=True,size=(40,1)),
         sg.Text('a:'),
         sg.Input(key='-a-', do_not_clear=True,size=(10,1)),
         sg.Text('b:'),
         sg.Input(key='-b-', do_not_clear=True,size=(10,1)),
         sg.Text('tol:'),
         sg.Input(key='-tol-', do_not_clear=True,size=(10,1)),
         sg.Text('n_max:'),
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
        tol = values['-tol-']
        n = values['-n-']

        if event == 'Calcular':
            try:
                f_lambda = eval('lambda x: ' + f)
                f_lambda(1/pi+e)
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
                tol = float(tol)
                if tol < 0:
                    raise ValueError()
            except:
                print("Valor inválido para a tolerância.\n")
                continue
            try:
                n = int(n)
                if n < 0:
                    raise ValueError()
            except:
                print("Valor inválido para o número máximo de iterações.\n")
                continue

            bissecao(f, a, b, tol,n)


        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter o zero de f(x) = x**2-2, pertencente ao intervalo [0,2], aplicando o método '
                  'da bisseção com tolerância delta = 0.1 e um número máximo de N = 10 iterações, digite na primeira '
                  'entrada x**2-2, na segunda entrada 0, na terceira entrada 2, na quarta entrada 0.1 e na quinta '
                  'entrada 10. A resposta esperada é \n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Note que f(x) = x**2-2 é tal que f(0.0) = -2.0 e f(2.0) = 2.0. Portanto f satisfaz a condição '
                  'f(a)*f(b) < 0. Sendo f contínua no intervalo [0.0,2.0], temos que o método da bissecção pode ser '
                  'aplicado a este intervalo. A tabela a seguir mostra as iterações e o erro.\n'
                  '                                                                 n               pn                            en\n'
                  '                                                                 1   1.0000000000000    1.0000000000000\n'    
                  '                                                                 2   1.5000000000000    0.5000000000000\n'
                  '                                                                 3   1.2500000000000    0.2500000000000\n'
                  '                                                                 4   1.3750000000000    0.1250000000000\n'
                  '                                                                 5   1.4375000000000    0.0625000000000\n'
                  'Resultado: 1.4375\n'
                  '____________________________________________________________________________________________________\n')

    window.close()








