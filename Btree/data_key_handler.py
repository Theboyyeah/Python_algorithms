class DataHandler:
    def __init__(self,key: int,data =None):
        self.ID = key
        self.DATA = data
    def __repr__(self):
        return f"Key::\t  == \t {self.ID}  Data assigned to the key ::: \t  == \t {self.DATA}\n"
    def __eq__(self,other):
        return self.ID == other.ID
    def __lt__(self, other):
        return self.ID < other.ID

