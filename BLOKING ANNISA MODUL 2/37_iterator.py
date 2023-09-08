class MyNumbers:
    def __iter__(self):
        x = self.a
        self.a += 1
        return x
    
    myclass = ()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))