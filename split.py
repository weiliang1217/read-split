import os # operating system

description0 = []
description1 = [] 
description2 = []
n = 0
if os.path.isfile('wp1.csv'):
	print('file exist')
	#讀取檔案
	with open('wp1.csv', 'r', encoding='utf-8') as file: #read 也是需要相同的編碼方可讀取出正確的資料內容
		for line in file:
			if '商品,價錢' in line: #Boolean->True或是Fail 
				continue #滿足上述boolean值 Continue繼續表示直接進入'line #1'
			a = line.split(',') # split為分割，並已',' 作為區分的指標
			print('這是a的，line中第',n + 1, a)
			print('----------------')
			b = line.strip().split(',') # 注意執行順序 #1將line中移除\n；#2 再以','作為區分；#3 最後再存入 a str字串中。
			print('這是b的，line中第',n + 1, b)
			print('----------------')
			name, price = line.strip().split(',') # 得知透過strip()與split已','作為區分後，line已經被拆分為[0], [1]清單，我們透過name, price 宣稱 = [0], [1] 
			description2.append([name, price])
			n += 1
#description0.append(a)
#description1.append(b)
#description2.append([name, price])
#print('final --------------')
#print(description0)
#print(description1)
	print(description2)	
else:
	print('file unexist')


# 寫入特定檔案
products = []
while True: #強制進入loop環節；(boolen-> True or fail)
	item = input('商品名稱: ')
	if item == 'q':
		break # 當再商品紀錄: 輸入'q'時，會執行break 離開loop
	price = input('商品價錢: ')
	products.append([item, price])
#print(products)
#print(products[0][0])
#print(products[0][1])
#print(products[1][0])
#print(products[1][1])

# 分別寫入.csv or .txt file
with open('wp1.csv', 'w', encoding = 'utf-8') as file: #1 將'wp1.csv'作為file稱呼，隨著with open結束 file定義也release。 
                                                       #2 encoding = 'utf-8 '將其內容已utf-8編碼類型寫入csv之中，
                                                       # 當然excel內建初始設定非'utf-8'所以繁體中文會呈現???
	file.write('商品,價錢\n')
	for product in products:
		file.write(product[0] + ',' + product[1] + '\n')

with open('wp1.txt', 'w') as file:
	file.write('商品,價錢\n')
	for product in products:
		file.write(product[0] + ',' + product[1] + '\n')
