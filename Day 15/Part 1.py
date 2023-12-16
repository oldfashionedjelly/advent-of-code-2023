codes = open("codes.txt").read().split(',')
total=0
for code in codes:
    temp=0
    for str in code:
        temp+=ord(str)
        temp*=17
        temp%=256
    total+=temp

print(total)