'''
A simple program in GUI which find number of specific word in text file
'''
import re
import PySimpleGUI as sg
#creating GUI layout
layout = [
    [sg.Text('Wpisz proszę słowa których szukasz w pliku.')],
    [sg.FileBrowse(), sg.InputText('Plik')],
    [sg.Text('Szukane słowo: ', size=(15, 1)), sg.InputText('')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Ile razy występuje w tekstcie dane słowo.').Layout(layout)
button, values, = window.Read()

#function which get input from values[1] and count numbers of words
def regex(txt):
    '''
    simply function to find a word
    '''
    book_regex = re.compile(values[1], re.IGNORECASE)
    mo = book_regex.findall(txt)
    num = 0
    for i in mo:
        num += 1
    sg.Popup('Słowo '+str(values[1])+' występuje '+str(num)+' razy.')

#reading file but this's not all correct
filename = values[0]
try:
    with open(filename, encoding='utf8') as f_obj:
        content = f_obj.read()
except:
    print('Plik '+filename+' nie został znaleziony')


regex(content)
