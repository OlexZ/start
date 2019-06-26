amount_match = int(input())
team = {}
for i in range(amount_match):
        temp_vs_temp = input().split(';')
        if temp_vs_temp[0] not in team:
            team.setdefault(temp_vs_temp[0], [0, 0, 0, 0, 0])
        if temp_vs_temp[2] not in team:
            team.setdefault(temp_vs_temp[2], [0, 0, 0, 0, 0])
        if int(temp_vs_temp[1]) > int(temp_vs_temp[3]):
            team[temp_vs_temp[0]][0] += 1
            team[temp_vs_temp[0]][1] += 1
            team[temp_vs_temp[0]][4] += 3
            team[temp_vs_temp[2]][0] += 1
            team[temp_vs_temp[2]][3] += 1
        elif int(temp_vs_temp[3]) > int(temp_vs_temp[1]):
            team[temp_vs_temp[2]][0] += 1
            team[temp_vs_temp[2]][1] += 1
            team[temp_vs_temp[2]][4] += 3
            team[temp_vs_temp[0]][0] += 1
            team[temp_vs_temp[0]][3] += 1
        else:
            team[temp_vs_temp[0]][0] += 1
            team[temp_vs_temp[0]][2] += 1
            team[temp_vs_temp[0]][4] += 1
            team[temp_vs_temp[2]][0] += 1
            team[temp_vs_temp[2]][2] += 1
            team[temp_vs_temp[2]][4] += 1
for key, value in team.items():
    print(key+':',*value)