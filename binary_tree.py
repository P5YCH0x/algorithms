class leaf:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None

    def addChild(self, val):
        if self.data == val: # checking if we are adding something that's already in the tree.
            return

        if val > self.data: # if number is higher put it on the right.
            if self.right:
                self.right.addChild(val)
            else:
                self.right = leaf(val)
        else:                           # if number is lower it goes on the left.
            if self.left:
                self.left.addChild(val)
            else:
                self.left = leaf(val)

    def search(self, val):
        if self.data == val:
            return True
        
        if val > self.data: # if number is higher and there are more nodes on the right, check those.
            if self.right:
                return self.right.search(val)
            else:
                return False
        elif val < self.data: # check left, if it exists.
            if self.left:
                return self.left.search(val)
            else:
                return False

def Tree_builder(values):
    root = leaf(values[0]) # root node of the tree.

    for i in range(1, len(values)): # adds each node to the root node. starts from 2nd in array because 1st was used as root.
        root.addChild(values[i])
    
    return root

if __name__ == "__main__":
    numbers = [3, 5, 7, 8, 10, 11, 13, 16, 17, 19, 26, 27, 32, 37, 38, 39, 42, 43, 46, 47, 52, 53, 54, 55, 56, 60, 63, 65, 66, 67, 70, 72, 73, 74, 75, 77, 78, 80, 81, 82, 83, 85, 87, 89, 91, 92, 93, 94, 97, 98]
    number_tree = Tree_builder(numbers)
    print(number_tree.search(26))
    print(number_tree.search(97))
    print(number_tree.search(301))