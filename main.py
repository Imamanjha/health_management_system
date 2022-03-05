#health management system for harry,rohan and hammad
while(True):
    def time():
        import datetime
        return datetime.datetime.now()
    print("enter your desired serial number\n1.Lock data\n2.Retrieve data")
    while (True):
        a = int(input())
        if a != 1 and a != 2:
            print("you have entered an incorrect number")
            continue
        else:
            break
    if a==1:
        print("enter the serial number of person whose data you want to lock\n1. Harry\n2. Rohan\n3. Hammad")
        while(True):
            b = int(input())
            if b !=1 and b !=2 and b != 3:
                print("you have entered an incorrect number")
                continue
            else:
                break

        print("enter the serial number of data type you want to lock\n1. Diet\n2. Exercise")
        while (True):
            c = int(input())
            if c != 1 and c != 2:
                print("you have entered an incorrect number")
                continue
            else:
                break
        c=int(input())
        if b==1:#opens harry
            if c==1:#opens harry diet
                with open("harry-diet.txt","a") as f1:
                    print("enter what diet harry took")
                    f1.write(str(time()))
                    f1.write("  ")
                    f1.write(input())
                    f1.write("\n")
            elif c==2:#opens harry exercise
                with open("harry-exercise.txt","a") as f2:
                    print("enter what exercise harry performed")
                    f2.write(str(time()))
                    f2.write("  ")
                    f2.write(input())
                    f2.write("\n")
        if b==2:#opens rohan
            if c==1:#opens rohan diet
                with open("rohan-diet.txt","a") as f3:
                    print("enter what diet rohan took")
                    f3.write(str(time()))
                    f3.write("  ")
                    f3.write(input())
                    f3.write("\n")
            elif c==2:#opens rohan exercise
                with open("rohan-exercise.txt","a") as f4:
                    print("enter what exercise rohan performed")
                    f4.write(str(time()))
                    f4.write("  ")
                    f4.write(input())
                    f4.write("\n")
        if b==3:#opens hammad
            if c==1:#opens hammad diet
                with open("hammad-diet.txt","a") as f5:
                    print("enter what diet hammad took")
                    f5.write(str(time()))
                    f5.write("  ")
                    f5.write(input())
                    f5.write("\n")
            elif c==2:#opens hammad exercise
                with open("hammad-exercise.txt","a") as f6:
                    print("enter what exercise hammad performed")
                    f6.write(str(time()))
                    f6.write("  ")
                    f6.write(input())
                    f6.write("\n")
    if a==2:
        print("enter the serial number of person whose data you want to retrieve\n1. Harry\n2. Rohan\n3. Hammad")
        while (True):
            b = int(input())
            if b != 1 and b != 2 and b != 3:
                print("you have entered an incorrect number")
                continue
            else:
                break
        print("enter the serial number of data type you want to retrieve\n1. Diet\n2. Exercise")
        while (True):
            c = int(input())
            if c != 1 and c != 2:
                print("you have entered an incorrect number")
                continue
            else:
                break
        if b==1:#opens harry data
            if c==1:#opens harry diet data
                with open("harry-diet.txt","r") as f1:
                    print(f1.read())
            elif c==2:#opens harry exercise data
                with open("harry-exercise.txt","r") as f2:
                    print(f2.read())
        if b==2:#opens rohan data
            if c==1:#opens rohan diet data
                with open("rohan-diet.txt","r") as f3:
                    print(f3.read())
            elif c==2:#opens rohan exercise data
                with open("rohan-exercise.txt","r") as f4:
                    print(f4.read())
        if b==3:#opens hammad
            if c==1:#opens hammad diet
                with open("hammad-diet.txt","r") as f5:
                    print(f5.read())
            elif c==2:#opens hammad exercise
                with open("hammad-exercise.txt","r") as f6:
                    print(f6.read())
    print("Do you want to retrieve or lock other data\npress\n1 for yes\n2 for no")
    while (True):
        d = int(input())
        if d != 1 and d != 2:
            print("you have entered an incorrect number")
            continue
        else:
            break
    if d==1:
        continue
    elif d==2:
        exit()
