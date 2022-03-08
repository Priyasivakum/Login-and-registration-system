def login():
    X=input("Enter your username to login: ")
    X = X.strip()
    db = open("user_detail.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])
# checks the file in read mode->if the userid exists and password matches,->"logged in"
    if X in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("user_detail.txt",mode = "r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print("Welcome, logged in successfully!")
            else:
                F = input("Forgot Password [Yes/No] : ")

                if F == "No":
                    print("try")
                    login()

                if F == "Yes":
                    b = input("Create your new password with atleast one capital letter one integer and one special character: ")
                    s = False
#if user forgets password, the same logic is implied which is used for registration, when the entered value satisfies all the conditions,the new password is reset sucessfully
                    if len(b) < 5 and len(b) > 16:
                        print("Create Password with length between 5 and 16, Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                     if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password not match, Try Again")
                            c = input("Try Again: ")

                     else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("user_detail.txt", "w")
                    file.write(X + "," + b + "\n")
                    file.close()

     else:
        print("Unregistered user:To login your account, you need to register first")
        register()
