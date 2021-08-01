def batting(player):
    points = 0

    for key, value in player.items():
        if key == 'runs':
            runs = value
            points += int(runs/2);

            if runs >= 100:
                points += 15
            elif runs >= 50:
                points += 5

        if key == 'balls':
            strike_rate = runs/value * 100;

            if strike_rate > 100:
                points += 6
            elif strike_rate >= 80:
                points += 2

        if key == '4':
            points += value

        if key == '6':
            points += 2*value

        if key == 'field':
            points += 10*value

    return points


def bowling(player):
    points = 0

    for key, value in player.items():
        if key == 'wkts':
            points += 10*value

            if value >= 5:
                points += 10
            elif value >= 3:
                points += 5

        if key == 'overs':
            overs = value

        if key == 'runs':
            eco_rate = value/overs

            if eco_rate < 2:
                points += 10
            elif eco_rate <= 3.5:
                points += 7
            elif eco_rate <= 4.5:
                points += 4

        if key == 'field':
            points += 10*value

    return points
