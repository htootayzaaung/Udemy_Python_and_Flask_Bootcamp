def new_decorator(func):

    def wrap_func():
        print("some code before executing func")

        func()

        print("some code here after executing func")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!")

func_needs_decorator()
