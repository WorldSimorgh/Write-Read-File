import sys
print("Warning:This program does not support some formats and it is likely that the program will be closed by entering these formats.")
class Read:
    def Read(Read,Read1):
        while True:
            Read=input("Enter the address of your text file:")
            Read1=open(Read)
            Read.encode("utf8")
            #Error checking:
            '''If the user enters the data correctly, the program will skip this command and continue to work, 
            otherwise a text will appear for the user and the whole program will be stopped.'''
            try:
                Read1=open(Read,"r")
            except:
                 print("Error:There is no such directory:",Read)
                 continue
            print("Your file is being read....\n",Read1.read(),"\nYour file has been read")
            for re in Read:
                #Warning:
                'Do not move the following code as much as possible'
                if re==Read1 or re!=Read:
                    re=input("Do you want to close the program?:(y/n)")
                if re=="y":
                    break
                elif re=="n":
                    sys.exit(0)
    Read("Read","Read1")