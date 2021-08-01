import func_calc as fc

p1 = {'name' : 'Virat Kohli' , 'role' : 'bat' , 'runs' :112, '4' :10, '6' :0, 'balls' :119, 'field' :0}
p2 = {'name' : 'du Plessis' , 'role' : 'bat' , 'runs' :120, '4' :11, '6' :2, 'balls' :112, 'field' :0}
p3 = {'name' : 'Bhuvneshwar Kumar' , 'role' : 'bowl' , 'wkts' :1, 'overs' :10, 'runs' :71, 'field' :1}
p4 = {'name' : 'Yuzvendra Chahal' , 'role' : 'bowl' , 'wkts' :2, 'overs' :10, 'runs' :45, 'field' :0}
p5 = {'name' : 'Kuldeep Yadav' , 'role' : 'bowl' , 'wkts' :3, 'overs' :10, 'runs' :34, 'field' :0}

players = [p1, p2, p3, p4, p5]
scores = list()
man_of_match = dict()

def main():
    high_score = 0

    for i in range(0, 5):
        if players[i]['role'] == "bat":
            score = fc.batting(players[i])
            scores.append({'name': players[i]['name'], 'batscore': score})

        elif players[i]['role'] == "bowl":
            score = fc.bowling(players[i])
            scores.append({'name': players[i]['name'], 'bowlscore': score})

        if score > high_score:
            man_of_match.update(scores[i])
            high_score = score

    for score in scores:
        print(score)

    print("\nMan of the Match is  : {}".format(man_of_match))

main()
