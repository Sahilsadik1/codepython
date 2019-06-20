def user_input():
        servername =input("Enter name of the server:")
        dbname= input("Enter name of the database:")
        username=input("Enter your username:")
        password=input("enter your password:")
        a="servername="+servername+";"+"dbname="+dbname+";"+"username="+username+";"+"password="+password
        return a
data=user_input()
print(data)
                       
        
OR 
def user_input():
        servername =input("Enter name of the server:")
        dbname= input("Enter name of the database:")
        username=input("Enter your username:")
        password=input("enter your password:")
                    
        return servername,dbname,username,password
def main():
               servername,dbname,username,password=user_input()
               s,d,u,p=(servername,dbname,username,password)
               print("The string names are:",s,d,u,p)
               return s,d,u,p
main()             
