import pyautogui
import time

class Login:
    def __init__(self,usuario:str, senha:str) -> None:
        self.usuario = usuario
        self.senha = senha

    def logando(self):
        #Digita no campo usuario o Login de usuario e após isso pressiona a tecla tab para pular para o proximo campo
        pyautogui.write(self.usuario)
        pyautogui.press("tab")

        #Digita no campo senha a senha do usuario e após isso pressiona a tecla enter para confirmar o login
        pyautogui.write(self.senha)
        time.sleep(2)
        pyautogui.press('enter')