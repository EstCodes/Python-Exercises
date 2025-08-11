import random
import json
import string
import os
from datetime import datetime

class GenPassword:
    def __init__(self, keyword: str = "", keynumbers: int = 0):
        self.keyword = keyword
        self.keynumbers = keynumbers

    def getKeyword(self) -> None:
        print("""Hello, this is a Secure and local program created by Esteban
To execute this program you should enter a keyword, this is to remember the associate and remember each password.""")

        print("-----------------------------------------------------")

        state = True 

        while state:
            print("Consider these factors to have a strong password: Length and characters. More characters/length better.")
            self.keyword = input("Type here: ")

            if not isinstance(self.keyword, str) or len(self.keyword) < 3 or len(self.keyword) > 20:
                print("The keyword must be a string and have a length of at least 6 characters. Please try again.")
            else:
                print(f"Keyword set to: {self.keyword}, successfully.")
                state = False

    def getKeynumbers(self) -> None:
        print("To execute this program you should enter a keynumber to remember the password.")

        state2 = True

        while state2:
            try:
                self.keynumbers = int(input("Type here: "))
                print(f"Keynumber set to: {self.keynumbers}")
                state2 = False
            except ValueError:
                print("The keynumber must be an integer. Please try again.")
                

    def generatePass(self) -> str:
        if not self.keyword:
            return "Error: Keyword is empty. Please set a keyword first."

        password = list(self.keyword)

        for index, char in enumerate(password):
            options = ["Upper", "Lower"]
            choice_selected = random.choice(options)
            
            if choice_selected == "Upper":
                password[index] = char.upper()
            else:
                password[index] = char.lower()
            
        symbols = ['#', '@', '!', '-', '_', '=', '+', ']', '[', '{', '}', '.', ',', '~', '$', '%', '&', ':', ';', '?', '^']
        selected_symbols = random.sample(symbols, 3)

        password.extend(selected_symbols)
        random.shuffle(password)

        if len(password) > 0:
            insert_index = random.choice(range(len(password) + 1))
            password.insert(insert_index, str(self.keynumbers))

            newCodeGen = random.sample(range(9, 50), k=5)
            # Convert numbers to strings and add them to the end of the password list
            password.extend([str(num) for num in newCodeGen])

        final_password = "".join(password)
        return final_password
    
    def getStorage(self, label, entry_id, password, filename="passwords.json"):
        print("""This step is not mandatory. Do you want to save your password on a local file?
This is actually much easier option than save your passwords on the cloud...""")
        
        optionConfirm = input("Type y/n (Yes or No): ")

        state3 = True

        while state3:
            if optionConfirm == "y" or optionConfirm == "yes":
                print("Alright so lets continue with the process.")
                print("-----------------------------------")
                print("You have a storage file?")

                optionConFile = input("Type y/n (Yes or No): ")

                state4 = True

                while state4:
                    if optionConFile == "y" or optionConFile == "yes" or activation == True:
                        print("Okay lets find where is your file...")

                        if os.path.exists(filename):
                            with open(filename, "r") as file:
                                try:
                                    data = json.load(file)
                                except json.JSONDecodeError:
                                    data = {}

                        else:
                            data = {}

                        entry = {
                            "passID": passId,
                            "password": generate_pwd,
                            "date": date
                        }

                        data[label] = entry

                        with open(filename, "w") as file:
                            json.dump(data, file, indent=4)                        

                        state4 = False 

                    elif optionConFile == 'n' or optionConFile == 'no':
                        print("Its okay we can create a new one from scratch.")
                        # Funcion para crear un archivo

                        empty_data = {}

                        with open("passwords.json", "w") as file:
                            json.dump(empty_data, file, indent=4)

                        print("Empty passwords.json file created.")
                        
                        activation = True
                        state4 = False

                        # Debo conectar esto con lo otro de arriba para continuar con el proceso correctamente...

                    else:
                        print("Sorry but your response doesnt match with none of our options, try again.")


                passId = input(f"The following password: {generate_pwd}, corresponds to which Site or App? (This is to identify): ")
                date = datetime.now().isoformat()
                
                # Aqui se debe recopilar passID, Passwd, Date, Versions



                state3 = False
                
            elif optionConfirm == "n" or optionConfirm == "no":
                print("Thanks for your response. ")
                state3 = False
            else:
                print("Somethings wrong with your answer... please type y/n to confirm.")
    
if __name__ == "__main__":
    password_gen = GenPassword()

    password_gen.getKeyword()
    password_gen.getKeynumbers()

    generate_pwd = password_gen.generatePass()
    print(f"Generated Password: {generate_pwd}")

    password_gen.getStorage()




