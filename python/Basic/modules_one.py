## __name__

def hello():
    print("Hello!")


print(__name__)
if __name__ == '__main__':
    hello()
    print("running this module directly")
else:
    print("running other module indirectly")
