dict = {}
ans = 'y'
lst = []

while ans == 'y':
    name = input("Enter the team name: ")
    win = int(input("Enter the number of matches won: "))
    lost = int(input("Enter the number of matches lost: "))
    lst = list((win,lost))

    dict[name] = lst
    ans = input("More teams?(y/n)")
    
print(dict)

team_name = input("Enter the required team name: ")
win_per = (dict[team_name][0])/(dict[team_name][0] + dict[team_name][1])*100
print("Winning percentage is",win_per)

total_wins = []
win_lst = []
for key in dict:
    total_wins.append(dict[key][0])

    if dict[key][0]>0:
        win_lst.append(key)

print("Number of wins is",total_wins)
print("Teams that have winning records is",win_lst)