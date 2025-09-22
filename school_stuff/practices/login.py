# AS 2nd login

uname = input("what would ye like thy username to be")
password = input("what would ye like thy passworde to be")
check_name = input("what was thine username")
check_pass = input("what was thine password")
if uname != check_name or password != check_pass:
    print("wronge")
    while uname != check_name or password != check_pass:
        check_name = input("what was thine username")
        check_pass = input("what was thine password")
        if uname == check_name and password == check_pass:
            print("ye are logged in nowe")
        else:
            print("bad")
elif uname == check_name and password == check_pass:
    print("ye are logged in nowe")
else:
    print("howe did thy do thate")