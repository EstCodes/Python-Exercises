import random

class GenPassword:
    def __init__(self, keyword: str = "", keynumbers: int = 0):
        self.keyword = keyword
        self.keynumbers = keynumbers

    def getKeyword(self) -> None:
        print("To execute this program you should enter a keyword to remember the password")
        self.keyword = input("Type here: ")
        print(f"Keyword set to: {self.keyword}")

    def getKeynumbers(self) -> None:
        print("To execute this program you should enter a keynumber to remember the password")
        while True:
            try:
                self.keynumbers = int(input("Type here: "))
                print(f"Keynumber set to: {self.keynumbers}")
                break 
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

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
            
        symbols = ['#', '@', '!', '-', '_', '=', '+', ']', '[', '{', '}', '.', ',', '~', '$', '%', '&', ':', ';']
        selected_symbols = random.sample(symbols, 3)

        password.extend(selected_symbols)
        random.shuffle(password)

        if len(password) > 0:
            insert_index = random.choice(range(len(password) + 1))
            password.insert(insert_index, str(self.keynumbers))
        final_password = "".join(password)
        return final_password
    
if __name__ == "__main__":
    password_gen = GenPassword()

    password_gen.getKeyword()
    password_gen.getKeynumbers()

    generate_pwd = password_gen.generatePass()
    print(f"Generated Password: {generate_pwd}")




