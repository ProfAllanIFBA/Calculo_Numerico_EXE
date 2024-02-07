import PySimpleGUI as sg
from numpy import*

def f_decomposicao_LU():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def decomposicao_LU(A):

        A = matrix(A, dtype=float)
        n = shape(A)[0]


        U = copy(A)
        n = shape(U)[0]

        L = eye(n)
        for j in arange(n - 1):
            for i in arange(j + 1, n):
                L[i, j] = U[i, j] / U[j, j]
                for k in arange(j + 1, n):
                    U[i, k] = U[i, k] - L[i, j] * U[j, k]
                U[i, j] = 0

        print(f'____________________________________________RESPOSTA_____________________________________________\n'
              f'As matrizes L e U associadas à decomposição LU da matriz em questão são dadas por:\n'
              '  Matriz L\n'
              f'{L}\n'
              '  Matriz U\n'
              f'{U}')
        print('')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Decomposição LU')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('A:'),
         sg.Input(key='-A-', do_not_clear=True,size=(30,1))],
        [sg.Button('Calcular', bind_return_key=True),
         sg.Button('Tutorial'),
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
                if shape(A)[0] != shape(A)[1]:
                    raise Exception('')
            except:
                print(f'Matriz A inválida.\n')
                continue

            decomposicao_LU(A)

        if event == 'Tutorial':
            print(
                '____________________________________________TUTORIAL_____________________________________________\n'
                'Por exemplo, para obter as matrizes L e U associadas a matriz\n'
                '	            	            	            	                           |1   3   2|\n'
                '	            	            	            	                           |2   1  -1|\n'
                '	            	            	            	                           |1   0   1|\n'
                'digite 1,3,2;2,1,-1;1,0,1 na entrada de dados (coeficientes de cada linha da matriz do sistema '
                'separados por "," e linhas separadas por ";"). A solução esperada é:\n'
                '____________________________________________RESPOSTA_____________________________________________\n'
                'As matrizes L e U associadas à decomposição LU da matriz em questão são dadas por:\n'
                '  Matriz L\n'
                '[[1.  0.  0. ]\n'
                '[2.  1.  0. ]\n'
                '[1.  0.6 1. ]]\n'
                '  Matriz U\n'
                '[[ 1.  3.  2.]\n'
                ' [ 0. -5. -5.]\n'
                '[ 0.  0.  2.]]\n'
                '____________________________________________________________________________________________________\n')

    window.close()

