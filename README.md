# ROBO-PYTHON
Bot simples feito em python utilizando a biblioteca pyautogui que comenta automaticamente em sorteios do instagram. (Dado uma lista de vários amigos para uma quantidade limitada de amigos marcados por comentário o bot irá marcar estes de forma aleatória)

## Como usar
Caso não tenha a biblioteca pyautogui na sua máquina, abra o terminal e digite o comando
```
pip install pyautogui
```
e logo após execute o arquivo main.py. Após esse processo irá abrir uma interface textual que pede para você informar quais são os amigos (@) que serão marcados; você também terá que informar quantos amigos por comentário o bot irá marcar; por último você deve informar o tempo de espera que o bot vai dar a cada publicação de comentário.
Feito o que foi pedido e com seu instagram aberto no post desejado, aperte a tecla ```enter```  e clique na caixa de comentários. Pronto, o bot vai começar com uma espera de 5 segundos e após isso irá marcar os amigos que você informou de forma aleatória.

### Observações
1 - A cada 60 comentários o bot faz uma pausa preventiva de 1h para que o instagram não bloqueie sua conta
2 - Caso deseje gerar um executável instale a biblioteca pyinstaller usando o comando
```
pip install -U pyinstaller
```
Na pasta do seu projeto use o comando 
```
pyinstaller --onefile "nome-do-seu-arquivo"
```
O executável estará numa página chamada "dist" que foi gerada ao rodar esse comando.
3 - Para parar de comentar apenas finalize a execução do programa ou feche a janela do executável;