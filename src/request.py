import requests
import json
from time import sleep
import PySimpleGUI as sg

layout = [
    [
        sg.Text("Arquivo JSON:")
    ],
    [
        sg.In(size=(43, 1), enable_events=True, key="-FILE-"),
        sg.FileBrowse(button_text='Buscar')
    ],
    [
        sg.Text('Url:'),
    ],
    [
        sg.Input(size=(52, 1), key="-URL-")
    ],
    [sg.Button('Enviar', key='-SEND-', pad=((330,0),(10, 5)))],
    [sg.HSeparator()],
    [sg.Multiline(key='-LOG-', disabled=True, size=(50, 10))]
]

window = sg.Window(title="Requester", layout=layout)
exitLog = []
file = {}
url = ''

def request(url, payload):
    headers = {"Content-type": "application/json"}
    conn = requests.post(url, data=json.dumps(payload), headers=headers)
    print(conn.text)
    exitLog.append(conn.text)
    window['-LOG-'].update('\n'.join(exitLog))

def get_json(path):
    file = open(path)
    return json.load(file)

def send():
    print(url)
    print(file)
    for i in file:
        print(i)
        request(url, i)
        sleep(1)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == '-FILE-':
        file = get_json(values['-FILE-'])
    if event == '-SEND-':
        url = values['-URL-']
        send()
