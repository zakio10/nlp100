# 65
# メモ
# カテゴリー名がgramから始まる行は文法的アナロジーで、それ以外が意味的アナロジー
# それぞれの正解率を計算する

with open('ans64.txt') as f:
    data = f.readlines()

ans = []
gram_num = 0
gram_ok = 0
nongram_num = 0
nongram_ok = 0

for s in data:
    s = s.rstrip()
    s = s.split(' ')

    if 'gram' in s[0]:
        # 意味的アナロジー
        gram_num += 1
        if s[4] == s[5]:
            gram_ok += 1
    else:
        # 文法的アナロジー
        nongram_num += 1
        if s[4] == s[5]:
            nongram_ok += 1

print("semantic analogy:\t", gram_ok / gram_num)
print("syntactic analogy:\t", nongram_ok / nongram_num)

# semantic analogy:        0.7400468384074942
# syntactic analogy:       0.7308602999210734