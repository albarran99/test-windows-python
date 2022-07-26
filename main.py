import random
from tkinter import *

ram_num_easy = random.randint(1, 10)

ram_num_medium = random.randint(1, 20)

ram_num_hard = random.randint(1, 50)

num_try = 0


def catch_number_easy():
    global num_try

    print(ram_num_easy)

    if int(entry.get()) < ram_num_easy:
        game_message['text'] = '¡es menor que el numero que buscas!'
        num_try += 1

    elif int(entry.get()) > ram_num_easy:
        game_message['text'] = '¡¿a donde vas? ese nuemro es mayor al numero que buscas!'
        num_try += 1

    elif int(entry.get()) == ram_num_easy:
        game_message['text'] = '¡Bien, lo atrapaste!, hiciste ' + str(num_try) + ' intentos antes de encontrarlo'


def catch_number_medium():
    global num_try

    print(ram_num_medium)

    if int(entry.get()) < ram_num_medium:
        game_message['text'] = '¡es menor que el numero que buscas!'
        num_try += 1

    elif int(entry.get()) > ram_num_medium:
        game_message['text'] = '¡¿a donde vas? ese nuemro es mayor al numero que buscas!'
        num_try += 1

    elif int(entry.get()) == ram_num_medium:
        game_message['text'] = '¡Bien, lo atrapaste!, hiciste ' + str(num_try) + ' intentos antes de encontrarlo'


def catch_number_hard():
    global num_try

    print(ram_num_hard)

    if int(entry.get()) < ram_num_hard:
        game_message['text'] = '¡es menor que el numero que buscas!'
        num_try += 1

    elif int(entry.get()) > ram_num_hard:
        game_message['text'] = '¡¿a donde vas? ese nuemro es mayor al numero que buscas!'

        num_try += 1

    elif int(entry.get()) == ram_num_hard:
        game_message['text'] = '¡Bien, lo atrapaste!, hiciste ' + str(num_try) + ' intentos antes de encontrarlo'


window = Tk()
# set window title
window.title("Catch the number!! | Encuentra el numero")
# set window width and height
window.configure(width=500, height=300)
# set window background color

window.configure(bg='lightgray')
entry = Entry()

entry.configure(font=('Ink Free', 10))
entry.pack()

tutorial = Label(window, text='El modo facil consiste en un numero aleatorio entre 1 y 10,'
                              '\n El modo normal es un numero aleatorio entre 1 y 20\n'
                              'El modo dificil consiste en un nuemro entre 1 y 50. buena suerte, ¡Campeón!')
tutorial.pack()

game_message = Label(window, text='(aqui apareceran los mensajes de el juego)')
game_message.pack()

check_easy = Button(window, text='comprobar (modo facil)', command=catch_number_easy)
check_easy.pack()

check_medium = Button(window, text='comprobar (modo normal)', command=catch_number_medium)
check_medium.pack()

check_medium = Button(window, text='comprobar (modo "Dark Souls")', command=catch_number_hard)
check_medium.pack()

window.mainloop()
