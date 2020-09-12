from arena import arena

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    x = arena()

    #Build Teams
    x.build_team_one()
    x.build_team_two()
    while game_is_running:

        x.team_battle()
        x.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            x.team_one.revive_heroes()
            x.team_two.revive_heroes()
