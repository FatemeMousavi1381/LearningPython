# Password Strength Checker

A simple Python script to check the strength of a user's password.  
It evaluates passwords based on 7 security filters (8 if birth year is included),  
calculates a score from 1 to 7 (or 8), gives a security level,  
and shows reasons for failing filters and password strengths.

## How to Use
1. Run the script in your terminal:  
```bash
python password-checker.py
```
2. Enter your username and password when asked.  
3. Optionally, enter your birth year to enable an extra security check.  
4. The program will display:  
   - Your password score  
   - Security level (Very Weak, Weak, Medium, Very Strong)  
   - Reasons for failing filters  
   - Password strengths  
5. You can try again with a new password if you want.

## Features
- Checks password length  
- Ensures a mix of lowercase, uppercase, and special characters  
- Prevents using username, swapcase, or character-substituted versions  
- Detects common passwords  
- Optional birth year check  
- Provides score, security level, reasons for failing, and strengths  
- Easy to use with retry option
