#string compression(char + count,singles left as char)
s = input("enter a string: ")
res = []
i = 0
n = len(s)
while i< n:
    ch = s[i]
    cnt = 1
    while i+1<n and s[i+1] == ch:
        cnt+=1
        i+=1
    if cnt>1:
            res.append(ch+str(cnt))
    else:
        res.append(ch)
        i+=1
        print(''.join(res))
