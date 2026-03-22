import customtkinter as ctk
from gtts import gTTS
import secrets
import pygame
import random

starter = [
    "6-pc Chicken McNuggets",
    "Chicken McDo",
    "Mac Spaghetti"
]

burger = [
    "Big Mac",
    "Quarter Pounder with Cheese",
    "Burger McDo",
    "Double Cheeseburger",
    "Cheeseburger",
    "Mac Crispy Chicken Sandwich",
    "Mac Chicken",
]

fries = [
    "World Famous Fries",
    "Cheese Shake Shake Fries",
    "BBQ Shake Shake Fries",
]

drink = [
    "Coke",
    "Sprite",
    "Mango Passion Fruit Fizz",
    "Green Apple Fruit Fizz"
    "Pineapple Juice",
    "Apple Juice",
    "Fruit McFloat",
    "Coke McFloat"
]

dessert = [
    "Oreo McFlurry",
    "Hot Fudge Sundae",
    "Caramel Sundae",
    "Chocnut Sundae",
    "Apple Pie",
    "Vanilla Cone"
]

text = (
    "Can I have " + random.choice(starter) + ", " +
    "And also, " + random.choice(burger) + ", " +
    "And," + random.choice(fries) + ", " +
    "Also for drink just a " + random.choice(drink) + ", " +
    "For dessert I think I'll have " + random.choice(dessert) + ", " +
    "That's it, thank you"
)
end = secrets.token_hex(4)
def generate():
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=True, tld='co.uk')
    speech.save(f'MyOrder{end}.mp3')
    label.configure(text=f'Saved file as MyOrder{end}.mp3', font=("Helvetica", 20))
def play():
    pygame.mixer.init()
    pygame.mixer.music.load(f'MyOrder{end}.mp3')
    pygame.mixer.music.play()
def showinfo():
    app = ctk.CTkToplevel(root)
    app.geometry('400x200')
    app.resizable(False, False)
    app.title('info')
    app.attributes("-alpha", 0.88)
    line1 = ctk.CTkLabel(app, text="This is a cool little project experimenting with text to speech so yea.")
    line2 = ctk.CTkLabel(app, text="Feel free to fork, and yes it generates a new order. Well")
    line3 = ctk.CTkLabel(app, text="Most of the time there's some rare chance it's the same.")
    line4 = ctk.CTkLabel(app, text="Cuz yk, there's a finite amount of options.")
    line5 = ctk.CTkLabel(app, text="It mostly works fine, just a heads up tho.")
    line6 = ctk.CTkLabel(app, text="Hope you enjoy messing around with it!")
    line1.pack()
    line2.pack()
    line3.pack()
    line4.pack()
    line5.pack()
    line6.pack()
root = ctk.CTk()
root.geometry("500x500")
root.attributes("-alpha", 0.88)
label = ctk.CTkLabel(root, height=100, width=100, text='AutoOrder', font=("Helvetica", 90))
label.pack()
button = ctk.CTkButton(root, text='generate', width=200, height=100, command=lambda: generate())
button.pack()
listen = ctk.CTkButton(root, text='play', width=200, height=100, command=lambda: play())
listen.pack(pady=10)
info = ctk.CTkButton(root, text='info', width=50, height=50, command=lambda: showinfo())
info.pack(pady=50)
root.mainloop()