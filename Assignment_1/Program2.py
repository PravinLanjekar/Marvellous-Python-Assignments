def ChkNum():
    print("Enter First Number : ")
    No = int(input())
    

    if((No % 2)== 0):
        print("Even Number")
    else:
        print("Odd Number")
        
def main():
    ChkNum()
    
        
if __name__ == '__main__':
    main()
    