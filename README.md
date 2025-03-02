# Hanging-man
Server and client side
Hanging Man Game

This project implements a simple "Hangman" game with a client-server architecture. The client interacts with the server to play the game, while the server manages game logic and data persistence.

Features:

Registration and Login: Players can register with a username, ID number, and password, and then log in to play.
Gameplay: The client requests a word from the server and allows the player to guess letters.
Game History: Players can view their game history, including the number of games played, wins, and words used.
Data Persistence: Player data and game history are stored in a JSON file.
Files:

client.py: Contains the client-side logic for interacting with the server and playing the game.
server.py: Contains the server-side logic for handling client requests, managing game data, and providing game functionality.
player.py: Defines the Player class with methods for registration, login, and game history management.
How to Run:

Install Dependencies: Make sure you have the required libraries installed. You can use the provided requirements.txt file:
Bash

pip install -r requirements.txt
Start the Server: Run server.py.
Start the Client: Run client.py.
Note:

The server is designed to run locally on http://127.0.0.1:5000.
The game uses a simple word list stored in game'sWords.txt. You can modify this file to add or change words.

משחק איש תלוי

פרויקט זה מיישם משחק "איש תלוי" פשוט עם ארכיטקטורת שרת-לקוח. הלקוח מתקשר עם השרת כדי לשחק במשחק, בעוד שהשרת מנהל את לוגיקת המשחק ואת שמירת הנתונים.

תכונות:

הרשמה וכניסה: שחקנים יכולים להירשם עם שם משתמש, מספר תעודת זהות וסיסמה, ולאחר מכן להיכנס כדי לשחק.
משחקיות: הלקוח מבקש מילה מהשרת ומאפשר לשחקן לנחש אותיות.
היסטוריית משחקים: שחקנים יכולים להציג את היסטוריית המשחקים שלהם, כולל מספר המשחקים שנערכו, ניצחונות ומילים בהן השתמשו.
שמירת נתונים: נתוני שחקן והיסטוריית משחקים נשמרים בקובץ JSON.
קבצים:

client.py: מכיל את הלוגיקה בצד הלקוח לאינטראקציה עם השרת ולמשחק.
server.py: מכיל את הלוגיקה בצד השרת לטיפול בבקשות לקוח, ניהול נתוני משחק ומתן פונקציונליות משחק.
player.py: מגדיר את מחלקת Player עם שיטות להרשמה, כניסה וניהול היסטוריית משחקים.
כיצד להפעיל:

התקן תלויות: ודא שהספריות הדרושות מותקנות. אתה יכול להשתמש בקובץ requirements.txt שסופק:
Bash

pip install -r requirements.txt
הפעל את השרת: הפעל את server.py.
הפעל את הלקוח: הפעל את client.py.
הערה:

השרת מיועד לפעול באופן מקומי בכתובת http://127.0.0.1:5000.
המשחק משתמש ברשימת מילים פשוטה המאוחסנת ב- game'sWords.txt. אתה יכול לשנות קובץ זה כדי להוסיף או לשנות מילים.
