#Lists:
my_list = [10,20,30, 40, 50]
    for i in mylist:
    print i



#Tuples:
my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for i in my_tup:
        print i



#Dict (is a hash-table):
my_dict = {'name': 'Bronx', 'age': '2', 'occupation': "Corey's Dog"}
for key, val in my_dict.iteritems():
    print("My {} is {}". format(key, val))



#Set:
my_set = {10,20,30,40,50,10,20,30,40,50}
    for i in my_set:
        print(i)