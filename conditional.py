#if
#else
#elif
#nested if
if True:
    print("nenu if")
elif True:
    print("nenu elif")
else:
    print("nenu else")



if True:
    print("outer if")
    if False:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")

age=18
if age>18:
    print("you can vote")
elif age==18:
    print("you can vote buddy")
else:
    print("wait")

