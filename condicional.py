import PySimpleGUI as sg
from numpy import*

def f_condicional():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def condicional(A):
        A = matrix(A, dtype=float)
        invA = linalg.inv(A)
        condA = linalg.norm(A, inf) * linalg.norm(invA, inf)
        return print(f'____________________________________________RESPOSTA_____________________________________________\n'
                     f'Temos que ||A|| = {linalg.norm(A, inf)} e que ||A^-1|| = {linalg.norm(invA, inf)}. Portanto '
                     f'cond(A) = {condA}.')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Condicional de Uma Matriz')],
        [sg.Output(size=(100, 20), font='Times 12 bold')],
        [sg.Text('Insira a matriz:')],
        [sg.Input(key='-A-', do_not_clear=True,size=(30,1))],
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


            condicional(A)
        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para obter o condicional da matriz A dada por\n'
                  '                                                                                              |2   1|\n'
                  '                                                                                              |4   3|\n'
                  'digite 2,1;4,3 (elementos da linha separados por "," e linhas separadas por ";". Não '
                  'insira espaços. A resposta esperada é: \n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'Temos que ||A|| = 7.0 e que ||A^-1|| = 3.0. Portanto cond(A) = 21.0.\n'
                  '____________________________________________________________________________________________________\n')

    window.close()

