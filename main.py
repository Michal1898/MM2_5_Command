# import black
game_options = {"ano": True, "ne": False, "yes": True, "no": False}
next_game = "ano"
code_values = [_ for _ in range(1, 9)]


class Attempt:
    def __init__(self, att_no, your_code=[], white=0, black=0 ):

        self.__index = att_no
        self.__your_code=your_code
        self.__black_stick = white
        self.__white_stick = black

    def __repr__(self):
        self.att_Report = ""
        self.att_Report+= f"{self.__index}. "
        self.att_Report+= f"{self.__your_code} "
        self.att_Report+= f"Black: {self.__black_stick} "
        self.att_Report+= f"White: {self.__white_stick} "
        self.att_Report+="\n"
        return self.att_Report

class MasterMind:
    def __init__(self, attempt=10, option=8, digit=5):
        import uuid
        from random import choices

        actual = ["running", "code_hacked", "time_left", "attempts_exhausted"]
        self.__attempt = attempt
        self.__option = option
        self.__digit = digit

        self.__game_id = str(uuid.uuid4())
        self.__possible_values = [_ for _ in range(1, self.__option + 1)]
        self.__secret_code = choices(self.__possible_values, k=self.__digit)
        self.__game_status = "running"
        self.__current_att = 0
        self.__game_active = True
        self.__code_hacked = False
        self.__all_values_OK = False
        self.__time_left = False
        self.__all_attempts_exhausted = False

        self.__attempts_pool = []

        print(f"Created new game with ID {self.__game_id}")
        print(f"Good luck")

    def show_secret(self):
        return f"Secret code is: {self.__secret_code} \n"

    def show_secret_list(self):
        return  self.__secret_code

    def list_of_values(self):
        return self.__possible_values

    def next_attempt(self, your_attempt ="0 0 0 0 0"):
        #self.__game_active=False
        #self.__current_att=10
        if self.__game_active == False:
            return False, "Game is not active!"

        elif self.__current_att<self.__attempt:
            #evaluate attempt
            your_attempt=list(map(int, your_attempt.split()))
            print(your_attempt)
            secret=self.show_secret_list()
            print(secret)
            digit_equal=[]
            attemp_rest=[]
            secret_rest=[]
            for _ in range (0, len(secret)):
                if secret[_] == your_attempt[_]:
                    digit_equal.append(your_attempt[_])
                else:
                    attemp_rest.append(your_attempt[_])
                    secret_rest.append(secret[_])
            black_stick=len(digit_equal)

            white_stick = 0
            wrong_position= True
            while wrong_position:
                wrong_position=False
                for digit in attemp_rest:
                    if digit in secret_rest:
                        attemp_rest.remove(digit)
                        secret_rest.remove(digit)
                        white_stick+=1
                        wrong_position= True
                        break



            the_attempt=Attempt(self.__current_att, your_attempt, black_stick , white_stick)
            self.__current_att+=1
            self.__attempts_pool.append(the_attempt)
            return True, the_attempt


        else:
            return False, "You have not attempt available!"
            # this case can't occur in fact.
            # but better save than sorry.

    def __repr__(self):
        MM_Report = ""
        MM_Report += " * L O G I C * \n"
        MM_Report += f"Game ID: {self.__game_id} \n"
        MM_Report += f" Number of attempts: {self.__attempt} \n"
        MM_Report += f" Number of digits in quesed code: {self.__digit} \n"
        MM_Report += (
            f" The digit has one of the values : \n {self.__possible_values} \n"
        )
        MM_Report += "Digit values can be repeated. \n"
        MM_Report += "Only for tests! Remove, when completed!"
        MM_Report += self.show_secret()
        MM_Report += " Game flags: \n"
        MM_Report += f" Game status: {self.__game_status} \n"
        if self.__game_active:
            MM_Report += "You are in the game. \n"

            if self.__all_values_OK:
                MM_Report += (
                    "You just guessed all the numbers. You are close to the goal! \n"
                )
            else:
                MM_Report += "Keep on! \n"
        else:
            MM_Report += "Game is over! \n"

            if self.__code_hacked:
                MM_Report += "You hacked the secret! I congratulate you! \n"
            elif self.__all_values_OK:
                MM_Report += "You guessed all the numbers. Unfortunately, the sequence is wrong! \n"
            else:
                MM_Report += "You are looser!"

        # print(MM_Report)
        return MM_Report



game_commands = [
    "new_game",
    "game_status",
    "print_game",
    "quess_code",
    "resign",
    "resign2",
    "help",
]
current_game = ""
# while current_game not in game_commands:
#    current_game = str.lower(input("Co chces delat dale? "))
current_game = "new_game"
match current_game:
    case "new_game":
        # the_game = MasterMind()
        # the_game.show_secret()
        # print(the_game.list_of_values())

        the_game = MasterMind()
        # the_game.show_secret()
        # print(the_game.list_of_values())
        # print(repr(the_game))

        for _ in range(0,100):
            single_attempt=the_game.next_attempt("3 4 5 6 8")
            print([single_attempt])


        the_attempt = Attempt(13, [1 ,2 ,3 ,8 ,111], 19, 7)
        print(the_attempt)
        # the_attempt2 = Attempt("7 7 7 13 13 13", 17)
        # the_game = MasterMind(7,10,4)
        # the_game.show_secret()
        # print(the_game.list_of_values())
        # print(repr(the_game))

    case "game_status":
        pass
    case "print_game":
        pass
    case "quess_code":
        pass
    case "resign":
        pass
    case "resign2":
        pass
    case "help":
        pass

print(current_game)

# quit game?
#next_game = str.lower((input("Dalsi kolo? (Ano/Ne) ")))
#print(next_game)


print("Game over!")
