# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 18705762

# Date: 07-12-2021

#Part 3 - List/Tuple/Directory
Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
Pro = []
Tra = []
Ret = []
Exc = []

def progression(passcredit,defercredit,failcredit,Progress,Trailer,Retriever,Excluded):
  #Progress
  if(passcredit==120):
        print("Progress")
        Pro.append([passcredit, defercredit, failcredit])
        return 1
      
  #Progress (module trailer)
  elif (passcredit==100 and (defercredit==20 or failcredit==20)) :
        print("Progress (module trailer)")
        Tra.append([passcredit, defercredit, failcredit])
        return 2
      
  #Do not progress – module retriever
  elif (failcredit<80) :
        print("Do not progress – module retriever")
        Ret.append([passcredit, defercredit, failcredit])
        return 3
      
  #Exclude
  elif (failcredit>60) :
        print("Exclude")
        Exc.append([passcredit, defercredit, failcredit])
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

                      #Vertical Histogram
                      #Reference to Vertical Histogram
                      #https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops#:~:text=You%20can%20use,Improve%20this%20answer

                      print("Vertical Histogram")
                      print("Progress",Progress, "|" , "Trailier",Trailer, "|", "Retriever",Retriever, "|", "Excluded",Excluded, "|")
                      for i in range(max(Progress, Trailer, Retriever, Excluded)):
                          print("  {0}            {1}            {2}              {3} ".format(
                              '*' if i < Progress else ' ',
                              '*' if i < Trailer else ' ',
                              '*' if i < Retriever else ' ',
                              '*' if i < Excluded else ' '
                          ))
                      
                      print("------------------------")
                      for i in range (Progress):
                         print("Progress :",Pro[i])
                      for i in range (Trailer):
                         print("Progress (module trailer) :",Tra[i])
                      for i in range (Retriever):
                         print("module retriever :",Ret[i])
                      for i in range (Excluded):
                         print("Exclude :",Exc[i])
                      
                  elif(continu=="y"):
                      chance=1
                  else :
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

