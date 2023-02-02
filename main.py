from time import*
import hashlib
print('"SEE" for check your passwords and pwd for entering a new password :')
test = input()
if test.upper() == "SEE":
    file = open("password.json","r")
    print(file.read())
    file.close()
elif test.lower() == "pwd":
    pwd = input("set a password : ")
    if len(pwd)>7 and pwd.upper() != pwd and pwd.lower() != pwd and True in [a in [str(b) for b in range(10)] for a in pwd] and True in [["!", "@", "#", "$", "%", "^", "&", "*"][a] in pwd for a in range(8)]:
        print("YES")
    else:
        while True:
            print("you need 8 characters, with an upper and a lower letter, a number and a special charater like : ")
            print(" ! , @ , # , $ , % , ^ , & , * ")
            sleep(1)
            pwd = input("set a password : ")
            if len(pwd)>7 and pwd.upper() != pwd and pwd.lower() != pwd and True in [a in [str(b) for b in range(10)] for a in pwd] and True in [["!", "@", "#", "$", "%", "^", "&", "*"][a] in pwd for a in range(8)]:
                break
    result = hashlib.sha256()
    result.update(eval('b"'+pwd+'"'))
    file = open("password.json","a")
    file.close()
    file = open("password.json","r")
    track = file.read()
    file.close()
    if "password" not in track:
        reset = {"password": []}
    else:
        reset = eval(track)
    if result.hexdigest() not in reset["password"]:
        reset["password"] += [result.hexdigest()]
        reset = str(reset)
        file = open("password.json","w")
        file.write(reset)
        file.close()
    else:
        print("you already added this password")
