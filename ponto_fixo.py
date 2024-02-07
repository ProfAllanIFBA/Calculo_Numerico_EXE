import PySimpleGUI as sg
from numpy import*

def f_ponto_fixo():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def ponto_fixo(g, p0, tol,n):

        p0 = float(p0)
        tol = float(tol)
        n = int(n)

        G = lambda x: eval(g)
        i = 0
        delta = float('inf')
        print(f'____________________________________________RESPOSTA_____________________________________________'
              f'Note que g([a,b]) está contida em [a,b] com p0 = {p0} neste intervalo e |g´(x)| <= k < 1 para todo x em '
              f'(a,b). Portanto, o método do ponto fixo pode ser aplicado. A tabela a seguir mostra as iterações e o erro:')
        print('                                                                 n               pn                            en')
        while tol < delta:
            if i == n:
                print('O método atingiu a quantidade máxima de iterações.')
                break
            p = G(p0)
            i = i + 1
            delta = abs(p0 - p)
            print(f'                                                                 %0.0f   %0.13f    %0.13f' % (i, p, delta))
            p0=p
        return print(f'Resultado: {p}\n')
################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método do Ponto Fixo')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('g(x):'),
         sg.Input(key='-g-', do_not_clear=True,size=(40,1)),
         sg.Text('p0:'),
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

        g = values['-g-']
        p0 = values['-p0-']
        tol = values['-tol-']
        n = values['-n-']

        if event == 'Calcular':
            try:
                g_lambda = eval('lambda x: ' + g)
                g_lambda(1/pi+e)
            except:
                print("Função inválida.\n")
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

            ponto_fixo(g, p0, tol,n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para aplicar o método do ponto fixo à função g(x)* = log(10/x), partindo de p0 = 1 (p0 '
                  'em um intervalo [a,b] adequado), com uma precisão 0.1 e no máximo 10 iterações, digite na primeira '
                  'entrada log(10/x), na segunda 1, na terceira 0.1 e na quarta 10. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________'
                  'Note que g([a,b]) está contida em [a,b] com p0 = 1.0 neste intervalo e |g´(x)| <= k < 1 para todo x '
                  'em (a,b). Portanto, o método do ponto fixo pode ser aplicado. A tabela a seguir mostra as iterações '
                  'e o erro:\n'
                  '                                                                 n               pn                            en\n'
                  '                                                                 1   2.3025850929940    1.3025850929940\n'
                  '                                                                 2   1.4685526477461    0.8340324452480\n'
                  '                                                                 3   1.9183077706039    0.4497551228578\n'
                  '                                                                 4   1.6511416650660    0.2671661055379\n'
                  '                                                                 5   1.8011181261248    0.1499764610589\n'
                  '                                                                 6   1.7141774397646    0.0869406863602\n'
                  'Resultado: 1.714177439764644\n'
                  '*Observação: log(x/10) = ln(x/10)\n'
                  '____________________________________________________________________________________________________\n')



    window.close()