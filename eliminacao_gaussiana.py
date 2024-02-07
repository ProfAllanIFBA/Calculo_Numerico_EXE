import PySimpleGUI as sg
from numpy import*

def f_eliminacao_gaussiana():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def eliminacao_gaussiana(A,B):

        A = matrix(A, dtype=float)
        B = matrix(B, dtype=float)

        n = len(B)
        x = zeros(n, float)


        for k in range(n - 1):
            if fabs(A[k, k]) < float('inf'):

                for i in range(k + 1, n):
                    if fabs(A[i, k]) > fabs(A[k, k]):
                        A[[k, i]] = A[[i, k]]
                        B[[k, i]] = B[[i, k]]
                        break



            for i in range(k + 1, n):
                if A[i, k] == 0: continue

                factor = A[k, k] / A[i, k]
                for j in range(k, n):
                    A[i, j] = A[k, j] - A[i, j] * factor

                B[i] = B[k] - B[i] * factor

        x[n - 1] = B[n - 1] / A[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            sum_Ax = 0

            for j in range(i + 1, n):
                sum_Ax += A[i, j] * x[j]

            x[i] = (B[i] - sum_Ax) / A[i, i]

        print(f'____________________________________________RESPOSTA_____________________________________________\n'
              f'A solução do sistema em questão, via eliminação gaussiana, é dada por: {x}^T.\n')


################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Eliminação Gaussiana')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('A:'),
         sg.Input(key='-A-', do_not_clear=True,size=(30,1)),
         sg.Text('B:'),
         sg.Input(key='-B-', do_not_clear=True,size=(30,1))],
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

                eliminacao_gaussiana(A, B)
        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para cacular a solução do sistema de equações dado por\n'
				  '	            	            	            	                     x +  y + 3z  = -1\n'
				  '                                                                                   2x +  y  -   z  = 4\n'
				  '                                                                                     x        + 2z  = -1\n'
                  'digite 1,1,3;2,1,-1;1,0,2 na primeira entrada (coeficientes de cada linha da matriz do sistema '
                  'separados por "," e linhas separadas por ";") e -1;4;-1 na segunda entrada (novamente, linhas '
                  'separadas por ";"). A solução esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'A solução do sistema em questão, via eliminação gaussiana, é dada por: [ 1.  1. -1.]^T.\n'
                  '____________________________________________________________________________________________________\n')

    window.close()