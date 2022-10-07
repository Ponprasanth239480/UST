email_id = str(input("enter the mail id to be checked : "))
if "@" in email_id:
    if "." in email_id:
        if (email_id[0]=="@" or email_id[0]=="."):
            print("the mail id is  not correct")
        else:
            print("the mail id is correct")     
    else:
        print("the mail id is not correct")
else:
    print("the mail id is  not correct")



