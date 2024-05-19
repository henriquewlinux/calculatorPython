from calculator import Calculator

def main():
    while True:
        print("Options:")
        print("Type '1' to add two numbers")
        print("Type '2' to subtract two numbers")
        print("Type '3' to multiply two numbers")
        print("Type '4' to divide two numbers")
        print("Type 'exit' to exit the progrm")
        
        option = input("Type the operation you want to perform: ")

        if option == "exit":
            print("Exiting the program...")
            break
        if option in ('1', '2', '3', '4'):
            num1 = int(input("Type the first number: "))
            num2 = int(input("Type the second number: "))
            print(' ')

            if option == '1':
                print("Result: {}".format(Calculator.add(num1, num2)))
            elif option == '2':
                print("Result: {}".format(Calculator.subtract(num1, num2)))
            elif option == '3':
                print("Result: {}".format(Calculator.multiply(num1, num2)))
            elif option == '4':
                Result = Calculator.divide(num1, num2)
                print("Result: {}".format(Result))
            print(' ')
            print(' ')
        else:
            print(' ')
            print("Invalid option! Try again.")
            print(' ')

if __name__ == "__main__":
    main()