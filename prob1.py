import random

def pick_ball_experiment():
    balls = [1,2,3,4,5,6]
    result = random.choice(balls)
    pro = balls.count(6) / len(balls)
    print("Probability of pickking Red ball no 6 is:", pro)
    if result == 6:
        return 'Six was pickked'
    else:
        return ' Better luck nex time'
    
res = pick_ball_experiment()
print(res)