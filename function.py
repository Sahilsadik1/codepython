def user_input():
        servername =input("Enter name of the server:")
        dbname= input("Enter name of the database:")
        username=input("Enter your username:")
        password=input("enter your password:")
        a="servername="+servername+";"+"dbname="+dbname+";"+"username="+username+";"+"password="+password
        return a
data=user_input()
print(data)
                       
        
