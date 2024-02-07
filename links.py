import PySimpleGUI as sg
import webbrowser
import os

def f_links():


################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Output(visible=False)],
        [sg.Text('Clique nos botões para navegar nas minhas páginas!')],
        [sg.Text('Canal: Matemática Para Gente Grande', font='defalut 10'),
         sg.Button('Canal', bind_return_key=True, font='defalut 10')],
        [sg.Text('Playlist: Cálculo Numérico                  ', font='defalut 10'),
         sg.Button('Playlist 1', bind_return_key=True, font='defalut 10')],
        [sg.Text('Playlist: Matemática com Python        ', font='defalut 10'),
         sg.Button('Playlist 2', bind_return_key=True, font='defalut 10')],
        [sg.Text('Meu GitHub (Todos os códigos)           ', font='defalut 10'),
         sg.Button('GitHub', bind_return_key=True, font='defalut 10')],
        [sg.Text('Acesse o Código Completo:                ', font='defalut 10'),
         sg.Button('Código', bind_return_key=True, font='defalut 10')],
        [sg.Text('Tutorial Rápido de Uso:                       ', font='defalut 10'),
         sg.Button('Tutorial 1 ', bind_return_key=True, font='defalut 10')],
        [sg.Text('Tutorial Rápido de Construção:            ', font='defalut 10'),
         sg.Button('Tutorial 2 ', bind_return_key=True, font='defalut 10')],
        [sg.Text('Autoria: Allan de Sousa Soares, professor do Instituto Federal de Educação, \n'
                 'Ciência e Tecnologia da Bahia - Campus Vitória da Conquista - IFBAVDC')],
        [sg.Button('Voltar', bind_return_key=True)]
    ]

    window = sg.Window('Cálculo Numérico - youtube: @prof_allanIFBA', layout)

    event = 0

    while event != 'Voltar':


        if event == 'Voltar':
            break

        if event == None:
            break

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Canal':
            os.system("start \"\" https://www.youtube.com/@prof_allanIFBA")

        if event == 'Playlist 1':
            os.system("start \"\" https://youtube.com/playlist?list=PL8aWdrmfXHiLm6mHduRN0AH5J3QoqdMkI")

        if event == 'Playlist 2':
            os.system("start \"\" https://youtube.com/playlist?list=PL8aWdrmfXHiLeEamnK0PfGjWkosG267bt")

        if event == 'GitHub':
            os.system("start \"\" https://github.com/ProfAllanIFBA")

        if event == 'Código':
            os.system("start \"\" https://github.com/ProfAllanIFBA/calculo_numerico_pysimplegui_v2")

    window.close()