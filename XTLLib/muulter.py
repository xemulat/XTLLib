from time import sleep

def muulter(org, file1, name1, namez1, fname1, 
                 file2, name2, namez2, fname2,
                 file3, name3, namez3, fname3):
    print("Version:\n"
         f"[1] {name1}\n"
         f"[2] {name2}")
    if name3 and file3 and namez3 and fname3 != False: print(f"[3] {name3}") ; f3 = False
    choose = input("> ")
    if choose == "1": dl(org, file1, fname1, namez1)
    elif choose == "2": dl(org, file2, fname2, namez2)
    elif choose == "3" and f3 == True: dl(org, file3, fname3, namez3)
    else: print("No option named " + choose) ; sleep(3)