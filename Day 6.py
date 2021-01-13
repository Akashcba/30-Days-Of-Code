
def odd_even(a):
    odd = ""; even =""
    for i in range(len(a)):
        if i%2==0:
            even = even + a[i]
        else :
            odd += a[i]
    return str(even)+" "+str(odd)



def main():
    t =int(input())
    while(t>0):
        t-=1
        s = input().split(" ")[0]
        print(odd_even(s))


if __name__ == "__main__":
    main()
