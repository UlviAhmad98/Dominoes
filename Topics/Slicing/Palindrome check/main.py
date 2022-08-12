# please work with the preset variable `word`
forward =  word[0:]
backward =  word[::-1]

if forward == backward:
    print("Yes")
else:
    print("No")
