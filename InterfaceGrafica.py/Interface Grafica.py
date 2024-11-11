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