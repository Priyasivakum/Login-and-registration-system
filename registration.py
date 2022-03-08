def register():
    db = open("user_detail.txt", "r")
    a = input("Create your username in format __@__.__: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])
     if a in d:
        print("user name already exists,Try login")
        register()
     elif a.count('@') != 1 and a.count('.') != 1:
        print("enter username in proper format")
        register()
     elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Start with only characters")
        register()
     else:
        print("Username created")
 b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    if len(b) < 5 and len(b) > 16:
        print("Create Password with length between 5 an 16, Try Again")
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
     