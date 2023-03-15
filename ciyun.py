import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file = '绿.txt'
wenben = open(file,'r',encoding = 'utf-8').read()

for c in '，。“”；':
    wenben = wenben.replace(c,"")

#wenben = wenben.split()
words = jieba.lcut(wenben)
print(words)

words=' '.join(words)
#print(wenben)
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
liebiao = list(counts.items())
liebiao.sort(key=lambda x: x[1], reverse=True)

for i in range(10):
    c=liebiao[i]
    print(c[0],c[1])

ciyun=WordCloud(background_color='white',font_path='msyh.ttc')
ciyun.generate(words)

# 显示词云图
plt.imshow(ciyun)
plt.axis('off')
plt.show()