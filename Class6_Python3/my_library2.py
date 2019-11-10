def hello():
    print("hello")

def beautiful_day(text):
    return "Hello "+text+". It is a beautiful day!"


print("__name__ =",__name__)
if __name__=="__main__":
    # not executed when importing

    hello()
    print("Some code")
    print(beautiful_day("Thomas"))