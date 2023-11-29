import random

import pandas
import pandas as pd
from tkinter import *
TEMPORIZADOR = 3000
BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
def  flip_card():
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(word_text, text= random_word["English"], fill= "white")
    canvas.itemconfig(front_canvas, image= back_card1)
#Coger una palabra aleatoria del CSV "french_word".
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict_data= original_data.to_dict(orient="records")
else:
    dict_data = df.to_dict(orient= "records")

random_word = random.choice(dict_data)
french_word = random_word["French"]
def show_random_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(dict_data)
    canvas.itemconfig(card_title, text= "French", fill= "black" )
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    canvas.itemconfig(front_canvas, image= front_card)
    flip_timer = window.after(3000, func=flip_card)
def known():
    dict_data.remove(random_word)
    data = pandas.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv")
    show_random_word()
#Creamos ventana Tk e importamos imagenes y la asociamos a variables.
window = Tk()

flip_timer = window.after(3000, func=flip_card)
window.config(bg= BACKGROUND_COLOR, pady=50, padx=50)
back_card1 = PhotoImage(file="images/card_back.png")
front_card = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

#Creamos canvas necesarios para incluir front y back cards junto a los textos.
canvas = Canvas(width=800,  height=526, highlightthickness= 0, bg=BACKGROUND_COLOR)
front_canvas = canvas.create_image(0,0, image= front_card)
canvas.coords(front_canvas,400,263)
canvas.grid(row=0, column=0, columnspan= 2 )
card_title = canvas.create_text(400, 126, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263 , text= "" , font=("Ariel", 60, "bold"))

#Creamos el boton de "Erroneo".
wrong_button = Button(image= wrong, highlightthickness= 0, command= show_random_word )
wrong_button.grid(row=1, column= 0)

#Creamos el boton de "Correcto".
right_button = Button(image= right, highlightthickness= 0, command=known)
right_button.grid(row=1, column= 1)

show_random_word()

window.mainloop()

