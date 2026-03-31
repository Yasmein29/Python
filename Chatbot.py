import re, random
from colorama import Fore, init
init(autoreset=True)
destins = {"beaches": ["Maladives", "Bora Bora", "Maui"],
           "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
           "cities": ["New York", "Paris", "Venice"]}

jokes = ["Why didn't the wooden car with a wooden engine and wooden wheels move? Because it was wooden work!",
         "Why did the bicycle fall over? Because it was two-tired!",
         "Why did the tomato turn red? Because it saw the salad dressing!"]

def normalize_input(text):
    return re.sub(text.strip.lower())

def recommend():
    print(Fore.SKYBLUE + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You:")
    preference = normalize_input(preference)
    if preference in destins:
        sugestions = random.choice(destins[preference])
        print(Fore.GREEN + f"TravelBot: How about {sugestions}?")
        answer = input(Fore.YELLOW + "You: ").lower()
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestions}!")
        elif answer == "no":
            print(Fore.CYAN + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: Sorry, I will suggest another.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()
    
def packing_tips():
    print(Fore.SKYBLUE + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + "TravelBot: Packing tips for {days} in {location}:")
    print(Fore.GREEN + "Pack versatile clothes")
    print(Fore.GREEN + "Bring chargers and adapters")
    print(Fore.GREEN + "Check the weather forecast")

def jokes():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def showhelp():
    print(Fore.MAGENTA + "I can help you with:")
    print(Fore.GREEN + "Suggest travel spots (say "suggestion")")
    print(Fore.GREEN + "Tell a joke (say "joke")")
    print(Fore.CYAN + "Type "exit" or "quit" to leave")

def chat():
    print(Fore.CYAN + "Welcome to TravelBot!")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    showhelp()
    while True:
        user_input = input(Fore.YELLOW + f"You: {name}").lower()
        user_input = normalize_input(user_input)
        if "recommend" in user_input or "suggestion" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "jokes"in user_input or "funny" in user_input:
            jokes()
        elif "help" in user_input:
            showhelp()
        elif "exit" in user_input or "quit" in user_input:
            print(Fore.GREEN + f"TravelBot: Goodbye, {name}!")
            break
        else: 
            print(Fore.RED + "TravelBot: Sorry, I didn't understand that. Type "help" for options.")

if __name__ == "__main__":
    chat()