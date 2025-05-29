while True:
    print("~~Welcome To Online Calculator~~")
    a = int(input("How Many Values You Want to Perform: "))
    b = int(input("Click the Valid Number to Do a Operations 1 - Addition, 2 - Subtracton, 3 - Multiplication, 4 - Division, 5 - Modulus: "))
    lst = []
    match b:
        case 1:
            for i in range(a):
                num = int(input(f"Enter a {i}th Number: "))
                lst.append(num)

            sum1 = 0
            for j in range(a):
                sum1 += lst[j]
            print("Addition of Numbers is: ",sum1)
            
        case 2:
            for i in range(a):
                num = int(input(f"Enter a {i}th Number: "))
                lst.append(num)
                

            sum1 = 0
            sum2 = lst[0]
            for j in range(1,a):
                sum1 = lst[0]
                sum2 -= lst[j]
            print("Subtraction of Numbers is: ",sum2)

        case 3:
            for i in range(a):
                num = int(input(f"Enter a {i}th Number: "))
                lst.append(num)
                

            sum1 = 1
            for j in range(a):
                sum1 *= lst[j]
            print("Multiplication of Numbers is: ",sum1)

        case 4:
            for i in range(a):
                num = int(input(f"Enter a {i}th Number: "))
                lst.append(num)
                
            sum1 = 0
            sum2 = lst[0]
            for j in range(1,a):
                sum1 = lst[0]
                sum2 /= lst[j]
            print("Division of Numbers is: ",sum2)

        case 5:
            for i in range(a):
                num = int(input(f"Enter a {i}th Number: "))
                lst.append(num)
                
            sum1 = 0
            sum2 = lst[0]
            for j in range(1,a):
                sum1 = lst[0]
                sum2 %= lst[j]
            print("Modulus of Numbers is: ",sum2)
            

        

                          
                
                
            
    
