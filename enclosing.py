message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print("Enclosing message " + message)
    local()
    print("Enclosing message " + message)

print("Global message " + message)
enclosing()
print("Global message " + message)