TYPO=input("Would u like to use list, dictionary or loop ")
if TYPO=="loop":
    print("Polygon area calculator")
    number = int(input("How many sides does the polygon have? "))
    if number < 3:
        print ("Area of a 1D figure is non existant")
    elif number == 3:
        print("Triangle Area Calculator")
        a =[1,2,3]
        m=0
        for y in range(3):
            m=m+1
            print ("Enter Side number ",m);a[y] = int(input())
        s=(a[0]+a[1]+a[2])/2
        if a[0]+a[1]<=a[2] or a[0]+a[2]<=a[1] or a[2]+a[1]<=a[0]:   #Finds if triangle is even possible by checking if sum of 2 sides is less than 3rd side
            print("This Triangle Is Not Possible")
        else:
            x=((s-a[0])*(s-a[1])*(s-a[2])*s)**0.5     #Finds Area of Triangle through herons formula
            print("Area of triangle is ", x)
    elif number == 4:
        print ("Quadrilateral area Calculator")
        quadrilateral_type = str(input("What is the type of quadrilateral?(square/rectangle/rhombus/kite/trapezium/not defined) "))
        #uses looping and logical operators to allot the correct formula for each shape 
        if quadrilateral_type == "square":
            x=int(input("Enter side "))
            print ("Area =",x**2)
        elif quadrilateral_type == "rectangle":
            x=int(input("Enter lenght "))
            y=int(input("Enter Breadth "))
            print ("Area =",x*y)
        elif quadrilateral_type=="rhombus":
            x=int(input("Enter Diagonal 1 "))
            y=int(input("Enter Diagonal 2 "))
            ar=(x*y)/2
            print ("Area =",ar)
        elif quadrilateral_type=='kite':
            x=int(input("Enter Diagonal 1 "))
            y=int(input("Enter Diagonal 2 "))
            ar=(x*y)/2
            print ("Area =",ar)
        elif quadrilateral_type=='trapezium':
            x=int(input("Enter parallel side 1 "))
            y=int(input("Enter parallel side 2 "))
            h=int(input("Enter distance between parallel sides "))
            ar=0.5*x*y*h
            print ("Area =",ar)
elif TYPO=="list":
    list_1=list(input("Please Enter the List to be Manipulated (without space, without enter)  "))
    cont="y"
    while cont=="y":
        print("Please Enter the What you would like to do? ")
        type_1=str(input("Options- length, retrieve,existence check,change,insert,list combiner,deleter or sorter "))
        if type_1=="length" :
            x=len(list_1)
            print ("Lenght of the entered list is ",x)
        elif type_1=="retrieve" :
            print("You have chosen retrieve function ")
            x=str(input("Would u like to use positive or negative indexing "))
            if x=="positive" :
                y=int(input("Please enter the index of the value to be retrived "))
                print ("The requested value is ", list_1[y])
            elif x=="negative" :
                y=int(input("Please enter the negative index of the value to be retrived "))
                print ("The requested value is ", list_1[y])
        elif type_1=="existence check":
            x=input("Enter the value to be checked ")
            if x in list_1:
                print("Yes,",x,"does exist in this list")
            else:
                print("No,",x,"does not exist in this list")
        elif type_1=="change":
            x=int(input("Enter the index of value to be changed "))
            y=input("Enter new value ")
            list_1[x]=y
            print("Altered List is ")
            print(list_1)
        elif type_1=="insert":
            x=str(input("Would u like to specify the position of inserted value?(y/n)"))
            if x=="y":
                y=input("Enter Value to be inserted ")
                z=int(input("Enter the Index at value is to be inserted "))
                list_1.insert(z,y)
                print("Altered List is ")
                print(list_1)
            else:
                y=input("Enter Value to be inserted ")
                list_1.append(y)
                print("Altered List is ")
                print(list_1)
        elif type_1=="list combiner":
            x=list(input("Enter the list to be added on to the original list "))
            list_1.extend(x)
            print("Altered List is ")
            print(list_1)
        elif type_1=="deleter":
            x=str(input("Would you like to delete based on index or value? "))
            if x=="index":
                y=int(input("Enter the Index whose corresponding value has to be deleted "))
                list_1.pop(y)
            else:
                y=input("Enter the value to be deleted from the list ")
                list_1.remove(y)
            print("Altered List is ")
            print(list_1)        
        elif type_1=="sorter":
            x=input("Would u like your list to be sorted ascending or descending? ") 
            if x=="ascending":
                list_1.sort()
            else:
                list_1.sort(reverse=True)
            print("Altered List is ")
            print(list_1)
        else:
            print("Spelling Mistake, please try again  ")   
        cont=str(input("Would u like to continue?(y/n) "))
elif TYPO=="dictionary":
    print("Enter a dictionary with word and meanings ")
    n= int(input ( "How many items in Dicitonary "))
    fd= {}
    for i in range(n) :
        print ("Enter the pair", (i+1) )
        name = input ("Word: ")
        ph = input("Meaning: ")
        fd[name] = ph
    print("Entered Dictionary is", fd)
    cont="y"
    while cont=="y":
        print("What Would u like to do with the dicitonary? ")
        c=input("length, clear, get, delete ")
        if c=="length" :
            x=len(fd)
            print("Length of dictionary is ",x)
        elif c=="clear":
            fd.clear()
            print("Your dcitionary has been cleared")
        elif c=="get":
            b=input("Enter Key to be retrieved ")
            x=fd.get(b)
            print("Requied Value is ",x)
        elif c=="delete":
            b=input("Enter the key of the pair to be deleted ")
            del fd[b]
            print("Edited dictionary is ",fd)
        cont=str(input("Would u like to continue?(y/n) "))
        
        
        
    