import sys
import time
class write:
    def write():
        while True:
            write1=input("Enter your text:\n")
            save=input("Enter the name of the file you want to save: ")
            write=open(save,"a")
            write.write(write1)
            for wr in save:
                #Warning:
                'Do not move the following code as much as possible'
                if wr!=write1 :
                    wr=input("Do you want to close the program?:(y/n)")
                if wr=="y":
                     print("Saving completed successfully",save)
                     break
                elif wr=="n":
                    print("Saving completed successfully",save)
                    time.sleep(2)
                    sys.exit(0)
    write()