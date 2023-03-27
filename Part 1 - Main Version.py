# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 18705762

# Date: 07-12-2021


Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0

#Choose whether Student ver or Staff ver

print("If Student version, please enter 1")
print("If Staff version, please enter 2")
print("   ")
ver= str(input("Student version or Staff ver - "))
print("   ")
#If Student version
if (ver == "1"):
    Progress = 0
    Trailer = 0
    Retriever = 0
    Excluded = 0

    #Functions
    def progression(passcredit,defercredit,failcredit):
      #Progress
      if(passcredit==120):
            print("Progress")
          
      #Progress (module trailer)
      elif (passcredit==100 and (defercredit==20 or failcredit==20)) :
            print("Progress (module trailer)")
          
      #Do not progress – module retriever
      elif (failcredit<80) :
            print("Do not progress – module retriever")
          
      #Exclude
      elif (failcredit>60) :
            print("Exclude")

            
    #Validation
    try:
        passcredit = int(input("Enter your total PASS credits:"))
        if passcredit in [20*i for i in range(7)] :
          defercredit = int(input("Enter your total DEFER credits:"))
          if defercredit in [20*i for i in range(7)] :
              failcredit = int(input("Enter your total FAIL credits:"))
              if failcredit in [20*i for i in range(7)] :
                  if passcredit+defercredit+failcredit==120 :
                      num=progression(passcredit, defercredit, failcredit)
                  else :
                      print("Total incorrect")
              else :
                 print("Out Of range")
          else :
              print("Out of range")
        else :
          print("Out of range")

    except ValueError:
     print("Integer required")
    except NameError:
        print("")
        
#If Staff version
#Multiple outcomes and Histogram will be displayed
elif(ver == "2"):

    print("Staff Version with Histograms ")
    print("  ")
    Progress = 0
    Trailer = 0
    Retriever = 0
    Excluded = 0

    def progression(passcredit,defercredit,failcredit,Progress,Trailer,Retriever,Excluded):
      #Progress
      if(passcredit==120):
            print("Progress")
            
            return 1
          
      #Progress (module trailer)
      elif (passcredit==100 and (defercredit==20 or failcredit==20)) :
            print("Progress (module trailer)")
            
            return 2
          
      #Do not progress – module retriever
      elif (failcredit<80) :
            print("Module retriever")
            
            return 3
          
      #Exclude
      elif (failcredit>60) :
            print("Exclude")
            
            return 4

    try:
     chance = 0
     while chance<2:

      passcredit = int(input("Enter your total PASS credits:"))
      if passcredit in [20*i for i in range(7)] :
          defercredit = int(input("Enter your total DEFER credits:"))
          if defercredit in [20*i for i in range(7)] :
              failcredit = int(input("Enter your total FAIL credits:"))
              if failcredit in [20*i for i in range(7)] :
                  if passcredit+defercredit+failcredit==120 :
                      outcome=progression(passcredit, defercredit, failcredit ,Progress,Trailer,Retriever,Excluded)
                      if(outcome == 1) :
                          Progress += 1
                          
                      elif(outcome == 2) :
                          Trailer += 1
                          
                      elif (outcome == 3):
                          Retriever+=1
                          
                      elif (outcome == 4):
                          Excluded += 1

                      print ("  ")    
                      print("Would you like to enter another set of data?")
                      continu = input("Enter 'y' for yes or 'q' to quit and view results: ")
                      print ("  ")

                   #Histogram
                      #Horizontal Histogram
                      if(continu=="q") :
                          chance=2
                          print("------------------------")
                          print("Horizontal Histogram")
                          print("Progress ",Progress, " :",end=" ")
                          for i in range(0,Progress):
                              print("*",end=" ")
                          print("")
                          print("Trailer  ", Trailer, " :",end=" ")
                          for i in range(0, Trailer):
                              print("*", end=" ")
                          print("")
                          print("Retriever", Retriever, " :",end=" ")
                          for i in range(0, Retriever):
                              print("*", end=" ")
                          print("")
                          print("Excluded ", Excluded, " :",end=" ")
                          for i in range(0, Excluded):
                              print("*", end=" ")
                          print("")
                          print("     ")
                          print (Progress + Trailer + Retriever + Excluded, "outcomes in total.")
                          print ("  ")
                          
                          print("------------------------")
                          
                          
                                               
                      elif(continu=="y"):
                        #To while loop to continue
                          chance=1
                      else :
                        #If other than 'y' or 'q' entered, program will end
                        print ("Only enter 'y' or 'q' ")
                        break
                  else :
                      print("Total incorrect")
              else :
                 print("Out Of range")
          else :
              print("Out of range")
      else :
          print("Out of range")

    except ValueError:
     print("Integer required")
     
    except NameError:
        print("")
else :
  #If other than '1' or '2' entered, program will end
  print ("Only enter '1' or '2' ")

                        
