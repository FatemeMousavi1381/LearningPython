# National Code Validator

A simple Python script to validate Iranian national codes (10-digit ID numbers).  
It checks that the input is numeric, exactly 10 digits long,  
rejects codes with all repeated digits (like 1111111111),  
and verifies the code using the official checksum algorithm.

## How to use

1. Run the script by typing in terminal:  
   ```bash
   python national-code-validator.py
   ```
2. Enter your 10-digit national code when asked.  
3. The program will tell you if your code is valid or not.  
4. You can try again if you want.

## Features

- Input validation (only numbers, length check)  
- Reject repeated-digit codes  
- Uses official Iranian national code validation logic  
- Easy to use with retry option
