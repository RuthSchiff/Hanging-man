# הדפסת הלוגו בפתיחת המשחק
import random
import time
import requests
session = requests.session()
from player import Player
basic_url="http://127.0.0.1:5000"

logo = """    
    _	 _       
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  |
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""
# פונקציה להדפסת הלוגו של המשחק
def printLogo():
    print(logo)

# יצירת decorator
def decorator(func):
    def wrapper(*arg, **kwargs):
        response = session.get(f'{basic_url}/get_cookie')
        if response.status_code == 200:
            return func(*arg, **kwargs)
        else:
            print("you have to reconnect. ")
            checking()
            ans = input("for play agin press 1 for more options press 2")
            if ans == '1':
               game(player)
            elif ans == '2':
               after(player.name,player.password)
            else:
                print("there is not an valid option 🥱 ")

    return wrapper

def checking():
    ans = input("enter n if you connect y for register:")
    name = input("enter you name:").strip()
    if not name.isalpha():
        while not name.isalpha():
            print("err")
            name = input("enter you name:").strip()
    password = input("enter your password:")
    if not password.isdigit():
        print("err")
        while not password.isdigit():
            print("err")
            password = input("enter your password:")

    if ans.lower()=='y':
        id_number = input("enter your identity:")
        if not id_number.isdigit():
            print("err")
            while not id_number.isdigit():
                print("err")
                id_number = input("enter your identity:")
        # words = {}
        playerr = Player(name , id_number , password , 0 , {} , 0)
        r = session.post(f"{basic_url}/register", json={"name": name, "password": password , "id_number" : id_number
            , "count_games" : 0 , "words" : [] , "count_winner" : 0})
        print(r)
        if r.status_code == 201:
            obj = {'user_name': name}
            response = session.post(f"{basic_url}/set_cookie", json=obj)
            cookie = response.cookies.get_dict()


    elif ans.lower() == 'n':
        playerr = Player(name , None , password ,0 ,None,0)
        r = session.post(f"{basic_url}/login", json={"name": playerr.name, "password": playerr.password})
        if r.status_code == 200:
            obj = {'user_name': name}
            response = session.post(f"{basic_url}/set_cookie", json=obj)
            cookie = response.cookies.get_dict()
        else:
            print("user not fount, try agin")

    return playerr


def get_word():
    response = session.get(f"{basic_url}/get_word")
    if response.status_code == 200:
        words = response.json()
    return words

@decorator
def game(playerr):

    print("hello" + " "+ playerr.name )

    words = get_word()
    random.shuffle(words)

    num = int(input("input num"))%len(words)
    print("============")

    print(len(words[num]))
    # הדפסת פסים כאורך המילה
    guess = ['_'] * len(words[num])
    with open("../איש תלוי.txt",'r') as fileH:
        wordsH = fileH.read().split('r/')
    count = 1
    while count < len(wordsH)-1 and '_' in guess:

        print("guess:")
        print(''.join(guess))
        index = 0
        letterH = input("enter char: ")
        if len(letterH) != 1 or not letterH.isalpha():
            print("please input single char")
            continue
        if letterH in words[num] != -1 or letterH.upper() in words[num] or letterH.lower() in words[num]:
            index = 0
            for l in words[num]:
                if letterH.upper() == l or letterH.lower() == l or letterH == l:
                      guess[index] = l
                index += 1
            print(''.join(guess))
        else:
            count += 1
            print(count)
            # הדפסת המן תלוי על עץ
            if count < len(wordsH):
                print(wordsH[count])
                # הודעת כישלון או הצלחה

    data_game = {
        "name": player.name,
        "password": player.password,
        "word":words[num]
    }
    if count  == len(wordsH)-1 and '_' in guess:
        print("🥲😓😭😪😟☹️😕 you luss")
        session.post(f"{basic_url}/add_game", json=data_game)

        after(playerr.name, playerr.password)
    elif count < len(wordsH)-1 and '_' not in guess:
        print("👍😉😊😁😀🥰😋😃😄👍👍 you win !!!!!!")
        response = session.post(f"{basic_url}/add_game", json=data_game)

        response = session.post(f"{basic_url}/add_winner" , json=data_game)

        word = words[num]
        response = session.post(f"{basic_url}/add_word",
                                json={"name": playerr.name, "password": playerr.password, "word": word})

        print("***********")
        after(playerr.name,playerr.password)

@decorator
def after(name, password):
    qwestchen = input("""Choose one of the following options:
    If you want to continue playing press 1,
    If you want to see your game history - press 2,
    To exit press 3  """)

    if qwestchen == '1':
       game(player)
    elif qwestchen == '2':
        response = session.post(f"{basic_url}/get_history",
                                json={"name": name, "password": password})
        if response.status_code == 200:
            print("your history 🧾:")
            print(response.json())
            print("***********")
        return
    elif qwestchen == '3':
        return

if __name__ == "__main__":

    player = checking()
    printLogo()
    game(player)