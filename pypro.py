import os
import random
import re

global usn
usn = "vish"


# file=open("reg.txt","a+")
class Reg:

    def __init__(self, name, username, passw, age, gender, email):
        self.name = name
        self.username = username
        self.passw = passw
        self.age = age
        self.gender = gender
        self.email = email

    def data(self):
        file = open("reg.txt", "a+")
        dict = {
            "name": self.name,
            "username": self.username,
            "password": self.passw,
            "age": self.age,
            "gender": self.gender,
            "email": self.email,
        }
        file.write(str(dict) + "\n")
        file.close()


class Login:
    # file=open("reg.txt","a+")
    def __init__(self, username, passw):
        self.username = username
        self.passw = passw

    def check(self):
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                print(data)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    print("Login successful")
                    return
        print("Invalid password or username")

    def create_user_folder(self):
        if not os.path.exists(self.username):
            os.makedirs(self.username)


class profile:
    # file=open("reg.txt","a+")
    def __init__(self, username, passw):
        self.username = username
        self.passw = passw

    def update_name(self, name):
        updated_data = []
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    data["name"] = name
                updated_data.append(data)

        with open("reg.txt", "w") as file:
            for data in updated_data:
                file.write(str(data) + "\n")

    def update_user(self, user):
        updated_data = []
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    data["user"] = user
                updated_data.append(data)

        with open("reg.txt", "w") as file:
            for data in updated_data:
                file.write(str(data) + "\n")

    def update_passw(self, passw):
        updated_data = []
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    data["password"] = passw
                updated_data.append(data)

        with open("reg.txt", "w") as file:
            for data in updated_data:
                file.write(str(data) + "\n")

    def update_age(self, age):
        updated_data = []
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    data["age"] = age
                updated_data.append(data)

        with open("reg.txt", "w") as file:
            for data in updated_data:
                file.write(str(data) + "\n")

    def update_gender(self, gender):
        updated_data = []
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    data["gender"] = gender
                updated_data.append(data)

        with open("reg.txt", "w") as file:
            for data in updated_data:
                file.write(str(data) + "\n")

    def update_email(self, email):
        updated_data = []
        with open("reg.txt", "r") as file:
            for line in file:
                data = eval(line)
                if (
                    data.get("username") == self.username
                    and data.get("password") == self.passw
                ):
                    data["email"] = email
                updated_data.append(data)

        with open("reg.txt", "w") as file:
            for data in updated_data:
                file.write(str(data) + "\n")


class Ran_num:
    def __init__(self, n):
        self.n = n

    def generate_random_numbers(self):
        random_numbers = []
        for _ in range(self.n):
            random_numbers.append(
                random.randint(1, 100)
            )  # Generate random numbers between 1 and 100 (inclusive)
        return random_numbers


class guess:
    def __init__(self, l3, l3_m):
        self.l3 = l3
        self.l3_m = l3_m

    def guess_m(self):
        data = self.l3_m.lower()

        print(self.l3.lower())
        for j in range(9):
            a = input(
                "Guess any letter between (A-Z) or number between (0-9) or the movie:-"
            )
            temp_a=re.escape(a)
            if (re.match(temp_a,self.l3.lower())) and (len(temp_a)==len(self.l3.lower())):
                print("your guess is correct")
                data = self.l3.lower()
                break
            

            elif a in self.l3.lower():
                l = []
                print("That's correct!!!")
                # insted of using i as a element of the list, use i as a index of element.
                for i in range(len(self.l3)):
                    if a == self.l3[i].lower():
                        l.append(i)
                for x in range(len(data)):
                    if x in l:
                        data = data[:x] + a + data[x + 1 :]
                print("-------------------------------------------------------------------------")
                print(data)
                print("-------------------------------------------------------------------------")
                
                # If all the blanks has been filled it will break the loop for next movie name
                temp = data.replace("/", " ")
                if temp == self.l3.lower():
                    print("Congratulation, You've correctly guessed movie name.")
                    break
            else:
                print("Your guess is incorrect, guess again.")

    def store_game_data(self, usn, movie_number, points):
        filename = f"{usn}_game_history.txt"
        with open(os.path.join(usn, filename), "a+") as file:
            file.write(f"Movie Number: {movie_number}, Points: {points}\n")


while True:
    print("-------------------------------------------------------------------------")
    print("Press 1 to register..")
    print("Press 2 to login..")
    print("Enter 3 to update")
    print("Enter 4 to start playing")
    print("Enter 5 to exit")
    print("-------------------------------------------------------------------------")
    try:
        ch = int(input("enter your choice:-"))
        if ch == 1:
            name = input("enter your name:-")
            username = input("enter your username:-")
            password = int(input("enter your password:-"))        
            age = int(input("enter your age:-"))
            gender = input("Enter your gender:-")
            while True:
                email = input("enter your email id:-")

            reg = Reg(name, username, password, age, gender, email)
            reg.data()

        elif ch == 2:
            username = input("enter your username:-")
            password = int(input("enter your password:-")) 
            log = Login(username, password)
            log.check()
            log.create_user_folder()
            usn = username
        elif ch == 3:
            username = input("Enter your username: ")
            password = int(input("enter your password:-"))     
            pro = profile(username, password)
            field_to_update = input(
                "Enter the field you want to update (name, username, password, age, gender, email): "
            )
            new_value = input("Enter the new value: ")

            if field_to_update == "name":
                pro.update_name(new_value)
                print("Name updated")
            elif field_to_update == "user":
                pro.update_user(new_value)
                print("UserName updated")
            elif field_to_update == "password":
                pro.update_passw(new_value)
                print("Password updated")
            elif field_to_update == "age":
                pro.update_age(new_value)
                print("Age updated")
            elif field_to_update == "gender":
                pro.update_gender(new_value)
                print("Nender updated")
            elif field_to_update == "email":
                pro.update_email(new_value)
                print("Email updated")
            else:
                print("No such feild exists....")
        elif ch == 4:
            while True:
                print("\n")
                print("-------------------------------------------------------------------------")
                print("Welcome the THE GAME OF BOLLYWOOD!!!")
                print("Let the game begin!!!")
                print("Select the level of Game..")
                print("1.Easy")
                print("2.Medium")
                print("3.Hard")
                print("-------------------------------------------------------------------------")
                print("\n")
                ch = int(input("Enter your choice:-"))
                if ch == 1:
                    points=0
                    file = open("movies.txt", "r")
                    l = file.readlines()
                    file_m = open("movies_.txt", "r")
                    l_m = file_m.readlines()
                    r = Ran_num(3)
                    l2 = r.generate_random_numbers()
                    l3 = []
                    l3_m = []
                    for i in l2:
                        print(i)
                        l3.append(l[i - 1])
                        l3_m.append(l_m[i - 1])
                    # print(l3)
                    a=1
                    for j in l3:
                        index = l3.index(j)  # Get the index of j in l3
                        print("Movie no. ", a, " is:-")
                        print(l3_m[index])
                        g = guess(l3[index], l3_m[index])
                        ans = g.guess_m()
                        if ans == j:
                            g.store_game_data(usn, index, 10)
                            points=points+10
                        else:
                            g.store_game_data(usn, index, 0)
                            points=points+0
                        a=a+1
                    print("Your total score is:-",points)

                elif ch == 2:
                    points=0
                    file = open("movies.txt", "r")
                    l = file.readlines()
                    file_m = open("movies_.txt", "r")
                    l_m = file_m.readlines()
                    r = Ran_num(5)
                    l2 = r.generate_random_numbers()
                    l3 = []
                    l3_m = []
                    for i in l2:
                        print(i)
                        l3.append(l[i - 1])
                        l3_m.append(l_m[i - 1])
                    # print(l3)
                    for j in l3:
                        index = l3.index(j)  # Get the index of j in l3
                        print("Movie no. ", j, " is:-")
                        print(l3_m[index])
                        g = guess(l3[index], l3_m[index])
                        ans = g.guess_m()
                        if ans == j:
                            g.store_game_data(usn, index, 10)
                            points=points+10
                        else:
                            g.store_game_data(usn, index, 0)
                            points=points+0
                    print("Your total score is:-",points)
                            
                elif ch == 3:
                    points=0
                    file = open("movies.txt", "r")
                    l = file.readlines()
                    file_m = open("movies_.txt", "r")
                    l_m = file_m.readlines()
                    r = Ran_num(7)
                    l2 = r.generate_random_numbers()
                    l3 = []
                    l3_m = []
                    for i in l2:
                        print(i)
                        l3.append(l[i - 1])
                        l3_m.append(l_m[i - 1])
                    # print(l3)
                    for j in l3:
                        index = l3.index(j)  # Get the index of j in l3
                        print("Movie no. ", j, " is:-")
                        print(l3_m[index])
                        g = guess(l3[index], l3_m[index])
                        ans = g.guess_m()
                        if ans == j:
                            g.store_game_data(usn, index, 10)
                            points=points+10
                        else:
                            g.store_game_data(usn, index, 0)
                            points=points+0
                    print("Your total score is:-",points)
                            
                else:
                    break
        elif ch == 5:
            exit()
    except ValueError:
        print("Please enter number only")
    except NameError:
        print("Please enter number only")
    except FileNotFoundError:
        print("Please ensure you have the file you're trying to work with")
    except Exception as e:
        print(e)