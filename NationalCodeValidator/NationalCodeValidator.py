def valid_national_code (code) : 
    
    if code == code[0] * len(code) : 
        return False
    
    Check_national_code = int(code[9])
    Algoritm = sum(int(code[i]) * (10 - i) for i in range(9))
    national_code = Algoritm % 11
    
    if national_code < 2 :
        return Check_national_code == national_code
    else : 
        return Check_national_code == (11 - national_code)
      
def run() : 
    while True : 
        
        code = input('Please enter your national code :')

        if not code.isdigit() : 
            print('Invalid input !!! Please enter numbers only.')
        
        elif len(code) != 10 :
            print('Nationalcode must be exactly 10 numbers.')

        elif not valid_national_code(code) : 
            print('Invalid nationalcode !!!')
        
        else : 
            print ('The nationalcode is valid :)')
        break

    while True : 
        retry = input ('Do you want to try again ? (1 = yes / 0 = no) :')
        if retry == "1" : 
         return run()

        elif retry == "0" :
            print ('Goodbye.')
            exit()

        else : 
            print('Invalid choice !!!Please enter 1 0r 0.')

run()