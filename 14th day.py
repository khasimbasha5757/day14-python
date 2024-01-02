#  break and continue
for i in range(1,20):
          print(i)
          if(i==12):
                  break
print("Yes our break statement has really worked")
for i in range(1,10):
          if(i==5):
                  print("We have used continue in this value")
                  continue     
          print(i)
print("Our continue statement has worked but we should keep the if statement before the print statement")   