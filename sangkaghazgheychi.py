score1=0
score2=0
i = 0
while i <=4:
    player1=int(input("player1's choice:"))
    player2=int(input("player2's choice:"))
    if player1==1 and player2==3 or player1==2 and player2==1 or  player1==3 and player2==2:
        score1 = score1+1
    elif player2==1 and player1==3 or player2==2 and player1==1 or player2==3 and player1==2:
        score2=score2+1
    i = i+1
print("score1:",score1, "score2:", score2)
if score1>score2:
    print("player1 won!!")
elif score2>score1:
    print("plyer2 Won!!")