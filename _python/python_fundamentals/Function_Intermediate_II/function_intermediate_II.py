#1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0].update({'last_name': 'Bryant'})
print(students)

new_List = sports_directory.get('soccer')
new_List[0] = 'Andres'
sports_directory.update({'soccer': new_List})
print(sports_directory)

z[0].update({'y': 30})
print(z)


#2
def iterateDictionary(lst):
    for i in lst:
        print(i)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines)

#3
def iterateDictionary2(key, dict_list):
    for i in dict_list:
        print(i.get(key))

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dct):
    key_list = dct.keys()
    for key in key_list:
        list_value = dct.get(key)
        print(f"{len(list_value)} {key.upper()}")
        for value in list_value:
            print(value)
        print("")
printInfo(dojo)

