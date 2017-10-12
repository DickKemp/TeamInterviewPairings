def comb(sofar, rest, n, result):
    if n==0:
        result.append(sofar)

    else:
        for i in range(len(rest)):
            copysofar = sofar[:]
            copysofar.append(rest[i])
            comb(copysofar, rest[i+1:], n-1, result)

def compliment(a, b):
    comp = []
    for i in range(len(b)):
        if b[i] in a:
            continue
        else:
            comp.append(b[i])
    return comp

def valueof(p,cp):
    score = 0
    for t in p:
        for c in teams[t]["cu"]:
            for other in cp:
                if c in teams[other]["re"]:
                    score += 1;
    return score;

teams = {}
allteams = ['ApartmentTeam1', 'ApartmentTeam2', 'DogTeam1', 'GraduationTeam1', 'GraduationTeam2', 'ParkingTeam1', 'RestaurantTeam1', 'RestaurantTeam2']

teams['ApartmentTeam1'] = { "cu" : ['Gabrielle', 'Hannah'], "re" : ['Kevin', 'Robert']}
teams['ApartmentTeam2'] = { "cu" : ['Cassidy', 'Joseph'], "re" : ['Caroline', 'Laura']}
teams['DogTeam1'] = { "cu" : ['Vincent', 'Xiaoyu'], "re" : ['Kaiwen', 'Zhe']}
teams['GraduationTeam1'] = { "cu" : ['Caroline', 'Laura'], "re" : ['Joseph', 'Xiaoyu']}
teams['GraduationTeam2'] = { "cu" : ['Prateek', 'Richard'], "re" : ['Ayana', 'Hannah']}
teams['ParkingTeam1'] = { "cu" : ['Michael', 'Robert'], "re" : ['Prateek', 'Vincent']}
teams['RestaurantTeam1'] = { "cu" : ['Ayana', 'Kevin'], "re" : ['Michael', 'Richard']}
teams['RestaurantTeam2'] = { "cu" : ['Kaiwen', 'Zhe'], "re" : ['Cassidy', 'Gabrielle']}

#all = [1,2,3,4,5,6,7,8]
all = allteams
combinations = []
comb([], all, 4, combinations)



for i in combinations:
    group1 = i
    group2 = compliment(i,all)

    v1 = valueof(group1, group2)
    v2 = valueof(group2, group1)
    if v1 + v2 > 13:
        print()
        print("OPTION")
        print("group 1:")
        for p in group1:
            print(p + " REs: [" + str(teams[p]["re"]) + "] to interview their customers: []"+ str(teams[p]["cu"]) + "]")

        print("group 2:")
        for p in group2:
            print(p + " REs: [" + str(teams[p]["re"]) + "] to interview their customers: []"+ str(teams[p]["cu"]) + "]")

