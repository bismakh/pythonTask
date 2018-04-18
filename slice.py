print('welcome in slicing of list ')
players = ['who','16','when','23','what','whom']
numbers = [23, 24, 25, 45, 56 ,67,78]
print(players[0:3])
for play in players[0:]:
	print(play)
print(players[1:4])	
print(players[:3])
print(players[:-4])	
print(players[2:])
print(numbers[2:])		
# copy a list through slice..... 
sums = numbers[:]
sums.append('bisma')
numbers.append('khan')
sums = numbers
print(numbers)
print(sums)