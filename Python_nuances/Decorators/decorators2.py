def hello():
  return "Hi Jose"

def other(func):                    #a function is passed
    print("Some other code")        #this prints first

    print(func())                   #a function is called

other(hello)                        #a function is passsed 
