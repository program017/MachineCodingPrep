class User(object):
    def __init__(self):
        self.Id = None
        self.name = None
        
    def setId(self, Id):
        self.Id = Id
        
    def getId(self):
        return self.Id
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
        
