# Bot de comentários

Bot simples feito em python utilizando a biblioteca pyautogui que comenta automaticamente em sorteios do instagram. (Dado uma lista de vários amigos para uma quantidade limitada de amigos marcados por comentário o bot irá marcar estes de forma aleatória)

## Como usar 💡
Caso não tenha a biblioteca pyautogui na sua máquina, abra o terminal e digite o comando

```
pip install pyautogui
```
e logo após execute o arquivo main.py. Tudo feito, você deve informar quais são os amigos (@) que serão marcados, quantos amigos por comentário o bot irá marcar e o tempo de espera (em segundos) que o bot vai dar a cada publicação de comentário.

Feito o que foi pedido e com seu instagram aberto no post desejado, aperte a tecla ```enter```  e clique na caixa de comentários. Pronto, o bot vai começar com uma espera de 5 segundos e após isso irá marcar os amigos que você informou de forma aleatória. ✅

### Observações ℹ️
1. A cada 60 comentários o bot faz uma pausa preventiva de 1h para que o instagram não bloqueie sua conta;🔒

2. Caso deseje gerar um executável instale a biblioteca <strong>pyinstaller</strong> usando o comando
```
pip install -U pyinstaller
```
2.1 Na pasta do seu projeto use o comando 
```
pyinstaller --onefile main.py
```
2.2 O executável estará numa página chamada "dist" que foi gerada ao rodar esse comando

3. Para interromper o bot apenas finalize a execução do programa ou feche a janela do executável ❌

## Programa funcionando 💻
![repositorio](https://user-images.githubusercontent.com/108037302/211219664-ce5ea4ed-86db-4175-8678-9d5c7aef19dd.gif) 
