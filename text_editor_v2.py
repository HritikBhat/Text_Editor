"""
    This program works as  a mini text editor .....i made it for my timepass :P

    INSTRUCTION:
        1)If You Are New To This Program Then Read That README File By Using RD In Program.
        2)If you are writing content or editing on an existing txt file, USE <e> OR <E> TO STOP.
        3)IT WILL PRINT THE PRESENT LINE FOR EDITING SO YOU CAN COPY IN ORDER TO EASE USER WORKLOAD.
            (For Editing ('e' option))

    If there is error or advice the user want to give ,feel free to give. :)

"""
import os
from time import sleep
def read_edit(file):
    """
        This function will help user to edit line which exist in middle of
        the paragraph of an existed txt file.To ease user work a bit, the program
        allows to edit more than one lines and IT CAN BE STOPPED BY <e> or <E>.
    """
    if os.path.isfile(file+".txt") is True:
        f1_e = open(file+".txt", "r")
        f2_e = open(file+".txt", "r")
        e_count = 1
        print("\nContent:")
        print("-------------------------------------------------------------------------")
        for e_line in f1_e.readlines():
            print(e_count, ":", e_line, end="")
            e_count = e_count + 1
        print("-------------------------------------------------------------------------")
        f1_e.close()
        text_content = f2_e.readlines()
        edit_start = int(input("Enter the line no to be editted:"))
        i = edit_start-1
        while i < len(text_content):
            print()
            print(text_content[i])
            line = input()
            if line in ("<e>", "<E>"):
                break
            elif line in ("<s>", "<S>", "<S1>", "<s1>"):
                #To add new line on next position
                if line == "<s1>":
                    i = i + 1
                line = input()
                #If <s> it will add on present positon,push older one to next line. 
                text_content.insert(i, line+"\n")
                continue
            #Removes present line
            elif line in ("<r>", "<R>"):
                del text_content[i]
                continue
            #Skips current/present line and goes to next.
            elif ("<sk" in line or "<SK" in line) and len(line) < 10:
                if len(line) > 4:
                    no = int(line[3:len(line)-1])-1
                    i = no
                    continue
                else:
                    i = i + 1
                    continue
            text_content[i] = line +"\n"
            i = i + 1
        f2_e.close()

        f3_e = open(file+".txt", "w")
        f3_e.writelines(text_content)
        f3_e.close()

    else:
        print("\nFile does not exists!\n")

def read_file(file):
    """
        This function reads and display contents of the requested existing txt file.
    """
    if os.path.isfile(file+".txt") is True:
        f4_r = open(file+".txt", "r")
        print("\nContents in the file:\n")
        print("-------------------------------------------------------------------------")
        print(f4_r.read())
        print("-------------------------------------------------------------------------")
        f4_r.close()
    else:
        print("\nFile does not exists!\n")

def write_append_file(op_mode, file):
    """
        This function allows to write or append an already existing file.
    """
    innerflag = False
    text = []
    print("\n")
    while innerflag is False:
        line_extract = input()
        if line_extract in ("<e>", "<E>"):
            break
        text.append(line_extract+"\n")
    f5_wa = open(file+".txt", op_mode)
    f5_wa.writelines(text)
    print()
    f5_wa.close()
FLAG = False
"""
    Main Body Of The Code!!!
"""
while FLAG is False:

    OP = input("Press\n 'RD' for README\n 'r' for read\n 'w' for write\n 'a' for "
               "append \n 'e' for edit\n 'w+' for writing a new file\n 'rm' for deleting a file"
               "\n 'q' for exit:\n")
    #Exits the program
    if OP == "q":
        FLAG = True
        continue
#Reads README File
    elif OP == "RD":
        read_file("README")
        continue
    FILE = input("Enter File Name:")
    #Reading a file
    if OP == "r":
        read_file(FILE)
    #Appending or Writing a file
    elif OP in ("w", "a"):
        write_append_file(OP, FILE)
    #To edit or modify the existed file
    elif OP == "e":
        read_edit(FILE)
    #Creating a new file
    elif OP == "w+":
        F3 = open(FILE+".txt", "w")
        sleep(1)
        print("\nFile Created!\n")
        F3.close()
    #To Remove A File
    elif OP == "rm":
        os.remove(FILE+".txt")
        sleep(1)
        print("\nFile Deleted!!\n")
    #If Exception Occurs...
    else:
        print("Error!Try Again.")
