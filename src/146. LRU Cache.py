class LRUCache:

    def __init__(self, capacity: int):
        self.odict=collections.OrderedDict()
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key in self.odict:
            value=self.odict[key]
            self.odict.pop(key)
            self.odict[key]=value
           # print("get",self.odict)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #print(self.odict)
        if key in self.odict:
            self.odict.pop(key)
            self.odict[key]=value
            #print(self.odict)
            #print("modify")
            return
        
        if len(self.odict)<self.capacity:
            self.odict[key]=value
        elif len(self.odict)>=self.capacity:
            self.odict.popitem(last=False)
            self.odict[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
