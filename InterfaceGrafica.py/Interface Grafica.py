# Tkinter
# É o framework GUI padrão do python. Sua sintaxe é simples, possui muitos componentes para interação com o usuário. 
# Além disso, seu código é aberto e é disponível sob a licença python. Caso ela não esteja instalada na sua versão do python, basta digitar o comando:

import tkinter
tkinter._test()

# Flexx
# É um kit de ferramentas para o desenvolvimento de interfaces gráficas com o usuário implementado em python que faz uso de tecnologia web para sua renderização. 
# O Flexx pode ser usado para criar tanto aplicações de desktop como para web e até mesmo exportar uma aplicação para um documento HTML independente. 

from flexx import flx
class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()


# CEF python
# É um projeto de código aberto voltado para o desenvolvimento de aplicações com integração ao Google Chrome. 
# Existem muitos casos de uso para CEF. Por exemplo, ele pode ser usado para criar uma GUI baseada em HTML 5, 
# pode usá-lo para testes automatizados, como também pode ser usado para web scraping, entre outras aplicações.

from cefpython3 import cefpython as cef
import platform
import sys

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://www.google.com/", window_title="Olá, mundo! Este é o primeiro exemplo do CEF python") 
    cef.MessageLoop() 
    cef.Shutdown()

def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] python {ver} {arch}".format(
        ver=platform.python_version(),
        arch=platform.architecture()[0]
    ))
    assert cef.__version__ >= "57.0", "CEF python v57.0+ required to run this"

if __name__ == '__main__':
    main()

# Kivy
# É um framework python de código aberto para o desenvolvimento de aplicações com interfaces de usuário e multitoque. 
# Ele é escrito em python e Cython, baseado em OpenGL ES 2, suporta vários dispositivos de entrada e possui uma extensa biblioteca de componentes (widgets).
# Com o mesmo código, a aplicação funciona para Windows, macOS, Linux, Android e iOS. Todos os widgets Kivy são construídos com suporte multitoque.

from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')


# Pyforms
# É um framework python 3 para desenvolver aplicações que podem operar nos ambientes Desktop GUI, Terminal e Web. 
# A biblioteca é composta por três sub-bibliotecas, cada uma implementando a camada responsável por interpretar a aplicação Pyforms em cada ambiente diferente:

# Pyforms-gui.
# Pyforms-web.
# Pyforms-terminal.

import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples,self).__init__('ExemploSimples')
        #Definition of the forms fields
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')


#Execute the application
if __name__ == " __main__":
    from pyforms import start_app
    start_app(ExemploSimples)


# PyQt
# Uma aplicação desenvolvida no framework PyQt e executada nas plataformas Windows, macOS, Linux, iOS e Android.

# Trata-se de um framework que aborda, além de desenvolvimento GUI, abstrações de sockets de rede, threads, Unicode, expressões regulares, bancos de dados SQL, OpenGL, XML, entre outras aplicações.

# Suas classes empregam um mecanismo de comunicação segura entre objetos que é fracamente acoplada, tornando mais fácil criar componentes de software reutilizáveis.

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class HelloWindow(QMainWindow):
   def __init__(self):
      QMainWindow.__init__(self)

      self.setMinimumSize(QSize(280, 120))
      self.setWindowTitle("Olá, Mundo! Exemplo PyQT5")

      centralWidget = QWidget(self)
      self.setCentralWidget(centralWidget)

      gridLayout = QGridLayout(self)
      centralWidget.setLayout(gridLayout)

      title = QLabel("Olá Mundo para PyQt", self)
      title.setAlignment(QtCore.Qt.AlignCenter)
      gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   mainWin = HelloWindow()
   mainWin.show()
   sys.exit( app.exec_() )

# wxPython
# É um kit de ferramentas GUI baseadas em uma biblioteca C++ chamada wxWidgets que foi lançada em 1998. 
# O wxpython usa os componentes (widgets) reais na plataforma nativa sempre que possível. 
# Essa, inclusive, é a principal diferença entre o wxpython e outros kits de ferramentas, como PyQt ou Tkinter.

import wx
class Janela(wx.Frame):
   def __init__(self, parent, title):
      super(Janela, self).__init__(parent, title=title, size = (400,300))
      self.panel = ExemploPainel(self)
      self.text_ctrl = wx.TextCtrl(self.panel, pos=(5, 5))
      self.btn_test = wx.Button(self.panel, label='Pressione esse componente!', pos=(5, 55))


class ExemploPainel(wx.Panel):
   def __init__(self, parent):
      super(ExemploPainel, self).__init__(parent)


class ExemploApp(wx.App):
   def OnInit(self):
      self.frame = Janela(parent=None, title="Janela wxPython")
      self.frame.Show()
      return True


app = ExemploApp()
app.MainLoop()


# PyAutoGUI
# Permite desenvolver aplicações python que controlem o mouse e o teclado para automatizar as interações com outros aplicativos.

import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.click(100, 200)
pyautogui.move(0, 10)
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.write('Olá, Mundo!', interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
pyautogui.alert('Esta é a mensagem para Tela.')


# PySimpleGUI
# Esse pacote foi lançado em 2018 e possui portabilidade com os pacotes: 
# Tkinter, PyQt, wxpython e Remi, portanto aumenta as possibilidades de uso de componentes na programação.

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text('Texto na linha 1')],
  [sg.Text('Entre com um texto na linha 2'), sg.InputText()],
  [sg.Button('Ok'), sg.Button('Cancel')] ]
  window = sg.Window('Bem-Vindo ao PySimpleGUI', layout)

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    break
  print('Você entrou com: ', values[0])

window.close()