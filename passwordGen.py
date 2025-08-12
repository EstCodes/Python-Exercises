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
    
        optionConfirm = input("Type y/n (Yes or No): ").strip().lower()
        state3 = True
        activation = False  # Initialize this here

        while state3:
            if optionConfirm in ["y", "yes"]:
                print("Alright, so let's continue with the process.")
                print("-----------------------------------")
                print("Do you already have a storage file?")

                optionConFile = input("Type y/n (Yes or No): ").strip().lower()
                state4 = True

                while state4:
                    if optionConFile in ["y", "yes"] or activation:
                        print("Okay, let's find your file...")

                        # Load file or initialize data
                        if os.path.exists(filename):
                            with open(filename, "r") as file:
                                try:
                                    data = json.load(file)
                                except json.JSONDecodeError:
                                    data = {}
                        else:
                            data = {}

                        passId = input(f"The following password: {password}, corresponds to which Site or App? (This is to identify): ")
                        date = datetime.now().isoformat()

                        entry = {
                            "passID": passId,
                            "entryID": entry_id,
                            "password": password,
                            "date": date
                        }


                        data[label] = entry

                        # Save to file
                        with open(filename, "w") as file:
                            json.dump(data, file, indent=4)

                        print(f"Password saved successfully to '{filename}'.")
                        state4 = False

                    elif optionConFile in ["n", "no"]:
                        print("It's okay, we can create a new one from scratch.")
                        # Create empty file
                        with open(filename, "w") as file:
                            json.dump({}, file, indent=4)
                        print(f"Empty '{filename}' file created.")

                        # Activate flow to continue with saving
                        activation = True
                        optionConFile = "y"  # Force next loop to write

                    else:
                        print("Sorry, your response doesn't match any of our options. Try again.")
                        optionConFile = input("Type y/n (Yes or No): ").strip().lower()

                state3 = False  # Exit main loop

            elif optionConfirm in ["n", "no"]:
                print("Thanks for your response. No password will be stored.")
                state3 = False

            else:
                print("Something’s wrong with your answer... please type y/n to confirm.")
                optionConfirm = input("Type y/n (Yes or No): ").strip().lower()
    
if __name__ == "__main__":
    password_gen = GenPassword()

    password_gen.getKeyword()
    password_gen.getKeynumbers()

    generate_pwd = password_gen.generatePass()
    print(f"Generated Password: {generate_pwd}")

    label = input("Enter a label to identify this password (e.g., 'email', 'bank'): ")
    entry_id = input("Enter an ID for this password entry (or just press enter to skip): ") or "N/A"

    password_gen.getStorage(label=label, entry_id=entry_id, password=generate_pwd)



