import time
a = 69420
b = 0.0000000000001
for i in range(5):
	a = a * a 
start_time = time.time()
print("You have advanced scoliosis!")
print("you must click a lot btw") #you must click 1000000000000 * 8.462671807278899e+154 i think , but im not sure
while True:
	if a > 0:
		input()
		a = a - b
		print(a)
	else:
		end_time = time.time()
		le_time = round((end_time - start_time) * 1000)
		if le_time > 1000:
				print('you still have scoliosis + you have terminal cancer now')
				exit()
		print("gg you no longer have scoliosis")
		exit()

