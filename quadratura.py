import PySimpleGUI as sg
from numpy import*

def f_quadratura():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def quadratura(f,a,b,n):

        F = lambda x: eval(f)
        a = float(a)
        b = float(b)
        n = int(n)
        g = lambda t: ((b-a)/2)*F(((b-a)/2)*t + (b+a)/2)


        if n == 2:
            s1 = 1*g(-0.577350269189626)
            s2 = 1*g(0.577350269189626)
            I_quad = s1+s2

        if n == 3:
            s1 = 0.555555555555556*g(0.774596669241483)
            s2 = 0.555555555555556*g(-0.774596669241483)
            s3 = 0.888888888888889*g(0.0000000000)
            I_quad = s1 + s2 + s3

        if n == 4:
            s1 = 0.347854845137454*g( 0.861136311594053)
            s2 = 0.347854845137454*g(-0.861136311594053)
            s3 = 0.652145154862546*g(0.339981043584856)
            s4 = 0.652145154862546*g(-0.339981043584856)
            I_quad = s1 + s2 + s3 + s4

        if n == 5:
            s1 = 0.236926885056189*g(0.906179845938664)
            s2 = 0.236926885056189*g(-0.906179845938664)
            s3 = 0.478628670499366*g(0.538469310105683)
            s4 = 0.478628670499366*g(-0.538469310105683)
            s5 = 0.568888888888889*g(0.000000000000000)
            I_quad = s1 + s2 + s3 + s4 + s5

        if n == 6:
            s1 = 0.171324492379170*g(0.932469514203152)
            s2 = 0.171324492379170*g(-0.932469514203152)
            s3 = 0.360761573048139*g(0.661209386466265)
            s4 = 0.360761573048139*g(-0.661209386466265)
            s5 = 0.467913934572691*g(0.238619186083197)
            s6 = 0.467913934572691*g(-0.238619186083197)
            I_quad = s1 + s2 + s3 + s4 + s5 + s6

        if n == 7:
            s1 = 0.129484966168870*g(0.949107912342759)
            s2 = 0.129484966168870*g(-0.949107912342759)
            s3 = 0.279705391489277*g(0.741531185599395)
            s4 = 0.279705391489277*g(-0.741531185599395)
            s5 = 0.381830050505119*g(0.405845151377397)
            s6 = 0.381830050505119*g(-0.405845151377397)
            s7 = 0.417959183673469*g(0.000000000000000)
            I_quad = s1 + s2 + s3 + s4 + s5 + s6 + s7

        if n == 8:
            s1 = 0.101228536290376*g(0.960289856497536)
            s2 = 0.101228536290376*g(-0.960289856497536)
            s3 = 0.222381034453375*g(0.796666477413627)
            s4 = 0.222381034453375*g(-0.796666477413627)
            s5 = 0.313706645877887*g(0.525532409916329)
            s6 = 0.313706645877887*g(-0.525532409916329)
            s7 = 0.362683783378362*g(0.183434642495650)
            s8 = 0.362683783378362*g(-0.183434642495650)
            I_quad = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8

        if n == 9:
            s1 = 0.2606106964029354*g(0.6133714327005904)
            s2 = 0.2606106964029354*g(-0.6133714327005904)
            s3 = 0.3123470770400029*g(0.3242534234038089)
            s4 = 0.3123470770400029*g(-0.3242534234038089)
            s5 = 0.0812743883615744*g(0.9681602395076261)
            s6 = 0.0812743883615744*g(-0.9681602395076261)
            s7 = 0.1806481606948574*g(0.8360311073266358)
            s8 = 0.1806481606948574*g(-0.8360311073266358)
            s9 = 0.3302393550012598*g(0.0000000000000000)
            I_quad = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9

        if n == 10:
            s1  = 0.0666713443086881 * g(0.9739065285171717)
            s2  = 0.0666713443086881 * g(-0.9739065285171717)
            s3  = 0.1494513491505806 * g(0.8650633666889845)
            s4  = 0.1494513491505806 * g(-0.8650633666889845)
            s5  = 0.2190863625159820 * g(0.6794095682990244)
            s6  = 0.2190863625159820 * g(-0.6794095682990244)
            s7  = 0.2692667193099963 * g(0.4333953941292472)
            s8  = 0.2692667193099963 * g(-0.4333953941292472)
            s9  = 0.2955242247147529 * g(0.1488743389816312)
            s10 = 0.2955242247147529 * g(-0.1488743389816312)
            I_quad = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10

        print(f'____________________________________________RESPOSTA_____________________________________________\n'
              f'A integral, via quadratura gaussiana, com n = {n} ({n} pontos), aplicada a f(x) = {f}, no '
              f'intervalo [{round(a, 13)},{round(b, 13)}] é igul a {I_quad}.')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Quadratura Gaussiana')],
        [sg.Output(size=(100, 15), font='Times 12 bold')],
        [sg.Text('f(x):'),
         sg.Input(key='-f-', do_not_clear=True, size=(40, 1)),
         sg.Text('a:'),
         sg.Input(key='-a-', do_not_clear=True, size=(10, 1)),
         sg.Text('b:'),
         sg.Input(key='-b-', do_not_clear=True, size=(10, 1)),
         sg.Text('n (2 a 10):'),
         sg.Input(key='-n-', do_not_clear=True, size=(10, 1))],
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
                f_lambda(1 / pi + e)
            except:
                print("Função inválida.\n")
                continue
            try:
                a = float(a)
            except:
                print("Valor inválido para o extremo inferior do intervalo de integração.\n")
                continue
            try:
                b = float(b)
            except:
                print("Valor inválido para o extremo superior do intervalo de integração.\n")
                continue
            try:
                n = int(n)
                if n<2 or n>10:
                    raise ValueError()
            except:
                print("Valor inválido para o número de pontos.\n")
                continue

            quadratura(f,a,b,n)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para aplicar quadratura gaussiana com n = 3 a função f(x) = exp(x) de no intervalo '
                  '[0,1], digite exp(x) na primeira entrada, 0 na segunda, 1 na terceira e 2 na quarta. A resposta '
                  'esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  f'A integral, via quadratura gaussiana, com n = 3 (3 pontos), aplicada a f(x) = exp(x), no intervalo '
                  f'[0.0,1.0] é igul a 1.7182810043725227.\n'
                  '__________________________________________________________________________________________________\n')


    window.close()
