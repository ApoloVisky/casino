from PySimpleGUI import PySimpleGUI as sg

sg.theme("Reddit")
layout = [
    [sg.Text('Usuário'),sg.InputText(key='usuario',size=(50, 50))],
    [sg.Text('Senha'),sg.InputText(key='senha',password_char='*')],
    [sg.Checkbox('Salvar informações?')],
    [sg.Button('Entrar'), sg.Button('Cancelar')]
        ]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or 'Cancelar':
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'adeilton' and valores['senha'] == 123456:
            print('Bem vindo ao casino Royal')
