import PySimpleGUI as sg
from numpy import*

def f_localizacao_zeros():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################

    def localizacao_zeros(f, a, b, n):

        a = float(a)
        b = float(b)
        n = int(n)

        a0 = a
        b0 = b
        gamma = (b - a) / n
        F = lambda x: eval(f)


        i = 0
        print('____________________________________________RESPOSTA_____________________________________________')
        while a <= b:
            Fa = F(a)
            if Fa == 0:
                i = i + 1
                if i == 1:
                    print(f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros.')
                print(f'-Temos que {a} é um zero de f.')
            a = a + gamma
            Fc = F(a)
            if Fa * Fc < 0:
                i = i + 1
                if i == 1:
                    print(f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros.')
                print(f'-Existe ao menos um zero entre {a - gamma} e {a}.')
        if i != 0:
            print(' ')
        if i == 0:
            print(f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros. Contudo, '
                  f'não localizamos nenhum zero. \n')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Localização de Zeros')],
        [sg.Output(size=(100, 15), font='Times 10 bold'),],
        [sg.Text('f(x):'),
         sg.Input(key='-f-', do_not_clear=True,size=(40,1)),
         sg.Text('a:'),
         sg.Input(key='-a-', do_not_clear=True,size=(10,1)),
         sg.Text('b:'),
         sg.Input(key='-b-', do_not_clear=True,size=(10,1)),
         sg.Text('n:'), sg.Input(key='-n-', do_not_clear=True,size=(10,1))],
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
                f_lambda(0)
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
                n = int(n)
                if n < 0:
                    raise ValueError()
            except:
                print("Valor inválido para a quantidade de pontos.\n")
                continue

            localizacao_zeros(f, a, b, n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para particionar o intervalo [-2,2] em 8 partes à procura de subintervalos contendo '
                  'ao menos um zero da função f(x) = x**2-2 , digite na primeira entrada x**2-2, na segunda -2, na '
                  'terceira 2 e na quarta entrada 8. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Note que f(x) = x**2-2 é contínua em [-2.0,2.0]. Portanto podemos aplicar o método de localização '
                  'de zeros.\n'
                  '-Existe ao menos um zero entre -1.5 e -1.0.\n'
                  '-Existe ao menos um zero entre 1.0 e 1.5.\n'
                  '____________________________________________________________________________________________________\n')

    window.close()

