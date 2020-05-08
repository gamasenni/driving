country = input('你哪國人? ')
age = input('年齡? ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('可以考')
	else:
		print('不行啦')
elif country == '美國':
	if age >= 16:
		print('可以考')
	else:
		print('不行啦')
else:
	print('只能輸入台灣或美國')		