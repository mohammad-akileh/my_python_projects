def flipper(flag):
    return not flag
tic_tac_lists ={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,}
def printing(list):
    print(f'  {tic_tac_lists["7"]}  |  {tic_tac_lists["8"]}  |  {tic_tac_lists["9"]}  ')
    print('     |     |     ')
    print(f'  {tic_tac_lists["4"]}  |  {tic_tac_lists["5"]}  |  {tic_tac_lists["6"]}  ')
    print('     |     |     ')
    print(f'  {tic_tac_lists["1"]}  |  {tic_tac_lists["2"]}  |  {tic_tac_lists["3"]}  ')
d =tic_tac_lists
def checker():
    if (d["1"]=='X' and d["2"]=='X' and d["3"]=='X') or (d["4"]=='X' and d["5"]=='X' and d["6"]=='X') or(d["7"]=='X' and d["8"]=='X' and d["9"]=='X') or (d["7"]=='X' and d["4"]=='X' and d["1"]=='X')or (d["8"]=='X' and d["5"]=='X' and d["2"]=='X')or (d["9"]=='X' and d["6"]=='X' and d["3"]=='X')or (d["7"]=='X' and d["5"]=='X' and d["3"]=='X')or (d["9"]=='X' and d["5"]=='X' and d["1"]=='X'):
        return 'x'
    elif (d["1"]=='O' and d["2"]=='O' and d["3"]=='O') or (d["4"]=='O' and d["5"]=='O' and d["6"]=='O') or(d["7"]=='O' and d["8"]=='O' and d["9"]=='O') or (d["7"]=='O' and d["4"]=='O' and d["1"]=='O')or (d["8"]=='O' and d["5"]=='O' and d["2"]=='O')or (d["9"]=='O' and d["6"]=='O' and d["3"]=='O')or (d["7"]=='O' and d["5"]=='O' and d["3"]=='O')or (d["9"]=='O' and d["5"]=='O' and d["1"]=='O'):
        return 'o'
    elif all(value in ('X', 'O') for value in d.values()):
        return 'end'
    
    
def printer(l,its):
    flag=''
    value = checker()
    if tic_tac_lists[l] ==int(l) and its ==True:
        tic_tac_lists[l]='X'
        flag ='True'
        value = checker()
        if value =='x':
            if checker()=='end':
                print(tic_tac_lists)
                printing(tic_tac_lists)
                return 'end'
            else :
                 printing(tic_tac_lists)
            return 'x'
        elif value =='end':
            printing(tic_tac_lists)
            return 'end'
    elif tic_tac_lists[l] ==int(l) and its ==False:
        tic_tac_lists[l]='O'
        flag ='false'
        value = checker()
        if value =='o':
            if checker()=='end':
                print(tic_tac_lists)
                printing(tic_tac_lists)
                return 'end'
            else :
                 printing(tic_tac_lists)
                 return 'o'
        elif value =='end':
            printing(tic_tac_lists)
            return 'end'    
    elif value =='end':
           return 'end'
    else :
        return 'False'
    printing(l)
    return 'True'
def player_first():
    first=False
    while True :
        play =input('What do you want to be X or O (X will start first)')
        if 'x' ==play or 'X' == play:
          return True
        elif 'o' ==play or play =='O':
            return False
        else :
            print('please select X or O')
    
def tic_tac_play(flag):
   winning_flag=True
   while winning_flag :
    user_input=''
    if flag ==True :
       its=True
       while True :
           user_input=input('Choose num between 1,9 for X player->')
           if user_input not in ['1','2','3','4','5','6','7','8','9']:
               print('Wrong Input!')
               break
           else :
               output =printer(user_input,its)
               if output =='True' :
                flag=flipper(flag)
                break
               elif output == 'x':
                   print('fuck')
                   print('X won!')
                   winning_flag=False
                   break
               elif output =='end':
                   print("Game End !\nNobody won!")
                   winning_flag=False
                   break
    else :
       its=False
       while True :
          user_input=input('Choose num between 1,9 for O player->')
          if user_input not in ['1','2','3','4','5','6','7','8','9']:
               print('Wrong Input!')
               break
          else :
               output =printer(user_input,its)
               if output=='True' :
                  printer(user_input,its)
                  flag=flipper(flag)
                  break
               elif output =='o':
                   print('fuck')
                   print('O won!')
                   winning_flag=False
                   break
               elif output =='end':
                   print('Game End !\nNobody won!')
                   winning_flag=False
                   break    
print("We will play X O game Based on this Table")
print(f'  7  |  8  |  9  ')
print('     |     |     ')
print(f'  4  |  5  |  6  ')
print('     |     |     ')
print(f'  1  |  2  |  3  ')
tic_tac_play(player_first())
