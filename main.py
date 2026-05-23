from pathlib import Path
import random

#path = Path(r"")
name = "Fake_News_Paper.txt"
#p = path / name

path = Path.cwd()
p = path / name

print("Wel-Come to Fake News Genration!")

class Fake_News:

    def politics_list(selt):
        names = ['Rahul Gandhi ', 'Aakhilesh Yadav ', 'Narendra Modi ', 'Mamta Banarji ']
        actions = ['loosing election ', 'becoming PM ', 'winning election ', 'becoming CM ']
        places = ['for USA', 'for UK','for china','for UAE']

        name = random.choice(names)
        action = random.choice(actions)
        place = random.choice(places)
        
        return name, action, place


    def sports_list(selt):
        names = ['Sachin Tendulkar ', 'Vishwanath Aanand ', 'Sania Mirza ', 'Niraj Thakur ']
        actions = ['playing cricket ', 'playing chess ', 'playing badminton  ', 'playing karate ']
        places = ['for Bangladesh', 'for Austrelia','for United States','for Saudi Arebia']

        name = random.choice(names)
        action = random.choice(actions)
        place = random.choice(places)
        
        return name, action, place


    def enter_list(selt):
        names = ['James Bond ', 'Brad Pitt ', 'Sharukh Khan ', 'Jacky Chain ']
        actions = ['acting ', 'dancing ', 'performing comedy ', 'performing advanture acts ']
        places = ['in Bollywood', 'in Hollywood','in Korian Drama','in auditerioum']

        name = random.choice(names)
        action = random.choice(actions)
        place = random.choice(places)
        
        return name, action, place


    def science_list(selt):
        names = ['Albert Einstein ', 'Isaac Newton ', 'Niels Bohr ', 'Galileo Galilei ']
        actions = ['discovered ', 'invented ', 'formulated ', 'groundbreaking integration ']
        places = ['laws of motion and universal gravitation', 'ftheories of relativity','pioneering the experimental method','quantum theory']

        name = random.choice(names)
        action = random.choice(actions)
        place = random.choice(places)
        
        return name, action, place


    def concatinate(self, name, action, place):
        #sentence = name + action + place
        sentence = name + " " + action + " " + place
        print(sentence)
        self.save_file(sentence)


    def save_file(self,sentence):
        with open(p,'a') as fs:
            fs.write(sentence + "\n")
            print(f"FILE CREATED SUCCESSFULLY")

    def politics(self):
        print("Press 1 if you want to choose your own option for Fake news like name, action and place")
        print("Press 2 if you want to choose option from list")
        check = int(input("Enter your option: "))
        if check == 1:
            own_name = input("Please enter your own name but it should be related to politics: ")
            own_action = input("Please enter your own action but it should be related to politics: ")
            own_place = input("Please enter your own place but it should be related to politics: ")
            self.concatinate(own_name,own_action,own_place)
        if check == 2:
            name, action, place = self.politics_list()
            self.concatinate(name,action,place)

    def sports(self):
        print("Press 1 if you want to choose your own option for Fake news like name, action and place")
        print("Press 2 if you want to choose option from list")
        check = int(input("Enter your option: "))
        if check == 1:
            own_name = input("Please enter your own name but it should be related to sports: ")
            own_action = input("Please enter your own action but it should be related to sports: ")
            own_place = input("Please enter your own place but it should be related to sports: ")
            self.concatinate(own_name,own_action,own_place)
        if check == 2:
            name, action, place = self.sports_list()
            self.concatinate(name,action,place)


    def enter(self):
        print("Press 1 if you want to choose your own option for Fake news like name, action and place")
        print("Press 2 if you want to choose option from list")
        check = int(input("Enter your option: "))
        if check == 1:
            own_name = input("Please enter your own name but it should be related to entertainment: ")
            own_action = input("Please enter your own action but it should be related to ertainment: ")
            own_place = input("Please enter your own place but it should be related to entertainment: ")
            self.concatinate(own_name,own_action,own_place)
        if check == 2:
            name, action, place = self.enter_list()
            self.concatinate(name,action,place)


    def science(self):
        print("Press 1 if you want to choose your own option for Fake news like name, action and place")
        print("Press 2 if you want to choose option from list")
        check = int(input("Enter your option: "))
        if check == 1:
            own_name = input("Please enter your own name but it should be related to science: ")
            own_action = input("Please enter your own action but it should be related to science: ")
            own_place = input("Please enter your own place but it should be related to science: ")
            self.concatinate(own_name,own_action,own_place)
        if check == 2:
            name, action, place = self.science_list()
            self.concatinate(name,action,place)


while True:
    choice = input("Do you want genrate Fake news (Y/N): ")
    if choice  == 'y' or choice == 'Y':
        News = Fake_News()
        print("Press 1 for Politics")
        print("Press 2 for Sports")
        print("Press 3 for Entertaintment")
        print("Press 4 for Science")

        check = int(input("Select you option in between 1 to 4: "))

        if check == 1:
            News.politics()

        if check == 2:
            News.sports()

        if check == 3:
            News.enter()

        if check == 4:
            News.science()

        True
    
    elif choice == 'n' or choice == 'N':
        print("Its funny, have you emjoyed?")
        break

    else:
        print("You entered wrong input")
        break



