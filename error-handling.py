#a=1
#print(b)


try:
    print(b) #risky code
except:
    print("error")
else:
    print("no error")
finally:
    print("always")


try:
    print('a'+32)
except TypeError:
    print("type error")
except valueError:
    print("ValueError")