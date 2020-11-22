def check(x):
    sym=["!",'@','#','$','%','&','*']
    alpha=[str(x) for x in range(1,10)]
    scount=0
    count=0
    if 14<len(x) or len(x)<7:
        return "Weak"
    else:
        for i in x:
            if count==2 and scount==2:
                break
            if not count==2:
                if i in sym :
                    count+=1
            if not scount == 2:
                if i in alpha :
                    scount+=1
    if count==2 and scount==2:
        return "Strong"
    else:
        return "Weak"
stri=input("give string")
print(check(stri))