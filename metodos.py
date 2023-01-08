import random
import pyautogui

class Bot:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    
    def posicoes_aleatorias(self):
        a1 = random.randint(0,len(self.nome)-1)
        a2 = random.randint(0,len(self.nome)-1)
        a3 = random.randint(0,len(self.nome)-1)
        a4 = random.randint(0,len(self.nome)-1)

        if self.quantidade > 4:
            return

        if self.quantidade == 1:
            return a1
        elif self.quantidade == 2 and a1 != a2:
            return a1, a2
        elif self.quantidade == 3 and a1 != a2 and a1 != a3 and a2 != a3:
            return a1, a2, a3
        elif self.quantidade == 4 and a1 != a2 and a1 != a3 and a1 != a4 and a2 != a3 and a2 != a4 and a3 != a4:
            return a1, a2, a3, a4
        else:
            return self.posicoes_aleatorias()

    def comentar(self):
        lista = self.nome
        p = self.posicoes_aleatorias()
        
        if self.quantidade == 1:
            pyautogui.typewrite(f'{lista[p[0]]}')
            pyautogui.press('enter')
        elif self.quantidade == 2:
            pyautogui.typewrite(f'{lista[p[0]]} {lista[p[1]]}')
            pyautogui.press('enter')
        elif self.quantidade == 3:
            pyautogui.typewrite(f'{lista[p[0]]} {lista[p[1]]} {lista[p[2]]}')
            pyautogui.press('enter')
        elif self.quantidade == 4:
            pyautogui.typewrite(f'{lista[p[0]]} {lista[p[1]]} {lista[p[2]]} {lista[p[3]]}')
            pyautogui.press('enter')
        else:
            return
    