import PySimpleGUI as sg
from numpy import*

def f_demilitacao_zeros():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def delimitacao_zeros(A):
        A = matrix(A, dtype=float)
        C = (1 / A[0, 0]) * A

        L = -float('inf')
        i = 1
        while i <= (size(A) - 1):
            C[0, i] = abs(abs(C[0, i]) ** (1 / i))
            if C[0, i] > L:
                L = C[0, i]
            i = i + 1

        B = matrix(A)
        j = 0
        while j <= (size(A) - 1):
            B[0, j] = A[0, size(A) - j - 1]
            j = j + 1
        D = (1 / B[0, 0]) * B

        L1 = -float('inf')
        k = 1
        while k <= (size(A) - 1):
            D[0, k] = abs(abs(D[0, k]) ** (1 / (k)))
            if D[0, k] > L1:
                L1 = D[0, k]
            k = k + 1

        print('____________________________________________RESPOSTA_____________________________________________\n'
              'Os zeros de P(x) pertencem à união de intervalos: [%0.6f,%0.6f] U [%0.6f,%0.6f].\n'
              % (-2 * L, -1 / (2 * L1), 1 / (2 * L1), 2 * L))
        return



################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Delimitação de Zeros de Um Polinômio')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('an,an-1,...,a1,a0:'),
         sg.Input(key='-A-', do_not_clear=True, size=(30, 1)),
         sg.Button('Calcular', bind_return_key=True),
         sg.Button('Tutorial', bind_return_key=True),
         sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Cálculo Numérico - youtube: @prof_allanIFBA', layout)

    event = 0

    while event != 'Voltar':

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        A = values['-A-']

        if event == 'Calcular':
            try:
                A = matrix(A, dtype=float)
                if shape(A)[0] != 1:
                    raise ValueError("")
                delimitacao_zeros(A)
            except:
                print('Coeficientes inválidos.\n')

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter uma união de intervalos que contém todos os zeros reais de P(x) = '
                  'x**3+3*x**2-10*x+24, digite 1,3,-10,24 (coeficientes do polinômio, na ordem, separados por vírgula '
                  'e sem espaços). A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Os zeros de P(x) pertencem à união de intervalos: [-6.324555,-1.200000] U [1.200000,6.324555].\n'
                  '___________________________________________________________________________________________________\n')


    window.close()


