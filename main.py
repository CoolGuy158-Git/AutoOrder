import secrets
from gtts import gTTS
import random

starter = [
    "6-pc Chicken McNuggets",
    "Chicken McDo",
    "Mac Spaghetti",
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
language = 'en'
speech = gTTS(text=text, lang=language, slow=True, tld='co.uk')
end = secrets.token_hex(4)
speech.save(f'MyOrder{end}.mp3')
print(f"Saved as MyOrder{end}.mp3")

