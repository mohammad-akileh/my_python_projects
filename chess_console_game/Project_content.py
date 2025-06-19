from rich.console import Console
from rich.rule import Rule
c = Console()
# Chess elements’ names
pieces = {
     "pawn": "⚔️","rook": "🏰", "knight": "🐴", "bishop": "👼", "king": "🤴"
    ,"queen": "👑"
}
p1_pushed_list=["    "]*16
p2_pushed_list=["    "]*16

#Implement 2 collections for the 2 Players with P1 and P2 before the piece name
p1_pieces=["P1"+pieces["pawn"]+" "]*8 +["P1"+e for e in tuple(pieces.values())[1:len(pieces.values())]]+["P1"+e for e in tuple(pieces.values())[3:0:-1]]
p2_pieces=["P2"+pieces["pawn"]+" "]*8 +["P2"+e for e in tuple(pieces.values())[1:len(pieces.values())]]+["P2"+e for e in tuple(pieces.values())[3:0:-1]]
#Implement the board
board = {x :{8:"    ",7:"    ",6:"    ",5:"    ",4:"    ",3:"    ",2:"    ",1:"    "} for x in'abcdefgh'}
# move the pieces 
def move(l1,l2):
    key_from=l1[0]
    value_from = int(l1[1])
    key_to=l2[0]
    value_to = int(l2[1])
    board[key_to][value_to]=board[key_from][value_from]
    board[key_from][value_from]="    " 
#check that the move player want to is allowed
def move_agreement(player_info):
    #P1 f2 g5
    global p1_pushed_list
    global p2_pushed_list
    global board
    player=player_info[0]
    move_from=player_info[1]
    move_to=player_info[2]
    #check that the move is not for a cell with piece for the same player or for the same cell
    if board[move_to[0]][int(move_to[1])].startswith(player) or (move_from==move_to) or (board[move_from[0]][int(move_from[1])].startswith(player)!=True):
        return False
    player_board=players_boards()
    p1_check=False
    p2_check=False
    if player=="P1":
        p1_list_all=[]
        p2_list_all=[]
        for i in player_board["P2"]:
            p2_list_all=p2_list_all+available_cells("P2",i)
        if "🤴" in board[move_from[0]][int(move_from[1])]:
            if move_to in p2_list_all:
                return False    
            else:
                p1_pushed_list[p1_pushed_list.index("    ")]=board[move_to[0]][int(move_to[1])]
                move(move_from,move_to) 
                printer()
                p1_check==False
                return True              
        for i in player_board["P1"]:
            p1_list_all=p1_list_all+available_cells("P1",i)     
        king2_cells=available_cells("P2",king_finder()["P2"])
        if king_2_cells:
            pass
        elif all(item in p1_list_all for item in available_cells("P2",king_finder()["P2"])) :
            c.print( "Player 1 Won !",style="bold red")  
            exit(0)        
        if move_to in available_cells(player,move_from):
          if "🤴" in board[move_from[0]][int(move_from[1])]:
            if move_to not in p2_list_all:
                p1_pushed_list[p1_pushed_list.index("    ")]=board[move_to[0]][int(move_to[1])]
                move(move_from,move_to)
                printer()
                return True 
          occurrences = p2_list_all.count(king_finder()["P1"]) 
          if occurrences>0:
            p1_check=True
          if occurrences==1 :
            for i in player_board["P2"]:
                movements = available_cells("P2",i)
                if (king_finder()["P1"] in movements) and (move_to ==i):
                    p1_check=False
                    break
          if not p1_check:
            #print("available cells are",available_cells("P1",move_from)) 
            ind=p1_pushed_list.index("    ")
            p1_pushed_list[ind]=board[move_to[0]][int(move_to[1])]
            move(move_from,move_to)
            player_board=players_boards()
            all_cells=[]
            for i in player_board["P2"]:
                all_cells=all_cells+available_cells("P2",i)
            if king_finder()["P1"] in all_cells:
                move(move_to,move_from)
                p1_pushed_list[ind]="    "
                return False   
          else:
            return "CHECK"  
          printer() 
          pawn_end_checker() 
          return True   
        else :
            return False   

    else :#player 2
        p1_list_all=[]
        p2_list_all=[]
        for i in player_board["P1"]:
            p1_list_all=p1_list_all+available_cells("P1",i)
            #print("available cells for ",i,"are ",available_cells("P1",i))
        if "🤴" in board[move_from[0]][int(move_from[1])]:
            if move_to in p1_list_all:
                return False 
            else: 
                p2_pushed_list[p2_pushed_list.index("    ")]=board[move_to[0]][int(move_to[1])]
                move(move_from,move_to)
                printer()
                p2_check==False
                return True      
        for i in player_board["P2"]:
            p2_list_all=p2_list_all+available_cells("P2",i)     
        king1_cells=available_cells("P1",king_finder()["P1"])
        if king_2_cells:
            pass
        elif all(item in p2_list_all for item in available_cells("P1",king_finder()["P1"])) :
            c.print( "Player 2 Won !",style="bold red")  
            exit(0)        
        if move_to in available_cells(player,move_from):

          if "🤴" in board[move_from[0]][int(move_from[1])]:
            if move_to not in p1_list_all:
                p2_pushed_list[p2_pushed_list.index("    ")]=board[move_to[0]][int(move_to[1])]
                move(move_from,move_to)
                printer()
                return True  
          occurrences = p1_list_all.count(king_finder()["P2"]) 
          if occurrences>0:
            p2_check=True
          if occurrences==1 :
            for i in player_board["P1"]:
                movements = available_cells("P1",i)
                if (king_finder()["P2"] in movements) and (move_to ==i):
                    p2_check=False
                    break
          if not p2_check:   
            ind=p2_pushed_list.index("    ")
            p2_pushed_list[ind]=board[move_to[0]][int(move_to[1])]
            move(move_from,move_to)
            player_board=players_boards()
            all_cells=[]
            for i in player_board["P1"]:
                all_cells=all_cells+available_cells("P1",i)
            if king_finder()["P2"] in all_cells:
                move(move_to,move_from)
                p2_pushed_list[ind]="    "
                return False    
          else:
            return "CHECK"
          printer()  
          pawn_end_checker() 
          return True   
        else :
            return False    
   

    
            

#a method to check if the pawn reached the last cell near to the enemy
def pawn_end_checker():
    for i in ["a","b","c","d","e","f","g","h"]:
        if "⚔️" in board[i][8] or "⚔️" in board[i][1]:
            while True :
                change = input("What whould you like to change ⚔️ with 1.🏰 2.🐴 3.👼 4.👑\nchoose 1 2 3 4 -> ")
                if change not in ["1","2","3","4"]:
                    c.print("Wrong Input!")
                    continue
                else:
                    if int(change)==1 and "⚔️" in board[i][8] :
                        board[i][8]="P1🏰"
                        break
                    elif int(change)==1 and "⚔️" in board[i][1] :
                         board[i][1]="P2🏰"
                         break
                    elif int(change)==2 and "⚔️" in board[i][8] :
                         board[i][8]="P1🐴"
                         break
                    elif int(change)==2 and "⚔️" in board[i][1] :
                         board[i][1]="P2🐴"
                         break  
                    elif int(change)==3 and "⚔️" in board[i][8] :
                        board[i][8]="P1👼"
                        break
                    elif int(change)==3 and "⚔️" in board[i][1] :
                         board[i][1]="P2👼"
                         break
                    elif int(change)==4 and "⚔️" in board[i][8] :
                         board[i][8]="P1👑"
                         break
                    elif int(change)==4 and "⚔️" in board[i][1] :
                         board[i][1]="P2👑"
                         break     
            printer()                        
#a method returns dictionary of the (cells with P1 pieces,cells with P2 pieces,cells with p1 and p2 pieces) .
def players_boards():
    p1_board=[]
    p2_board=[]
    p_board=[]
    for i in "abcdefgh":
        for j in range(1,9):
            if "P1" in board[i][j]:
                p1_board.append(f"{i}{j}")
                p_board.append(f"{i}{j}")
            elif "P2" in board[i][j]:
                p2_board.append(f"{i}{j}")  
                p_board.append(f"{i}{j}") 
    return {"P1":p1_board,"P2":p2_board,"ALL":p_board}         
#a method returns all the available moves for each piece and for all pieces
king_1_cells=False
king_2_cells=False
def available_cells(player,move_from):
    global king_1_cells
    global king_2_cells
    move_from_l=move_from[0]
    move_from_n=int(move_from[1])
    piece=board[move_from[0]][int(move_from[1])]
    allowed_movements=[]
    if player=="P1":
        if "⚔️" in piece:
            if "P" not in board[move_from_l][move_from_n+1]:
                allowed_movements.append(move_from_l+str(move_from_n+1))
            if move_from_l=="a" and "P2" in board[chr(ord(move_from_l)+1)][move_from_n+1]:
                allowed_movements.append(chr(ord(move_from_l)+1)+str(move_from_n+1))
            if move_from_l=="h" and "P2" in board[chr(ord(move_from_l)-1)][move_from_n+1]:
                allowed_movements.append(chr(ord(move_from_l)-1)+str(move_from_n+1)) 
            if move_from_l!="h" and move_from_l!="a":
                if  "P2" in board[chr(ord(move_from_l)+1)][move_from_n+1]:
                    allowed_movements.append(chr(ord(move_from_l)+1)+str(move_from_n+1))
                if  "P2" in board[chr(ord(move_from_l)-1)][move_from_n+1]:
                    allowed_movements.append(chr(ord(move_from_l)-1)+str(move_from_n+1))
            if (move_from_n==2 ) and ("P" not in board[move_from_l][move_from_n+2]) :
                allowed_movements.append(move_from_l+str(move_from_n+2))   
        elif "🏰" in piece:
            for i in range(move_from_n+1,9):
                if "P1" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            for i in range(move_from_n-1,0,-1):
                if "P1" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            #h=104,a=97 
            for i in range(ord(move_from_l)+1,105):
                if "P1" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:
                    break
            for i in range(ord(move_from_l)-1,96,-1):
                if "P1" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:  
                    break      
        elif "🐴" in piece:
            moves=[]
            moves.append(chr(ord(move_from_l)+2)+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)+2)+str(move_from_n+1))
            moves.append(chr(ord(move_from_l)-2)+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)-2)+str(move_from_n+1))
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n-2))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n-2))
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n+2))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n+2))
            for i in moves:
                if len(i)==2:
                    if i[0] in "abcdefgh" and i[1] in "12345678":
                        if "P1" not in board[i[0]][int(i[1])]:
                            allowed_movements.append(i[0]+i[1])
        elif "👼" in piece:
            f_counter=ord(move_from_l)+1
            s_counter=ord(move_from_l)-1
            for i in range(move_from_n+1,9):
                if f_counter<=104:
                    if ("P1" not in board[chr(f_counter)][i]):
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter+=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter>=97:
                    if "P1" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter-=1
                    else:
                        break  
            f_counter=ord(move_from_l)-1
            s_counter=ord(move_from_l)+1
            for i in range(move_from_n+1,9):
                if f_counter>=97:
                    if "P1" not in board[chr(f_counter)][i]:
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter-=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter<=104:
                    if "P1" not in board[chr(s_counter)][i]and (s_counter<=104):
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter+=1
                    else:
                        break               
        elif "👑" in piece:
            for i in range(move_from_n+1,9):
                
                if "P1" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            for i in range(move_from_n-1,0,-1):
                if "P1" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            for i in range(ord(move_from_l)+1,105):
                if "P1" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:
                    break
            for i in range(ord(move_from_l)-1,96,-1):
                if "P1" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:  
                    break
            #👼    
            f_counter=ord(move_from_l)+1
            s_counter=ord(move_from_l)-1
            for i in range(move_from_n+1,9):#
                if f_counter<=104:
                    if ("P1" not in board[chr(f_counter)][i]):
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter+=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter>=97:
                    if "P1" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter-=1
                    else:
                        break  
            f_counter=ord(move_from_l)-1
            s_counter=ord(move_from_l)+1
            for i in range(move_from_n+1,9):
                if f_counter>=97:
                    if "P1" not in board[chr(f_counter)][i]:
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter-=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter<=104:
                    if "P1" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter+=1
                    else:
                        break     
        elif "🤴" in piece:
            moves=[]
            moves.append(move_from_l+str(move_from_n+1))
            moves.append(move_from_l+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n))#4
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n+1))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n+1))#
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n-1))
            for i in moves:
                if i[0] in "abcdefgh" and i[1] in "12345678":
                    if "P1" not in board[i[0]][int(i[1])]:
                        allowed_movements.append(i[0]+i[1])  
            if len(allowed_movements)==0:
                king_1_cells=True

    else:#player =2
        if "⚔️" in piece:
            if "P" not in board[move_from[0]][int(move_from[1])-1]:
                allowed_movements.append(move_from[0]+str(int(move_from[1])-1))
            if move_from[0]=="a" and "P1" in board[chr(ord(move_from[0])+1)][int(move_from[1])-1]:
                allowed_movements.append(chr(ord(move_from[0])+1)+str(int(move_from[1])-1))
            if move_from[0]=="h" and "P1" in board[chr(ord(move_from[0])-1)][int(move_from[1])-1]:
                allowed_movements.append(chr(ord(move_from[0])-1)+str(int(move_from[1])-1)) 
            if move_from[0]!="a" and move_from[0]!="h":
                if  "P1" in board[chr(ord(move_from[0])-1)][int(move_from[1])-1]:
                    allowed_movements.append(chr(ord(move_from[0])-1)+str(int(move_from[1])-1))
                if  "P1" in board[chr(ord(move_from[0])+1)][int(move_from[1])-1]:
                    allowed_movements.append(chr(ord(move_from[0])+1)+str(int(move_from[1])-1))
            if (int(move_from[1])==7) and ("P" not in board[move_from[0]][int(move_from[1])-2]) :
                allowed_movements.append(move_from[0]+str(int(move_from[1])-2))        
        elif "🏰" in piece:
            for i in range(move_from_n+1,9):
                if "P2" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            for i in range(move_from_n-1,0,-1):
                if "P2" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            #h=104,a=97 
            for i in range(ord(move_from_l)+1,105):
                if "P2" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:
                    break
            for i in range(ord(move_from_l)-1,96,-1):
                if "P2" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:  
                    break 
        elif "🐴" in piece:
            moves=[]
            moves.append(chr(ord(move_from_l)+2)+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)+2)+str(move_from_n+1))
            moves.append(chr(ord(move_from_l)-2)+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)-2)+str(move_from_n+1))
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n-2))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n-2))
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n+2))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n+2))
            for i in moves:
                if len(i)==2:
                    if i[0] in "abcdefgh" and i[1] in "12345678":
                        if "P2" not in board[i[0]][int(i[1])]:
                            allowed_movements.append(i[0]+i[1])           
        elif "👼" in piece:
            f_counter=ord(move_from_l)+1
            s_counter=ord(move_from_l)-1
            for i in range(move_from_n+1,9):
                if f_counter<=104:
                    if ("P2" not in board[chr(f_counter)][i]):
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter+=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter>=97:
                    if "P2" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter-=1
                    else:
                        break  
            f_counter=ord(move_from_l)-1
            s_counter=ord(move_from_l)+1
            for i in range(move_from_n+1,9):
                if f_counter>=97:
                    if "P2" not in board[chr(f_counter)][i]:
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter-=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter<=104:
                    if "P2" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter+=1
                    else:
                        break 
        elif "👑" in piece:
            for i in range(move_from_n+1,9):
                if "P2" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            for i in range(move_from_n-1,0,-1):
                if "P2" not in board[move_from_l][i]:
                    allowed_movements.append(move_from_l+str(i))
                else:
                    break
            for i in range(ord(move_from_l)+1,105):
                if "P2" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:
                    break
            for i in range(ord(move_from_l)-1,96,-1):
                if "P2" not in board[chr(i)][move_from_n]:
                    allowed_movements.append(chr(i)+str(move_from_n))
                else:  
                    break
            f_counter=ord(move_from_l)+1
            s_counter=ord(move_from_l)-1
            for i in range(move_from_n+1,9):#👼 
                if f_counter<=104:
                    if ("P2" not in board[chr(f_counter)][i]):
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter+=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter>=97:
                    if "P2" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter-=1
                    else:
                        break  
            f_counter=ord(move_from_l)-1
            s_counter=ord(move_from_l)+1
            for i in range(move_from_n+1,9):
                if f_counter>=97:
                    if "P2" not in board[chr(f_counter)][i]:
                        allowed_movements.append(chr(f_counter)+str(i))
                        f_counter-=1
                    else:
                        break  
            for i in range(move_from_n-1,0,-1):
                if s_counter<=104:
                    if "P2" not in board[chr(s_counter)][i]:
                        allowed_movements.append(chr(s_counter)+str(i))
                        s_counter+=1
                    else:
                        break 
        elif "🤴" in piece:
            moves=[]
            moves.append(move_from_l+str(move_from_n+1))
            moves.append(move_from_l+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n))#4
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n+1))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n+1))#
            moves.append(chr(ord(move_from_l)+1)+str(move_from_n-1))
            moves.append(chr(ord(move_from_l)-1)+str(move_from_n-1))
            for i in moves:
                if i[0] in "abcdefgh" and i[1] in "12345678":
                    if "P2" not in board[i[0]][int(i[1])]:
                        allowed_movements.append(i[0]+i[1])
            if len(allowed_movements)==0:
                king_2_cells=True  
    return allowed_movements                    

#give the first values for the board
def first_board():
    num=ord("a")
    counter=0
    #2 1 8 7
    for i in range(32):
        if i <8:
            board[chr(num)][2]=p1_pieces[counter]
            counter+=1
            num+=1
        elif i <16:
            if i ==8:
                 counter=8
                 num=ord("a")
                 board[chr(num)][1]=p1_pieces[counter]
                 counter+=1
                 num+=1
            else :     
                board[chr(num)][1]=p1_pieces[counter]
                counter+=1
                num+=1
        elif i <24:
            
            if i ==16:
                 counter=0
                 num=ord("a")
                 board[chr(num)][7]=p2_pieces[counter]
                 counter+=1
                 num+=1
            else :     
                board[chr(num)][7]=p2_pieces[counter]
                counter+=1
                num+=1
        else:
            if i ==24:
                 counter=8
                 num=ord("a")
                 board[chr(num)][8]=p2_pieces[counter]
                 counter+=1
                 num+=1
            else:     
                board[chr(num)][8]=p2_pieces[counter]
                counter+=1
                num+=1
#print the chess board
def printer():
    c.print(f"                         a              b             c              d              e              f              g             h       ")
    counter=0
    for i in list(range(9))[8:0:-1]:
            
            c.print(f"                  -----------------------------------------------------------------------------------------------------------------------",style='red')
            c.print(f"{p2_pushed_list[counter]} {p2_pushed_list[counter+1]}      {i}  |   {board["a"][i]}      |    {board["b"][i]}     |     {board["c"][i]}     |     {board["d"][i]}     |     {board["e"][i]}     |     {board["f"][i]}     |     {board["g"][i]}     |     {board["h"][i]}     | {p1_pushed_list[counter]} {p1_pushed_list[counter+1]}",style='green')
            counter+=2
    c.print(f"                  -----------------------------------------------------------------------------------------------------------------------",style='red') 
    c.print("")
#return boolean and cell from and cell to ,true if it's p1 and False if it's p2
def input_checker(player_flag):
    if player_flag ==True:
        while True :
                p1cf=input("P1 cell from->")
                if len(p1cf)!=2:
                    c.print('Wrong Info')
                    continue
                try :
                    int(p1cf[1])
                except:
                    c.print('Wrong Info')
                    continue   
                if ((p1cf[0] not in["a","b","c","d","e","f","g","h"] and p1cf[0] not in["A","B","C","D","E","F","G","H"])or (p1cf[1] not in ["1","2","3","4","5","6","7","8"])):
                    c.print("Wrong Input!")
                    continue
                break
        while True:    
            p1ct=input("\n"+"P1 cell to->")
            if len(p1ct)!=2:
                c.print('Wrong Info')
                continue
            try :
                int(p1ct[1])
            except:
                c.print('Wrong Info')
                continue   
            if ((p1ct[0] not in["a","b","c","d","e","f","g","h"] and p1ct[0] not in["A","B","C","D","E","F","G","H"])or (p1ct[1] not in ["1","2","3","4","5","6","7","8"])):
                c.print("Wrong Input!")
                continue
            return ["P1",p1cf,p1ct]

    else :
        while True :
            p2cf=input("\n\n"+"P2 cell from->")
            if len(p2cf)!=2:
                c.print('Wrong Info')
                continue
            try :
                int(p2cf[1])
            except:
                c.print('Wrong Info')
                continue   
            if ((p2cf[0] not in["a","b","c","d","e","f","g","h"] and p2cf[0] not in["A","B","C","D","E","F","G","H"])or (p2cf[1] not in ["1","2","3","4","5","6","7","8"])):
                c.print("Wrong Input!")
                continue
            break
        while True:
            p2ct=input("\n"+"P2 cell to->")
            c.print("\n\n")
            if len(p2ct)!=2:
                c.print('Wrong Info')
                continue
            try :
                int(p2ct[1])
            except:
                c.print('Wrong Info')
                continue   
            if ((p2ct[0] not in["a","b","c","d","e","f","g","h"] and p2ct[0] not in["A","B","C","D","E","F","G","H"])or (p2ct[1] not in ["1","2","3","4","5","6","7","8"])):
                c.print("Wrong Input!")
                continue
            return ["P2",p2cf,p2ct]   
            #a8 a4 a4 a3   
#a method return the position of the king 
def king_finder():
    d={"P1":"","P2":""}
    class BreakAllLoops(Exception):
        pass
    try :
        for i in "abcdefgh":
            for j in "12345678":
                if "P1🤴" ==board[i][int(j)]:
                    d["P1"]=i+j
                    raise BreakAllLoops
    except BreakAllLoops:
        pass 
    try :
        for i in "abcdefgh":
            for j in "12345678":
                if "P2🤴" ==board[i][int(j)]:
                    d["P2"]=i+j
                    raise BreakAllLoops
    except BreakAllLoops:
        pass   
    return d            

                