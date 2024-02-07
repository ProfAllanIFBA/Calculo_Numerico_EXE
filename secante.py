import PySimpleGUI as sg
from numpy import*

def f_secante():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def secante(f, a, b, tol,n):

        a = float(a)
        b = float(b)
        tol = float(tol)

        F = lambda x: eval(f)
        if F(a) * F(b) < 0:
            i = 1
            s0 = F(a)
            s1 = F(b)
            delta = float('inf')
            print(f'____________________________________________RESPOSTA_____________________________________________\n'
                  f'Note que f(x) = {f} contínuam em [{a},{b}] e diferenciável em ({a},{b}) com f´(x) não nula em '
                  f'neste aberto. Portanto o método da secante pode ser aplicado. A tabela a seguir mostra as '
                  f'iterações e o erro:')
            print(
                '                                                                 n               pn                            en')
            while tol < delta:
                if i==n:
                    print('O método atingiu a quantidade máxima de iterações.')
                    break
                p = b - s1 * (b - a) / (s1 - s0)
                i = i + 1
                delta = abs(b - p)
                a = b
                s0 = s1
                b = p
                s1 = F(p)
                print(f'                                                                 %0.0f   %0.13f    %0.13f' % (i, p, delta))
            return print(f'Resultado: {p}')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método da Secante')],
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
                f_lambda(1 / pi + e)
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

            secante(f, a, b, tol,n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter o zero de f(x) = x**2-2, pertencente ao intervalo [0,2], aplicando o método '
                  'da secante com tolerância delta = 0.1 e um número máximo de N = 10 iterações, digite na primeira '
                  'entrada x**2-2, na segunda entrada 0, na terceira entrada 2, na quarta entrada 0.1 e na quinta '
                  'entrada 10. A resposta esperada é:\n' 
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Note que f(x) = x**2-2 contínuam em [0.0,2.0] e diferenciável em (0.0,2.0) com f´(x) não nula em '
                  'neste aberto. Portanto o método da secante pode ser aplicado. A tabela a seguir mostra as iterações '
                  'e o erro:\n'
                  '                                                                 n               pn                            en\n'
                  '                                                                 2   1.0000000000000    1.0000000000000\n'
                  '                                                                 3   1.3333333333333    0.3333333333333\n'
                  '                                                                 4   1.4285714285714    0.0952380952381\n'
                  'Resultado: 1.4285714285714286\n'
                  '___________________________________________________________________________________________________\n')
    window.close()
