class User:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    
        
a = User('name')

print(a.getName())