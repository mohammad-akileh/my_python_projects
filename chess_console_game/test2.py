from Project_content import *
from rich.console import Console
from rich.rule import Rule
c=Console()
c.print("We will start the chess game with 2 Players \nEach player should choose (cell from,cell to) for example(a2,a3)\nLet's Start :=)\n")
#fill the board and print it to start the game
first_board()
printer()
#Start the 2-players game and give each player his turn
def game_start():
        player1=True
        while True:
            if player1:
                player_info = input_checker(player_flag)
                print(player_info)
                print("the player is P1 ",player1)
                result=move_agreement(player_info)
                if result =="CHECK" and player1:
                        c.print("WARNING PLAYER 1 CHECK MATE!!!", style="bold red")
                        continue
                elif result =="CHECK" and not player1:
                    c.print("WARNING PLAYER 2 CHECK MATE!!!", style="bold red")
                    continue
                elif result == False:
                    continue
                elif result==True:    
                    player1=False
                
        
        
game_start()    
print("backuped yes its")
