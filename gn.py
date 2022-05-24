# 猜數字遊戲
import random
s = input('請決定下限(正整數): ')
s = int(s)
e = input('請決定上限(正整數): ')
e = int(e)
r = random.randint(s, e)
c = 0
while True:
	c += 1
	n = input('請猜數字: ')
	n = int(n)
	if n == r:
		print('猜對了')
		print('你共猜了', c, '次') 
		break
	elif n > r:
		print('比答案大')
	elif n < r:
		print('比答案小')
	print('這是你猜的第', c,'次')
	



