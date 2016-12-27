def change(list1,a):
    list1[1]=100
    a=100
    return a,list1
def main():
    a=10
    list1=[1,2,3,4,5]
    data= change(list1,a)
    print data[1]
main()
