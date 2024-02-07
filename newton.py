import PySimpleGUI as sg
from numpy import*

def f_newton():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def newton(f,df,p0,tol,n):

        p0 = float(p0)
        tol = float(tol)
        n = int(n)

        i = 0
        F = lambda x: eval(f)
        DF = lambda x: eval(df)
        delta = float('inf')

        if DF(p0) != 0:
            i = 0
            delta = float('inf')

            print(f'____________________________________________RESPOSTA_____________________________________________\n'
                  f'Note que f(x) = {f} contínuam em [a,b] e diferenciável em (a,b) com f´(x) = {df} não nula em '
                  f'neste aberto. Portanto o método de Newton pode ser aplicado. A tabela a seguir mostra as '
                  f'iterações e o erro:')
            print(
                '                                                                 n               pn                            en')
            while tol < delta:
                if i == n:
                    print('O método atingiu a quantidade máxima de iterações.')
                    break
                p = p0 - F(p0) / DF(p0)
                i = i + 1
                delta = abs(p0 - p)
                print(f'                                                                 %0.0f   %0.13f    %0.13f' % (
                i, p, delta))
                p0 = p
        return print(f'Resultado: {p}')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Newton')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('f(x):'),
         sg.Input(key='-f-', do_not_clear=True,size=(40,1)),
         sg.Text("df(x):"),
         sg.Input(key='-df-', do_not_clear=True,size=(40,1))],
        [sg.Text('p0: '),
         sg.Input(key='-p0-', do_not_clear=True,size=(10,1)),
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
        df = values['-df-']
        p0 = values['-p0-']
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
                df_lambda = eval('lambda x: ' + df)
                df_lambda(1 / pi + e)
            except:
                print("Derivada inválida.\n")
                continue
            try:
                p0 = float(p0)
            except:
                print("Valor inválido para o extremo inferior do intervalo.\n")
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

            newton(f, df, p0, tol,n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter o zero de f(x) = x**2-2, pertencente ao intervalo [0,2], aplicando o método '
                  'de Newton, partindo de p0 = 1 (p0 em um intervalo [a,b] adequado), com tolerância delta = 0.1 e um '
                  'número máximo de N = 10 iterações, digite na primeira entrada x**2-2, na segunda entrada 2*x, na '
                  'terceira entrada 1, na quarta entrada 0.01 e na quinta entrada 10. A resposta esperada é \n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Note que f(x) = x**2-2 contínuam em [a,b] e diferenciável em (a,b) com f´(x) = 2*x não nula em neste '
                  'aberto. Portanto o método de Newton pode ser aplicado. A tabela a seguir mostra as iterações e o erro:\n'
                  '                                                                 n               pn                            en\n'
                  '                                                                 1   1.5000000000000    0.5000000000000\n'
                  '                                                                 2   1.4166666666667    0.0833333333333\n'
                  '                                                                 3   1.4142156862745    0.0024509803922\n'
                  'Resultado: 1.4142156862745099\n'
                  '___________________________________________________________________________________________________\n')

    window.close()

