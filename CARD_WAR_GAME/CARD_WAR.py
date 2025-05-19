import random
#Player class
class Player:
    def __init__(self,name,deck):
        self.name=name
        self.deck=deck

#Card class 
class Card:
    def __init__(self,card_type,card_power,idnum):
        self.card_type=card_type
        self.card_power=card_power
        self.idnum=idnum

card_list=[]
#A method to initialize instances of the classes as need
def initializer():
    deck_list=["hearts","diamonds","clubs","spades"]
    counter=0
    cards_counter=0
    for i in range(1,53):
        card_list.append(Card(deck_list[counter-1],cards_counter+1,i-1))
        cards_counter+=1
        if i%13==0:
            counter+=1
            cards_counter=0
initializer()
random_nums_list=list(range(0,52))
p1_list=[]
p2_list=[]
#generate random numbers from 0 to 52
randcounter=0
while True:
    num =random.randint(0,52)
    if num  in random_nums_list and randcounter%2==0:
        p1_list.append(num)
        random_nums_list.remove(num)
        randcounter+=1
    elif num in random_nums_list and randcounter%2!=0:
        p2_list.append(num)
        random_nums_list.remove(num)
        randcounter+=1
    elif len(random_nums_list)==0:
        break     
#generate 2 decks with mixed 26 cards in every deck
p1_deck=[]
p2_deck=[]
for i in p1_list:
    for j in card_list:
        if i ==j.idnum:
            p1_deck.append(j)
            card_list.remove(j)
            break
for i in p2_list:
    for j in card_list:
        if i ==j.idnum:
            p2_deck.append(j)
            card_list.remove(j)
            break        
#generate 2 players
p1 = Player('P1',p1_deck)
p2=Player('P2',p2_deck)
#Printer method
def printer(list1,list2):
    list1n=[]
    list2n=[]
    cards=[]
    for i in list1:
        tup=(i.card_power,i.card_type)
        list1n.append(tup)
    for i in list2:
        tup=(i.card_power,i.card_type)
        list2n.append(tup)  
    for i in cards_holder:
        tup=(i.card_power,i.card_type)
        cards.append(tup)
    print(list1n,"\n                              Player 1\n\n","                               ",cards,"\n\n                              Player 2\n",list2n,"\n**************************************************************************************************************************************************")
#A method takes a list of instances with value and return the instance connected with the value
cards_holder=[]
def swapperp1(idn):
    if len(p1_deck) ==0 :
        print('Player 2 Won!')
        exit(0)
    else :   
        for i in p1_deck:
            if i.idnum ==idn:
                cards_holder.append(p1_deck.pop(p1_deck.index(i)))
                break


def swapperp2(idn):
    if len(p2_deck) ==0 :
        print('Player 1 Won!')
        exit(0)
    else :    
        for i in p2_deck:
            if i.idnum ==idn:
                cards_holder.append(p2_deck.pop(p2_deck.index(i)))
                print('fuc',len(cards_holder))
                break
def changer(destenation):
    if destenation==1:
        for i in range(0,len(cards_holder)):
            p1_deck.append(cards_holder.pop(0))
                        
    else:
        for i in range(0,len(cards_holder)):
            p2_deck.append(cards_holder.pop(0))                  
printer(p1_deck,p2_deck)
input('Game start ?')
#chooce method
def chooce(plist,num):
    numx=0
    if num ==1:
        numx=2
    else:
        numx=1    
    try:
        return random.choice(plist)
    except:
        print(f"Game End \nPlayer{numx} Won!")   
        exit(0) 

#Start the game
entire = False
def game_start():
    global entire
    while True :
        swap1=chooce(p1_deck,1)
        id1=swap1.idnum
        power1=swap1.card_power
        swap2=chooce(p2_deck,2)
        id2=swap2.idnum
        power2=swap2.card_power
        swapperp1(id1)
        swapperp2(id2)
        printer(p1_deck,p2_deck)
        if power1<power2 and entire==False:
            changer(2)
            printer(p1_deck,p2_deck)
        elif power1>power2 and entire==False:
            changer(1)
            printer(p1_deck,p2_deck)
        
        elif power1==power2:
            swap1=chooce(p1_deck,1)
            id1=swap1.idnum
            power1_1=swap1.card_power
            swap2=chooce(p2_deck,2)
            id2=swap2.idnum
            power2_1=swap2.card_power
            swapperp1(id1)
            swapperp2(id2)
            swap1=chooce(p1_deck,1)
            id1=swap1.idnum
            power1_2=swap1.card_power
            swap2=chooce(p2_deck,2)
            id2=swap2.idnum
            power2_2=swap2.card_power
            swapperp1(id1)
            swapperp2(id2)
            swap1=chooce(p1_deck,1)
            id1=swap1.idnum
            power1_3=swap1.card_power
            swap2=chooce(p2_deck,2)
            id2=swap2.idnum
            power2_3=swap2.card_power
            swapperp1(id1)
            swapperp2(id2)
            printer(p1_deck,p2_deck)
            if power1_1<power2_1:
                changer(2)
                printer(p1_deck,p2_deck)
            elif power1_1>power2_1:
                changer(1)
                printer(p1_deck,p2_deck)
            elif power1_1==power2_1:
                        if power1_2<power2_2:
                            changer(2)
                            printer(p1_deck,p2_deck)
                        elif power1_2>power2_2:
                            changer(1)
                            printer(p1_deck,p2_deck)
                        elif power1_2==power2_2:
                            if power1_3<power2_3:
                               changer(2)
                               printer(p1_deck,p2_deck)
                            elif power1_3>power2_3:
                               changer(1)
                               printer(p1_deck,p2_deck)
                            elif power1_3==power2_3:
                                entire=True
        elif power1==1 and entire==False:
            changer(1)
            printer(p1_deck,p2_deck)
        elif power2==1 and entire==False:
            changer(2)
            printer(p1_deck,p2_deck)    
        input('Continue ?')
game_start()
