import requests
session = requests.session()

basic_url="http://127.0.0.1:5000"

# הגדרת בנאי מחלקה
class Player:
    def __init__(self, name, id_number , password , count_games = 0 , words = None , count_winner = 0):
        self.name = name
        self.id_number = id_number
        self.password = password
        self.count_games = count_games
        self.words = []
        self.count_winner = count_winner

    # כאשר רוצים להתחבר שולחים 2 פרמטרים - שם וסיסמא
    def login(self):
        response = session.post(f"{basic_url}/login",
        json={"name":self.name , "password": self.password })

        return response.json()

    # הרשמה - יש להזין 3 פרמטרים
    def register(self):
        response = session.post(f"{basic_url}/register",
        json={"name":self.name ,"id_number": self.id_number,
              "password": self.password , "count_games": self.count_games
            , "words": self.words , "count_winner": self.count_winner  })

        return  response.json()

    # למונה משחקים של המשתמש - הוספת משחק
    def add_game(self):
        self.count_games += 1
    # הוספת ניצחון למשתמש
    def add_winner(self):
        self.count_winner += 1

    # הוספת מילה למערך של המילים בהם המשתמש שיחק
    def add_word(self , word):
        if word not in self.words:
            self.words.append(word)


    # def get_history(self):
    #     return {
    #         "count_games" : self.count_games,
    #         "count_winner" : self.count_winner,
    #         "words" : self.words
    #     }

    def get_history(self):
        response = requests.post(f"{basic_url}/get_history", json={"name": self.name, "password": self.password})
        print(response.json())















