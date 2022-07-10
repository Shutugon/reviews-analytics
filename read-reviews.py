data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:   
			print(len(data)) 
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100字')  # 16~19 是在做清單的篩選，篩出留言字數小於100字 
print(new[0])

#good = []
#for d in data:
#	if 'good' in d:  #如果評論中有提到good
#		good.append(d)
#print('一共有', len(good), '筆提到good')

good = [d for d in data if 'good' in d]  # 承上寫法的進階速寫法，可找出有good的評論
print(good)

bad = ['bad' in d for d in data]   # 'bad' in d 是一種運算，其運算結果為布林值
print(bad)

# 文字計數

wc = {}  # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1   # 如果字典中有word，就把字典中word的計數加一
		else:
			wc[word] = 1  # 新增新的key進字典 

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查啥字？')
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	if word in wc:
		print(word, '總共出現的次數為', wc[word])
	else:
		print('這個字沒有出現過喔')


