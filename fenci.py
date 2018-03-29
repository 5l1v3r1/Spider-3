import jieba
import jieba.analyse

#第一步：分词，这里使用结巴分词全模式
text = '''应用于肿瘤放射后副反应、咽喉部炎症的组合物及其制备'''
# fenci_text = jieba.cut(text)
# #print("/ ".join(fenci_text))
# for word in fenci_text:
#     print(word)
a=jieba.analyse.extract_tags(text, topK = 7, allowPOS = ())
print(a)
# #第二步：去停用词
# #这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
# stopwords = {}.fromkeys([ line.rstrip() for line in open('stopwords.txt') ])
# final = ""
# for word in fenci_text:
#     if word not in stopwords:
#         if (word != "。" and word != "，") :
#             final = final + " " + word
# print(final)
#
# #第三步：提取关键词
# a=jieba.analyse.extract_tags(text, topK = 5, withWeight = True, allowPOS = ())
# print(a)

