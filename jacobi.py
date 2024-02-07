import PySimpleGUI as sg
from numpy import*

def f_jacobi():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def jacobi(A, B, x0, tol, N):

        A = matrix(A, dtype=float)
        B = matrix(B, dtype=float)
        x0 = ravel(matrix(x0))

        tol = float(tol)
        N = int(N)

        n = shape(A)[0]
        x = zeros(n)
        it = 0
        print('____________________________________________RESPOSTA_____________________________________________\n'
              'As iterações e o erro, via método de Jacobi, são dados a seguir:')
        print('                              i           erro                                                 iterações')
        while (it < N):
            it = it + 1
            for i in arange(n):
                x[i] = B[i]
                for j in concatenate((arange(0, i), arange(i + 1, n))):
                    x[i] -= A[i, j] * x0[j]
                x[i] /= A[i, i]

            print('                             %d           %0.13f                           %0.1000s^T' % (it, linalg.norm(x - x0, inf), x))

            if (it == N):
                print('O número de iterações foi execido.')
                print('')
                break

            if (linalg.norm(x - x0, inf) < tol):
                print(f'A solução do sistema é: x{it} = {x}.')
                print('')
                break

            x0 = copy(x)


################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Jacobi')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('A:'),
         sg.Input(key='-A-', do_not_clear=True,size=(30,1)),
         sg.Text('B:'),
         sg.Input(key='-B-', do_not_clear=True,size=(30,1)),
         sg.Text('x0:'),
         sg.Input(key='-x0-', do_not_clear=True,size=(10,1)),
         sg.Text('tol:'),
         sg.Input(key='-tol-', do_not_clear=True,size=(10,1)),
         sg.Text('n:'),
         sg.Input(key='-N-', do_not_clear=True,size=(8,1))],
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
        B = values['-B-']
        x0 = values['-x0-']
        tol = values['-tol-']
        N = values['-N-']

        if event == 'Calcular':

            try:
                A = matrix(A, dtype=float)
                if shape(A)[0] != shape(A)[1]:
                    raise Exception('')
            except:
                print("Matriz A inválida.\n")
                continue

            try:
                B = matrix(B, dtype=float)
                if shape(B)[0] != shape(A)[0]:
                    raise Exception('')
            except:
                print("Matriz B inválida.\n")
                continue

            try:
                x0 = ravel(matrix(x0))
                if len(x0) != shape(B)[0]:
                    raise Exception('')
            except:
                print('Valor inicial inválido.\n')
                continue

            try:
                tol = float(tol)
            except:
                print('Valor de tolerância inválida.\n')
                continue

            try:
                N = int(N)
            except:
                print('Número de iterações inválido.\n')
                continue

            jacobi(A, B, x0, tol,N)

        if event == 'Tutorial':
            print(
                '____________________________________________TUTORIAL_____________________________________________\n'
                'Por exemplo, para cacular, via método de Jacobi, uma aproximação da solução do sistema linear\n'
                '	            	            	            	                    4x  +   y  - 2z  =  1\n'
                '                                                                                      x  + 5y + 2z  =  4\n'
                '                                                                                     2x  -  y  + 6z  = -1\n'
                'partindo de (0,0,0)^T, com precisão 0.1 e um número máximo de N = 10 iterações, digite '
                '4,1,-2;1,5,2;2,-1,6 na primeira entrada (coeficientes de cada linha da matriz do sistema separados '
                'por "," e linhas separadas por ";") e 1;4;-1 na segunda (novamente, linhas separadas por '
                '";"), 0;0;0 na terceira, 0.1 na quarta e 10 na quinta. A solução esperada é:\n'
                '____________________________________________RESPOSTA_____________________________________________\n'
                'As iterações e o erro, via método de Jacobi, são dados a seguir:\n'
                '                             i           erro                                                 iterações\n'
                '                            1           0.8000000000000                           [ 0.25        0.8        -0.16666667]^T\n'
                '                            2           0.2833333333333                           [-0.03333333  0.81666667 -0.11666667]^T\n'
                '                            3           0.0972222222222                           [-0.0125      0.85333333 -0.01944444]^T\n'
                'A solução do sistema é: x3 = [-0.0125      0.85333333 -0.01944444].\n'
                '___________________________________________________________________________________________________\n')

    window.close()








