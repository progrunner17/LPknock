# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
str = "stressed"
print(str[::-1])

# s[i:j:k] は
# slice of s from i to j with step k
# The slice of s from i to j with step k is defined as the sequence of items with index x = i + n*k such that 0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2*k, i+3*k and so on, stopping when j is reached (but never including j).
# If i or j is greater than len(s), use len(s). If i or j are omitted or None, they become “end” values (which end depends on the sign of k).
# http://d.hatena.ne.jp/redcat_prog/20111104/1320395840
