import webbrowser
import pyautogui
import time
from Login import Login

class Navegacao:
    def __init__(self, url:str, usuario:str, senha:str) -> None:
        self.url:str = url
        self.usuario:str = usuario
        self.senha:str = senha

    def abrir_navegador(self):
        #Abre o navegador com a url para realizar o login
        webbrowser.open(self.url)
        time.sleep(30)
        #cria o objeto e chama a função que preenche e realiza o login
        logar = Login(self.usuario, self.senha)
        time.sleep(5)
        logar.logando()
        time.sleep(10)
        #abre a aba do painel e em seguida pressiona a tecla F11 para colocar em fullScreen
        webbrowser.open(self.url)
        pyautogui.press('f11')
        time.sleep(3)
        #move o mouse para uma coordenada e adiciona um click para certificar de que o navegadr não fique em segundo plano
        pyautogui.moveTo(700,700)
        pyautogui.click()
