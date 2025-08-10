while True : 
    class Player : 
        def __init__ (self , player ) : 
            self.player = player
            self.choice = self.choice()

        def choice (self) :
            choices = ["Sang" , "Kaghaz" , "Gheychi" ]
            while True :
                player_input = input (f"{self.player} enter your choice :").title()
            
                if player_input in choices :
                    return player_input 
                else : 
                    print ("Invalid choice , please enter sang or kaghaz or gheychi :")


    class Game : 
        def __init__ (self , player1 , player2) : 
            self.P1 = player1
            self.P2 = player2 

        def Win (self) : 
            choice_player1 = self.P1.choice
            choice_player2 = self.P2.choice


            if choice_player1 == choice_player2 :
                print("It's a tie :D")

            elif (choice_player1 == "sang" and choice_player2 == "gheychi") or \
                (choice_player1 == "kaghaz" and choice_player2 == "sang") or \
                (choice_player1 == "gheychi" and choice_player2 == "kaghaz") : 
                print(f"{self.P1.player} is win :D ")

            else : 
                print(f"{self.P2.player} is Win :D")
    

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    game = Game(player1, player2)
    game.Win()

    again = input ("Do you still want to continue? 1 : yes , 0 : no :" )

    if  again == "0" :
        print("Bye Bye.")
        break