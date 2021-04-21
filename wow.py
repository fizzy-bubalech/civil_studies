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

parties1 = [
    [5.0, 2.0, 5.0, 5.0, 3.0, 3.0, 3.5, 3.0, 2.0, 3.0, 3.0, 4.0, 5.0, 4.0],
    [5.0, 3.0, 5.0, 4.0, 2.0, 4.0, 3.0, 5.0, 1.0, 5.0, 5.0, 5.0, 5.0, 5.0], 
    [5.0, 1.5, 5.0, 4.0, 2.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0],
    [5.0, 1.5, 5.0, 3.0, 3.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 1.0, 2.0, 1.0],
    [5.0, 1.0, 5.0, 3.0, 3.0, 3.0, 4.0, 5.0, 2.0, 5.0, 5.0, 4.0, 5.0, 4.0],
    [1.0, 5.0, 1.0, 1.0, 3.0, 2.0, 4.0, 2.0, 5.0, 3.0, 3.0, 3.0, 1.0, 2.0],
    [5.0, 1.0, 5.0, 2.0, 3.0, 3.0, 4.0, 5.0, 2.0, 5.0, 5.0, 4.0, 4.0, 4.0],
    [1.0, 2.0, 1.0, 1.0, 3.0, 3.0, 3.0, 1.0, 5.0, 3.0, 3.0, 3.0, 2.0, 3.0], 
    [5.0, 5.0, 4.0, 4.0, 3.0, 2.0, 1.0, 5.0, 1.0, 1.0, 1.0, 5.0, 4.0, 4.0], 
    [5.0, 4.0, 4.0, 2.0, 5.0, 2.0, 4.0, 3.0, 2.0, 2.0, 2.0, 5.0, 4.0, 5.0], 
    [5.0, 2.0, 4.0, 3.0, 3.0, 4.0, 2.0, 4.0, 2.0, 4.0, 5.0, 2.0, 2.0, 2.0]]
for i in parties:
    for j in range(len(i)):
        i[j] = float(i[j])

print("Jewish Nation	Church & State	National Home 	Military Actions	Diplomatic Actions	State & Economy	Social & Economic Equality	Jewish Alliya	Return PA Refugees	Orthodox Convertion	Orthodoxy&who is Jewish	Party Leader	In Goverment	Party Leader ID".split('	'))