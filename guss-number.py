import random
start = input('請決定開始數字')
end = input('請決定最後數字')
start = int(start)
end = int(end)



r = random.randint(start, end)
count = 0


while True:
	count = count + 1
	num = input("請猜數字: ")
	num = int(num)

	if num == r:
		print("你猜對了")
		print('你猜了第', count, '次終於對了')
		break
	elif num > r:
		print("數字太大拉")
	elif num < r:
		print("數字太小拉")
	print('你猜了第', count, '次了')