name = input("Enter name:")
print("(H)ello \n(G)oodbye \n(Q)uit") #display menu
choice = input() #get choice
while choice != "Q":
   if choice == "H":
       print("hello",name) #display "hello" name
       print("(H)ello \n(G)oodbye \n(Q)uit")  # display menu
       choice = input()  # get choice
   elif choice == "G":
       print("goodbye",name) #display "goodbye" name
       print("(H)ello \n(G)oodbye \n(Q)uit")  # display menu
       choice = input()  # get choice
   else:
       print("Invalid choice") #display invalid message
       print("(H)ello \n(G)oodbye \n(Q)uit")  # display menu
       choice = input()  # get choice
print("Finished.")#display finished message