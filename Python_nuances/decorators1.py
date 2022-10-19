def hello(name = "Jose"):
        print("the hello() function has been run")

        def greet():
                return "        This is inside greet()"

        def welcome():
                return "        This is inside welcome()"

        if name == "Jose":
            return greet        #This returns a greet() functio
        else:
            return welcome      #This returns a welcome() function

x = hello()						#x now stores whatever that is returned by hello()
print(x())
print("************************")
y = hello("Aung")
print(y())
