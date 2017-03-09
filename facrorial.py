print "Finding out the factorial of a number"

def start():
    number=int(raw_input("Enter the number here:"))
    ans=1
    while number>0:
        ans=ans*number
        number-=1
    print ans
    print "Again??? Y or N"
    ans1=raw_input("")
    if ans1=="Y":
        start()
    else:
        print "End program"

start()
