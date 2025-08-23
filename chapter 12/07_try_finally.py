def main():
    try:
        a = int(input("Enter your number : "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I am inside finally! ")


main()        