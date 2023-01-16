import random
import pyautogui

class Bot:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def comentar(self):
        lista = self.nome
        p = random.sample(lista, self.quantidade)
        
        for i in range(self.quantidade):
            pyautogui.typewrite(f'{p[i]} ')
            
        pyautogui.press('enter')
    