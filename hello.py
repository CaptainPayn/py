def hello(func):
    def inner():
        print("Hello ")
        func()
    return inner

@hello
def name():                                                                                                  
    print("Phil")                                                                                          
                                                                                                            
if __name__ == "__main__":                                                                                  
    name() 
