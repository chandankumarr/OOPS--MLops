class chatbot:

    __userid = 0

    def __init__(self):
        self.__name = 'sungjinwo'
        self.id = chatbot.__userid
        chatbot.__userid += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()

    def get_id():
        return chatbot.__userid
    
    def set_id(value):
        chatbot.__userid = value



    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to chatbot! how would you like to proceed?"
        1. press 1 to signup -->
        2. press 2 to signin -->
        3. press 3 to write a post -->
        4. press 4 to message a friend
        5. press any other key to exit
        
        -->""")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("please enter your email here -->")
        pwd = input("please enter your pwd here -->")
        self.username = email
        self.password = pwd
        print("you have signedup successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("ENter your password here -> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()
        
    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -->")
            print(f"following content has been posted --> {txt}")
        else:
            print("you need to sign in first to post something..")
        print("\n")
        self.menu()


    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -->")
            frnd = input("whom to send the message? -->")
            print(f"your message has been sent to {frnd}")
        else:
            print("you need to sign in first to post something..")
        print("\n")
        self.menu()

user1 = chatbot()
        