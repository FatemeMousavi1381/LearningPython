import getpass
import re

def check (user_name , password , birthday_date = None) : 
    failed_reasons = []
    strengths_reasons = []
    max_score = 7 
    score = 0
    substitutions = str.maketrans({'a':'@','i':'!','s':'$','o':'0'})
    comm_password = ["11111111" ,"12345678" ,"87654321" ,"123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin"]

    if len(password) > 8 :
        strengths_reasons.append("Password length is sufficient.")
        score += 1
    else : 
        failed_reasons.append("Password length is 8 characters or less.")
                                 
    if (re.search(r"[a-z]" , password )
    and re.search(r"[A-Z]" , password )
    and re.search(r"[!@#$%^&*<>,.;:'+=_]" , password)) : 
        strengths_reasons.append("Includes lowercase, uppercase, and special characters.")
        score += 1
    else :
        failed_reasons.append("Password must include at least \n one lowercase letter, one uppercase letter, \n and one special character(!,@,#,$,...).")
    
    if password != user_name : 
        strengths_reasons.append("Password is different from username.")
        score += 1
    else :
        failed_reasons.append("Password is identical to the username.")

    if not (password.islower() or password.isupper()) : 
        strengths_reasons.append("Contains a mix of uppercase and lowercase letters.")
        score += 1
    else : 
        failed_reasons.append("Password is all lowercase or all uppercase.")

    if password != user_name.swapcase() : 
        strengths_reasons.append("Password is not the swapcase version of the username.")
        score += 1
    else :
        failed_reasons.append("Password is the swapcase version of the username.")

    if password != user_name.translate(substitutions) : 
        strengths_reasons.append("Password is not username with character substitutions.")
        score += 1
    else :
        failed_reasons.append("Password is the username with character substitutions.")

    if password.lower () not in comm_password : 
        strengths_reasons.append("Password is not a common password.")
        score += 1
    else : 
        failed_reasons.append("Password is in the list of common passwords.")

    if birthday_date :
        max_score += 1
        if birthday_date not in password : 
            strengths_reasons.append("Does not include birth year.")
            score += 1
        else : 
            failed_reasons.append("Password includes the user's birth year.")

    return max_score , score , strengths_reasons , failed_reasons

while True : 

    user_name = input("Please enter your username :")
    password = getpass.getpass("Please enter your password :")
    birthday_date = input("Please enter birth year (optional) :")
    birthday_date = birthday_date if birthday_date.strip() != "" else None

    max_score,score,strengths,failed = check(user_name,password,birthday_date)

    if score <= max_score // 4 :
        level = "Very Week !!!"
    elif score <= 2 * (max_score // 4) :
        level = "Week !!!" 
    elif score <= 3 * (max_score // 4) : 
        level = "Medium :|"
    else : 
        level = "Strong :D"


    print("\n--- Password Strength Check ---")
    print(f"Score: {score} out of {max_score}")
    print("Security Level:", level)

    if failed:
        print("\nReasons for failing filters:")
        for reason in failed:
            print("-", reason)

    if strengths:
        print("\nPassword Strengths:")
        for s in strengths:
            print("-", s)

   again = input("Do you want to try again? 1:yes / 0:No : ").strip()
    if again == "0":
        break
    elif again != "1":
        print("Invalid input! Please enter 1 or 0 only.")

        
