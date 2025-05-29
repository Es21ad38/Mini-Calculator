while True:
    print("~~Welcome To Online Calculator~~")
    print()
    a = int(input("How Many Values You Want to Perform: "))
    print()
    b = int(input("Click the Valid Number to Do a Operations 1 - Addition, 2 - Subtracton, 3 - Multiplication, 4 - Division, 5 - Modulus: "))
    print()
    lst = []
    if (a>=2):
        match b:
                case 1:
                    for i in range(a):
                        num = int(input(f"Enter a {i}th Number: "))
                        lst.append(num)

                    temp1 = 0
                    for j in range(a):
                        temp1 += lst[j]
                        print()
                    print("Addition of Numbers is: ",temp1)
                    print()
                    
                case 2:
                    for i in range(a):
                        num = int(input(f"Enter a {i}th Number: "))
                        lst.append(num)
                        

                    temp1 = 0
                    temp2 = lst[0]
                    for j in range(1,a):
                        temp1 = lst[0]
                        temp2 -= lst[j]
                        print()
                    print("Subtraction of Numbers is: ",temp2)

                case 3:
                    for i in range(a):
                        num = int(input(f"Enter a {i}th Number: "))
                        lst.append(num)
                        

                    temp1 = 1
                    for j in range(a):
                        temp1 *= lst[j]
                        print()
                    print("Multiplication of Numbers is: ",temp1)
                    print()

                case 4:
                    for i in range(a):
                        num = int(input(f"Enter a {i}th Number: "))
                        lst.append(num)
                        
                    temp1 = 0
                    temp2 = lst[0]
                    for j in range(1,a):
                        temp1 = lst[0]
                        temp2 /= lst[j]
                        print()
                    print("Division of Numbers is: ",temp2)
                    print()

                case 5:
                    for i in range(a):
                        num = int(input(f"Enter a {i}th Number: "))
                        lst.append(num)
                        
                    temp1 = 0
                    temp2 = lst[0]
                    for j in range(1,a):
                        temp1 = lst[0]
                        temp2 %= lst[j]
                        print()
                    print("Modulus of Numbers is: ",temp2)
                    print()
                    
                case _:
                    print()
                    print("Enter a Valid Input to Perform a Operation")
                    print()
    else:
        print()
        print("Enter a Minimum of 2 Values to Perform the Operations! ")
        print()

        

                          
                
                
            
    
