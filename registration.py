def register():
    db = open("user_detail.txt", "r")
    a = input("Create your username in format __@__.__: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])
    #if email already exists say to login by entering password
     if a in d:
        print("user name already exists,Try login")
        register()
     #username format: it should begin with special char but can contain special char and not necessary to have digits and uppercase.
    #when it satisfies the above username is created and added to the text file named user_detail
    
     elif a.count('@') != 1 and a.count('.') != 1:
        print("enter username in proper format")
        register()
     elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Start with only characters")
        register()
     else:
        print("Username created")
 #password format: must include atleast 1 digit,1 uppercase and 1 special char and length should not exceed 15 char
 b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    if len(b) < 5 and len(b) > 16:
        print("Create Password with length between 5 an 16, Try Again")
        register()
#when it passes the first condition checks the remaining  includes number,uppercase & special char,initialized to zero
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
#when password is entered in correct format,user is registered successfully
    if s:
        c = input("Confirm Password: ")
        print("user registered successfully")
        while (c != b):
            print("Password not match, Try Again")
            c = input("Try Again: ")  
     
