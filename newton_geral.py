import PySimpleGUI as sg
import numpy as np
import ast

def f_newton_geral():

    ################################################DEFININDO A FUNÇÃO DE ITERAÇÃO################################################
    def newton_geral(x, y, tol, N, f, Jf):
        Jf = np.array(ast.literal_eval(Jf.replace(",", ";")))

        def itr(x, y, f, Jf):
            F = np.array(eval(f))
            invJF = np.linalg.inv(Jf)
            return np.array([x, y]) - np.dot(invJF, F)

        delta = float('inf')

        for k in range(N):
            I0 = np.array([x, y])
            I1 = itr(*I0, f, Jf)
            delta = np.max(np.abs(I1 - I0))
            print(f'n={k + 1}, {I1}, {delta}')
            x, y = I1
            if delta <= tol:
                break

        print(f'A solução é {np.array([x, y])} com erro {delta}.')

    ################################################CONSTRUINDO A INTERFACE################################################
    layout = [
        [sg.Text('Método de Newton Para Duas Variáveis')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('f(x,y):'),
         sg.Input(key='-f-', do_not_clear=True,size=(40,1)),
         sg.Text("Jf(x,y):"),
         sg.Input(key='-Jf-', do_not_clear=True, size=(40, 1))],
        [sg.Text('x0: '),
         sg.Input(key='-x-', do_not_clear=True, size=(10, 1)),
         sg.Text('y0: '),
         sg.Input(key='-y-', do_not_clear=True, size=(10, 1)),
         sg.Text('tol:'),
         sg.Input(key='-tol-', do_not_clear=True, size=(10, 1)),
         sg.Text('n_max:'),
         sg.Input(key='-N-', do_not_clear=True, size=(10, 1))],
        [sg.Button('Calcular', bind_return_key=True),
         sg.Button('Tutorial', bind_return_key=True),
         sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Cálculo Numérico - youtube: @prof_allanIFBA', layout)

    while True:

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit', 'Voltar'):
            break

        if event == 'Calcular':

            f = values['-f-']
            Jf = values['-Jf-']
            x = values['-x-']
            y = values['-y-']
            tol = values['-tol-']
            N = values['-N-']

            f_expr = "'{}'".format(f)
            Jf_expr = "'{}'".format(Jf)

            try:
                f_lambda = lambda x, y: eval(f_expr.format(x=x, y=y))
                f_lambda(float(x), float(y))
            except:
                print("Função inválida.\n")
                continue

            try:
                Jf_array = np.array(ast.literal_eval(Jf_expr))
                Jf_array.astype(float)
            except:
                print("Matriz Jacobiana inválida.\n")
                continue

            try:
                tol = float(tol)
                if tol < 0:
                    raise ValueError()
            except:
                print("Valor inválido para a tolerância.\n")
                continue

            try:
                N = int(N)
                if N < 0:
                    raise ValueError()
            except:
                print("Valor inválido para o número máximo de iterações.\n")
                continue

            newton_geral(x, y, tol, N, f_expr, Jf_expr)

        if event == 'Tutorial':
            print('')

    window.close()