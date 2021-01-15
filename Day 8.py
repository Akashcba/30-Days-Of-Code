# given n names + phone numbers
# Friends name to phone numbers
# O/P : name=phonenumber
# Not found

d = { }

def main():
    global d
    n=int(input())
    while(n>0):
        n-=1
        t = input().split()
        d[t[0]] = int(t[1])
    try :
        while(True):
            j = input()
            if j in d:
                print(j+"="+str(d[j]))
            else :
                print("Not found")
    except:
        return 0
if __name__ == '__main__':
    main()
