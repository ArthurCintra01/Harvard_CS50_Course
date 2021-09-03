#decorator announce recebe uma funcao e modifica nesse caso printando antes de depois da funcao
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

#adicionando o decorator announce a uma funcao 
@announce
def hello():
    print("Hello world")