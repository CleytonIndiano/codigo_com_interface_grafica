from PySimpleGUI import PySimpleGUI as sg


def janela_login():
    sg.theme('Dark')
    layout = [
        [sg.Text('Nome', size=(5,1)), sg.Input(key='nome', size=(20,1))],
        [sg.Text('Senha', size=(5,1)), sg.Input(key='', size=(20,1), password_char='*')],
        [sg.Button('Continuar')]
    ]   
    return sg.Window('Login', layout=layout,finalize=True)


def janela_cadastro():
    sg.theme('Dark')
    layout = [
        [sg.Text('Nome',size=(6,1)), sg.Input(key='usuario',size=(25,1))],
        [sg.Text('Idade',size=(6,1)), sg.Input(key='',size=(3,1))],
        [sg.Text('Cidade',size=(6,1)), sg.Input(key='cidade',size=(25,1))],
        [sg.Text('Bairro',size=(6,1)), sg.Input(key='bairro',size=(25,1))],
        [sg.Text('Rua',size=(6,1)), sg.Input(key='Rua',size=(25,1))],
        [sg.Text('Numero',size=(6,1)), sg.Input(key='numero',size=(5,1))],
        [sg.Button('Cadastrar'), sg.Button('Voltar'), sg.Button('Cancelar')]
    ]
    return sg.Window('Cadastro', layout=layout,finalize=True)
 
   
# Janelas iniciais
janela1, janela2 = janela_login(), None
#Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para a próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_cadastro()
        janela1.hide() 
    # Quando queremos voltar para janela de login
    elif window == janela2 and event == 'Voltar':                                   
        janela2.hide()
        janela1.un_hide()
    # Quando escolher cancelar a janela é fechada
    elif window == janela2 and event == 'Cancelar':
        break
    # Quando a janela for fechada
    elif window == janela2 and event == sg.WIN_CLOSED:
        break
    # Quando for cadastrado
    elif window == janela2 and event == 'Cadastrar': 
        sg.popup('Cadastrado com sucesso')
