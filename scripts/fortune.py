import random

def tell_fortune():
    fortunes = [
        "You will have a great day today.",
        "Something unexpected will happen soon.",
        "You will meet someone new today.",
        "A pleasant surprise awaits you.",
        "Be cautious, a challenge is coming your way.",
        "Good news will come to you by mail.",
        "You will find luck in your personal life.",
        "A new opportunity is just around the corner.",
        "You will have a chance to travel soon.",
        "You will have a long and healthy life."
    ]

    colors = ["red", "blue", "green", "yellow", "black", "white", "purple", "orange", "pink", "brown"]
    animals = ["dog", "cat", "bird", "fish", "lion", "elephant", "tiger", "bear", "horse", "monkey"]

    print("Welcome to the fortune teller! Please answer the following questions.")

    name = input("What is your name? ")
    color = input("What is your favorite color? ").lower()
    animal = input("What is your favorite animal? ").lower()

    if color in colors and animal in animals:
        print(f"Hello {name}. {random.choice(fortunes)}")
    else:
        print("Sorry, I couldn't tell your fortune. Please try again with a valid color and animal.")
        print("Valid colors are: ", colors)
        print("Valid animals are: ", animals)

tell_fortune()