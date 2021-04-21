

import math

import json 

import pprint

with open("all_people.txt", "r") as fp:
    all_people = json.load(fp)


with open("parties.txt", "r") as fp:
    hebrew = json.load(fp)

print(hebrew)

for i in all_people:
    for j in range(len(i)):
        i[j] = float(i[j])

def flip(ls,i):
    a = ls
    if(a[i] == 1):
        a[i] = 5.0
    elif(a[i] == 2):
        a[i] = 4.0
    elif(a[i] == 5):
        a[i] = 1.0
    elif(a[i] == 4):
        a[i] = 2.0
    return a

parties1 = [
    [3,3,5,3,2,4,5,5], #blue and white 0
    [3, 3, 4, 3, 4, 4, 5, 5], #likud 1
    [2, 3, 3, 2, 5, 2, 4, 3], # labour 2 
    [2, 2, 2, 2, 2, 2, 3, 5], #meretz 3
    [3, 4, 2, 4, 3, 5, 3, 4], # Bible jewishness 4
    [1, 1, 1, 1.75, 4, 1, 2, 1], #The joint list 5
    [5, 5, 2, 2, 4, 5, 4, 4], # Sh"s 6
    [5, 5, 1, 1.75, 4, 1, 3, 2], #raam 7
    [3, 3, 5, 3, 4, 3, 4, 4] # our home israel 8 
]
parties = [
"5	2	5	5	3	3	3.5	3	2	3	3	4	5	4".split('	'), #blue and white 0
"5	3	5	4	2	4	3	5	1	5	5	5	5	5".split('	'),#likud 1
"5	1.5	5	4	2	2	4	5	2	3	1	3	2	3".split('	'), # labour 2 
"5	1.5	5	3	3	2	4	5	2	3	1	1	2	1".split('	'),#meretz 3
"5	1	5	3	3	3	4	5	2	5	5	4	5	4".split('	'),# Bible jewishness 4
"1	5	1	1	3	2	4	2	5	3	3	3	1	2".split('	'),#The joint list 5
"5	1	5	2	3	3	4	5	2	5	5	4	4	4".split('	'), # Sh"s 6
"1	2	1	1	3	3	3	1	5	3	3	3	2	3".split('	'),#raam 7
"5	5	4	4	3	2	1	5	1	1	1	5	4	4".split('	'),# our home israel 8 
"5	4	4	2	5	2	4	3	2	2	2	5	4	5".split('	'),#There's a Future
"5	2	4	3	3	4	2	4	2	4	5	2	2	2".split('	') ]#The New Right


for i in parties:
    for j in range(len(i)):
        i[j] = float(i[j])


def dis(x,y):
    return math.pow((x-y),2)

def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += dis(x[i],y[i])
    d = math.sqrt(d)
    return d

def closest(per, parties):
    close = 0
    short = distance(per,parties[0])
    for i in range(len(parties)):
        d = distance(per,parties[i])
        if(d<short):
            short = d 
            close = i
    return close

all_people_changed = all_people#[]

def average(x,y):
    return (float(x)+float(y))/2



# for i in all_people:
#     person = []
#     app = lambda x: person.append(x)
#     app(average(flip(i,1)[1],i[0]))
#     app(i[2])
#     app(average(i[3],flip(i,4)[4]))
#     app(average(i[5],flip(i,6)[6]))
#     app(average(i[7],flip(i,8)[8]))
#     app(average(i[9],i[10]))
#     app(average(i[11],i[13]))
#     app(i[12])
#     all_people_changed.append(person)

votes = []

def find_thing(all,parties):
    ls = []
    for i in range(len(all)):
        ls.append(closest(all[i],parties))
    return ls

votes = find_thing(all_people_changed,parties)



def get_party(num):
    parties = {
                0:"כחול לבן",
                1:"הליכוד",
                2:"העבודה",
                3:"מר'צ",
                4: "יהדות התורה",
                5: "הרשימה המשותפת",
                6: "ש'ס",
                7: "רע'מ",
                8: "ישראל ביתנו",
                9:"יש עתיד",
                10:"הימין החדש"
                }
    return parties.get(num,"אחר")

for i in range(len(votes)):
    votes[i] = get_party(votes[i])

def match_results(ls, ls1):
    matched = []
    for i in range(len(ls)):
        string = f"Person number {i+2} Who Voted for {hebrew[i]}: {ls1[i]} ==> Should have voted for {ls[i]}\n"
        print(string)
        #with open("matched.txt", "a") as f: 
           # f.write(string+"\n")
        matched.append(string)

    return matched
#pp = pprint.PrettyPrinter(indent=1)
#pp.pprint(match_results(votes,all_people_changed))


match_results(votes,all_people_changed)


