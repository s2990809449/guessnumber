# 猜數字遊戲
import random
r = random.randint(1, 100)
c = 1
c = int(c)
while True:
	n = input('請輸入1~100的正整數: ')
	n = int(n)
	if n == r:
		print('猜對了')
		print('你共猜了', c, '次') 
		break
	elif n > r:
		print('比答案大')
	elif n < r:
		print('比答案小')
	c = c + 1



