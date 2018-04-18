 print('welcome in chapter 7 DICTIONARY')
person = {'name':'bisma','age': 27, 'grade':'B', 'education':'BS-CS' }
 print(person)
 print(person['name'])
 print(person['age'])
 print(person['grade'])
 print(person['education'])
 new_age = person['age']+5 # addition apply here
 print('your age for Eligibility is '+ str(new_age)) + '\t '+ "congrats !!"
person['house_no'] = 165
 person['city'] = 'karachi'
 print(person)
# empty dictionary .....
 user_a = {}
 user_a['name']= 'ali'
 user_a['color']= 'white'
 user_a['age']= 23
 user_a['city']= 'mumbai'
 print(user_a)
 # changing in color of user .....
user_a['color'] = 'baige'
print(user_a)
# delete a value from dictionary ..... using 'del'
del user_a['city']
print(user_a)
alien = {'positionX': 25, 'positionY': 30, 'speed':'medium','color':'green'}
print("Alian Origional Position \n" + str(alien['positionX']))
if alien['speed'] == 'slow':
     x_inc = 1
elif alien['speed'] == 'medium':
     x_inc = 2 
else:
	x_inc = 3 

alien['positionX'] = alien['positionX'] + x_inc
print('New position of ALIEN  \n' + str(alien['positionX']))

language = {
	'sarah':'C',
	
}
