# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
str1 = "パトカー"
str2 = "タクシー"
# str = list(map(lambda i:str1[i] + str2[i],range(4)))
str = ''.join([ str1[i] + str2[i]  for i in range(4) ])

print(str)


# http://programming-study.com/technology/python-list-join/
# https://docs.python.jp/3/tutorial/datastructures.html