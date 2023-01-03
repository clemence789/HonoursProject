import PySimpleGUI as sg

#sg.Window(title = "Twitter Sentiment Classifier", layout=[[]], margins=(300, 200)).read()

layout = [[sg.Text("Hello please enter your twitter bearer token")], [sg.Button("OK")]]
sg.Window("Twitter Sentiment Classifier", layout).read()