def hello_world():
    print("hello world")

""" I need these lines to be run only if the myfile is run"""
""" each module --> __name__ ='__main__'---> contains main of the module """

if __name__ == '__main__':
    hello_world()
    print("Hello from Ghaza ")

