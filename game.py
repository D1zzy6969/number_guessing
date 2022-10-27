import random
import time
x = random.randint(0,100)
start_time = time.time()
y = 0
sk = 0
minejumi = []
while y != x:
    y = int(input("Tavs skaitļa minējums: "))
    if y > x:
        print("vajadzīgais skaitlis ir mazaks")
    elif y < x:
        print('vajadzīgais skaitlis ir lielāks')
    else:
        print('Skaitlis tika uzminēts!')
    minejumi.append(y)
    sk = sk+1
print(minejumi)  
print(f'skaitļa atrašana tev prasīja {sk} mēģinājumus.')
print(f'videjais aritmetiskais ir {sum(minejumi)/sk}')
sum_of_difference = 0
for i in minejumi:
    sum_of_difference += sum_of_difference +abs(i- x)
print(sum_of_difference / len(minejumi))
print('Tu spēlēji %s sekundes' % (time.time() - start_time))
