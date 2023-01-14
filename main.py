import datetime

game_options = {"ano": True, "ne": False, "yes": True, "no": False}


class CustomException(Exception):
    pass


class Attempt:
    def __init__(
        self, att_no, your_code=[], white=0, black=0, duration=datetime.time(0)
    ):

        self.__index = att_no
        self.__your_code = your_code
        self.__black_stick = white
        self.__white_stick = black
        self.__attempt_time = duration

    def __repr__(self):
        self.att_Report = ""
        self.att_Report += f"{self.__index + 1}. "
        self.att_Report += f"{self.__your_code} "
        self.att_Report += f"Black: {self.__black_stick} "
        self.att_Report += f"White: {self.__white_stick} "
        self.att_Report += f"Time: {self.__attempt_time} "
        self.att_Report += "\n"
        return self.att_Report


class MasterMind:
    # Set time limit for the game
    # h ... hours
    # m ... minutes
    # s ... seconds
    def set_time_for_game(self, h=1, m=3, s=59):
        # in this case is time set for:
        # 1 hour,
        # 3 minutes
        # and 59 seconds
        self.__TIME_FOR_GAME = datetime.timedelta(days=0, hours=h, minutes=m, seconds=s)
        return True, self.__TIME_FOR_GAME

    def return_time_for_game(self):
        return self.__TIME_FOR_GAME

    def game_start(self):
        start_time = self.__date_of_the_game.time()
        return start_time

    def game_date(self):
        game_date = self.__date_of_the_game.date()
        return game_date

    def game_duration(self):
        game_duration = datetime.datetime.now() - self.__start_time
        return game_duration

    # this Dictionary return limits for:
    # - no of attempts
    # - no of digits
    # - possible values counts
    def limits(self, limit_name=" "):
        self.__the_outer_limits = {
            "ATTEMPT_MIN": 2,
            "ATTEMPT_MAX": 50,
            "DIGIT_MIN": 1,
            "DIGIT_MAX": 10,
            "VALUES_MIN": 2,
            "VALUES_MAX": 16,
        }
        limit_value = self.__the_outer_limits.get(limit_name, False)
        return limit_value

    def return_outer_limits(self):
        outer_limits = ""
        outer_limits += "All limits must be integers! \n"
        outer_limits += "All limits must be positive! \n"
        outer_limits += f"Count of attempts must be in range: {self.limits('ATTEMPT_MIN')} - {self.limits('ATTEMPT_MAX')}.\n"
        outer_limits += f"Count of digits must be in range: {self.limits('DIGIT_MIN')} - {self.limits('DIGIT_MAX')}. \n"
        outer_limits += f"Values for each digit must be in range: {self.limits('VALUES_MIN')} - {self.limits('VALUES_MAX')}.\n"
        return outer_limits

    def check_time_to_left(self):
        if self.__game_active:
            if self.game_duration() > self.return_time_for_game():
                print("You exceeded time limit for game!")
                self.__game_active = False
                self.__game_status = "time_exceeded"
                self.__time_left = True
        return self.__time_left

    def return_rest_time(self):
        rest_time = self.return_time_for_game() - self.game_duration()
        if rest_time.days < 0:
            return datetime.timedelta(seconds=0)
        else:
            return rest_time

    def __init__(self, attempt=10, option=8, digit=5):
        import uuid
        from random import choices

        self.__game_status = "parameter_checking"
        self.__game_active = False

        print("Test of the input parameters \n")
        # check, if all parameter of the class are in allowed limits.
        error_message = False
        if (
            isinstance(attempt, int)
            and isinstance(option, int)
            and isinstance(digit, int)
        ):
            if attempt < self.limits("ATTEMPT_MIN") or attempt > self.limits(
                "ATTEMPT_MAX"
            ):
                error_message = "Count of attempts out of range!"

            elif option < self.limits("VALUES_MIN") or option > self.limits(
                "VALUES_MAX"
            ):
                error_message = "Count of options out of range!"
            elif digit < self.limits("DIGIT_MIN") or digit > self.limits("DIGIT_MAX"):
                error_message = "Count of digits out of range!"
        else:
            error_message = "Parameters must be integer!"

        if error_message:
            print(self.return_outer_limits())
            raise CustomException(error_message)
            return error_message

        print("Parameters are OK. I start the game. \n")
        self.__attempt = attempt
        self.__option = option
        self.__digit = digit

        self.__game_id = str(uuid.uuid4())
        print(f"Created new game with ID {self.__game_id}")
        print("I generate the secret code. ")
        self.__possible_values = [_ for _ in range(1, self.__option + 1)]
        self.__secret_code = choices(self.__possible_values, k=self.__digit)
        print("Secret Code was generated.")
        self.__game_status = "game_running"
        self.__current_att = 0
        self.__game_active = True
        self.__code_hacked = False
        self.__all_values_OK = False
        self.__time_left = False
        self.__all_attempts_exhausted = False

        self.__attempts_pool = []

        self.set_time_for_game(1, 0, 0)
        self.__date_of_the_game = datetime.datetime.now()
        self.__start_time = datetime.datetime.now()
        self.__temp_time = self.__start_time
        print(f"Good luck")

    def show_secret(self):
        return f"Secret code is: {self.__secret_code} \n"

    def show_secret_list(self):
        return self.__secret_code

    def list_of_values(self):
        return self.__possible_values

    def is_running(self):
        return self.__game_active

    def game_status(self):
        return self.__game_status

    def active_attempt(self):
        return self.__current_att

    def rest_attempt(self):
        rest = self.__attempt - self.__current_att
        return rest

    def attempt_pool(self):
        return self.__attempts_pool

    def next_attempt(self, your_attempt="0 0 0 0 0"):
        self.check_time_to_left()
        if self.__game_active == False:
            return False, "Game is not active!"

        elif self.__current_att < self.__attempt:
            # evaluate attempt
            attemp_time = datetime.datetime.now() - self.__temp_time
            self.__temp_time = datetime.datetime.now()

            # check if valid code was inserted
            attempt_error = False
            secret = self.show_secret_list()
            your_attempt = your_attempt.split()
            if len(your_attempt) != len(secret):
                attempt_error = "Wrong number of digits!"
            else:
                for digit in your_attempt:
                    if digit.isdigit():
                        digit = int(digit)
                        if digit not in self.list_of_values():
                            attempt_error = "Value out of range!"
                            break

                    else:
                        attempt_error = "Digit must be positive integer!"
                        break

            if attempt_error:
                return False, attempt_error
            else:
                # inserted ccode is valid
                your_attempt = list(map(int, your_attempt))
                digit_equal = []
                attemp_rest = []
                secret_rest = []
                for _ in range(0, len(secret)):
                    if secret[_] == your_attempt[_]:
                        digit_equal.append(your_attempt[_])
                    else:
                        attemp_rest.append(your_attempt[_])
                        secret_rest.append(secret[_])
                black_stick = len(digit_equal)

                white_stick = 0
                wrong_position = True
                while wrong_position:
                    wrong_position = False
                    for digit in attemp_rest:
                        if digit in secret_rest:
                            attemp_rest.remove(digit)
                            secret_rest.remove(digit)
                            white_stick += 1
                            wrong_position = True
                            break

                the_attempt = Attempt(
                    self.__current_att,
                    your_attempt,
                    black_stick,
                    white_stick,
                    attemp_time,
                )
                self.__current_att += 1
                self.__attempts_pool.append(the_attempt)

                # Update status of the current game
                if white_stick + black_stick == len(secret):
                    self.__all_values_OK = True
                    print("Congratulate, you quessed all Values!")

                if black_stick == len(secret):
                    print("Congratulate, you hacked the secret!")
                    self.__code_hacked = True
                    self.__game_active = False
                    self.__game_status = "code_hacked"

                if len(self.__attempts_pool) < self.__attempt:
                    pass
                elif len(self.__attempts_pool) == self.__attempt:
                    self.__game_active = False
                    if self.__code_hacked == False:
                        print("not hacked")
                        self.__game_status = "attempts_exhausted"
                else:
                    # this case can't occur,
                    # but better safe than sorry!
                    print("Critical Error!")

                return True, the_attempt

        else:
            # this case can't occur in fact.
            # but better safe than sorry.
            return False, "You have not attempt available!"

    def __repr__(self):
        self.check_time_to_left()
        MM_Report = ""
        MM_Report += " *************\n"
        MM_Report += " * L O G I C * \n"
        MM_Report += " *************\n"
        MM_Report += f"Game ID: {self.__game_id} \n"
        MM_Report += f"Date: {self.game_date()} \n"
        MM_Report += f"Game started at: {self.game_start() } \n"
        MM_Report += f" Number of attempts: {self.__attempt} \n"
        MM_Report += f" Number of digits in quesed code: {self.__digit} \n"
        MM_Report += (
            f" The digit has one of the values : \n {self.__possible_values} \n"
        )
        MM_Report += "Digit values can be repeated. \n"
        if self.is_running() == False:
            MM_Report += 40 * "*" + "\n"
            MM_Report += self.show_secret()
        MM_Report += 40 * "*" + "\n"

        MM_Report += "Attempts pool:\n"
        MM_Report += "***************************\n"

        if len(self.attempt_pool()):
            for single_attempt in self.__attempts_pool:
                MM_Report += repr(single_attempt)
        else:
            MM_Report += "****** Pool is empty ******\n"
        MM_Report += "***************************\n"
        MM_Report += "\n"
        MM_Report += f"Active attempt number: {self.active_attempt() + 1} \n"
        MM_Report += f"Used attempts: {len(self.__attempts_pool)} \n"
        MM_Report += f"Rest attempts: {self.rest_attempt()} \n \n"

        MM_Report += f"Time for play: {self.return_time_for_game()} \n"
        MM_Report += f"Time left: {self.game_duration() } \n"
        MM_Report += f"Time rest: {self.return_rest_time() } \n"
        MM_Report += "\n"
        MM_Report += "  Game flags:  \n"
        MM_Report += "**************\n"
        MM_Report += f" Game status: {self.__game_status} \n"
        if self.__game_active:
            MM_Report += " You are in the game. \n"

            if self.__all_values_OK:
                MM_Report += (
                    " You just guessed all the numbers. You are close to the goal! \n"
                )
            else:
                MM_Report += " Keep on! \n"
        else:
            MM_Report += " Game is over! \n"

            if self.__time_left:
                MM_Report += " You exceeded time limit! \n"

            if self.__code_hacked:
                MM_Report += "You hacked the secret! I congratulate you! \n"
            elif self.__all_values_OK:
                MM_Report += "You guessed all the numbers. Unfortunately, the sequence is wrong! \n"
            else:
                MM_Report += "You are looser! \n"

        return MM_Report


the_game = MasterMind(10, 8, 5)

print(repr(the_game))
while the_game.is_running():
    quess_code = input("Insert your code: ")
    attempt_inserted = False
    while attempt_inserted == False:
        attempt_inserted = the_game.next_attempt(quess_code)
        print(attempt_inserted)
    print(repr(the_game))
    # print(the_game.attempt_pool())
print("Final report:")
print(repr(the_game))

# Save game to the file:
print("I will save finished game to the file.")
with open("data/mm_games.txt", "a") as f:
    f.write("Final report: \n")
    f.write(repr(the_game))
    f.write("-" * 50)
    f.write("\n")
print("Game was saved.")


print("Game over!")
