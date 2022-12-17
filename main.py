# import black
game_options = {"ano": True, "ne": False, "yes": True, "no": False}
next_game = "ano"
code_values = [_ for _ in range(1, 9)]


class MasterMind:
    def __init__(self, attempt=10, option=8, digit=5):
        import uuid
        from random import choices

        actual = ["running", "code_hacked", "time_left", "attempts_exhausted"]
        self.__attempt = attempt
        self.__option = option
        self.__digit = digit

        self.game_id = str(uuid.uuid4())
        self.__possible_values = [_ for _ in range(1, self.__option + 1)]
        self.__secret_code = choices(self.__possible_values , k = self.__digit)
        self.__game_status = "running"
        self.__current_att = 0
        self.__game_active = True
        self.__code_hacked = False
        self.__time_left = False
        self.__attempts_exhausted = False
        print(f"Created new game with ID {self.game_id}")
        print(f"Good luck")

    def show_secret(self):
        print(f"Secret code is: {self.__secret_code}")

    def list_of_values(self):
        return self.__possible_values

while game_options.get(next_game, True):
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
    while current_game not in game_commands:
        current_game = str.lower(input("Co chces delat dale? "))
    match current_game:
        case "new_game":
            the_game = MasterMind()
            the_game.show_secret()
            print(the_game.list_of_values())

            the_game = MasterMind(13,4,12)
            the_game.show_secret()
            print(the_game.list_of_values())

            the_game = MasterMind(7,10,4)
            the_game.show_secret()
            print(the_game.list_of_values())

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
    next_game = str.lower((input("Dalsi kolo? (Ano/Ne)")))
    print(next_game)

print("Game over!")
