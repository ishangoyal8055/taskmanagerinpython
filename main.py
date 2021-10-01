print("Task Manager")
choice=1
listoftask=[]
while(choice!=4):
    choice=int(input("Enter \n 1 Enter a task in task manager. \n 2 Display Task manager. \n 3 Remove item from task manager. \n 4 Exit "))
    if choice==1:
        a=input("\nEnter the task you want to add in task manager : ")
        if a in listoftask:
           print("\nYou already added that task in your task manager.")
        else:
           listoftask.append(a)
           print("\nYour task added in Your task manager")
    elif choice==2:
        if(len(listoftask)==0):
            print("\nYour Task Manager is Empty")
        else:
            for i in listoftask:
                print(i)
    elif choice==3:
        if(len(listoftask)==0):
            print("\nThere is no item in task manager to remove.")
        else:
            item=input("\nEnter item you want to remove : ")
            if item not in listoftask:
                print("\nItem You Entered is not in the Task Manager.")
            else:
                listoftask.remove(item)
                print("\nItem Removed Successfully.")
    elif choice==4:
        choice=4
    else: 
        print("\nEnter a Valid Choice")
