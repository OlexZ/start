amount_match = int(input())
team = {}
for i in range(amount_match):
    temp_vs_temp = input().split()
    for j in temp_vs_temp:
        team1, res1, team2, res2 = j.split(';')
        if team1 not in team:
            team.setdefault(team1, [0, 0, 0, 0, 0])
        if team2 not in team:
            team.setdefault(team2, [0, 0, 0, 0, 0])
        if int(res1) > int(res2):
            team[team1][0] += 1
            team[team1][1] += 1
            team[team1][4] += 3
            team[team2][0] += 1
            team[team2][3] += 1
        elif int(res2) > int(res1):
            team[team2][0] += 1
            team[team2][1] += 1
            team[team2][4] += 3
            team[team1][0] += 1
            team[team1][3] += 1
        else:
            team[team1][0] += 1
            team[team1][2] += 1
            team[team1][4] += 1
            team[team2][0] += 1
            team[team2][2] += 1
            team[team2][4] += 1
for key, value in team.items():
    print(key, value, end=': ')
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2