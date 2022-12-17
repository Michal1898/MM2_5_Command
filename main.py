import uuid
#import black
game_options={'ano': True, 'ne': False, 'yes': True, 'no': False}
next_game = "ano"
code_values=[_ for _ in range(1,9)]
while (game_options.get(next_game, True)):
    game_commands=["new_game", "game_status", "print_game", "quess_code", "resign", "resign2", "help" ]
    current_game=""
    while current_game not in game_commands:
        current_game=str.lower(input("Co chces delat dale?"))
    match current_game:
        case "new_game":
            pass
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
    next_game=str.lower((input("Dalsi kolo? (Ano/Ne)")))
    print(next_game)

print("Game over!")