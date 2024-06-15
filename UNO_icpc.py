
#UNO

T=int(input())
current_player=1
direction=1
for i in range(T):
    N, K = map(int, input().split())
    history = input().strip()
    #current_player=1
    #direction=1
    for i in history:
        if i == 'U':
            #current_player = (current_player + direction - 1) % N + 1
            #current_player= (current_player) + 1*(direction)
            if direction==1:
                if current_player==1:
                    current_player=2
                elif current_player==2:
                    current_player=3
                elif current_player==3:
                    current_player=1
            elif direction==-1:
                if current_player==1:
                    current_player=3
                elif current_player==2:
                    current_player=1
                elif current_player==3:
                    current_player=2

        
        
        elif i == 'S':
            #current_player = (current_player + 2 * direction - 1) % N + 1
            #current_player= (current_player) + 2*(direction)
            if direction==1:
                if current_player==1:
                    current_player=3
                elif current_player==2:
                    current_player=1
                elif current_player==3:
                    current_player=2
            elif direction==-1:
                if current_player==1:
                    current_player=2
                elif current_player==2:
                    current_player=1
                elif current_player==3:
                    current_player=2
        elif i == 'R':
            direction *= -1
            #current_player = (current_player + direction - 1) % N + 1
            if direction==1:
                if current_player==1:
                    current_player=2
                elif current_player==2:
                    current_player=3
                elif current_player==3:
                    current_player=1
            elif direction == -1:
                if current_player==1:
                    current_player=3
                elif current_player==2:
                    current_player=1
                elif current_player==3:
                    current_player=2
    print(current_player)



