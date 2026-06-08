class Verify:
    y=1234
    def __init__(self,pin):
        if pin==Verify.y:
            print("access granted")
        else:
            print("access denied")
    
pin=int(input("Enter your pin"))
objverify=Verify(pin)