class DataHandler:
    '''
    Class DataHandler represents a connection between data and key

    Attributes:
        ID = our key assigned to the data
        DATA = Files, strings or is considered Data for you
    Methods:
        def __init__ - creating object DataHandler with key and/or data
        def __repr__ - how the node is represented ,it will print key its key and assignet to it data
        def __eq__ - allows comparison for equality based on ID (key)
        def __lt__ - allows comparison for ordering based on ID (key)
        -

    '''
    def __init__(self,key: int,data =None):
        self.ID = key
        self.DATA = data
        self.debug_mode = True
    def __repr__(self):
        return f"Key::\t  == \t {self.ID}  Data assigned to the key ::: \t  == \t {self.DATA}\n"
    def __eq__(self,other):
        return self.ID == other.ID
    def __lt__(self, other):
        return self.ID < other.ID

