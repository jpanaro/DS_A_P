# custom implementation of a mutable array 
# leverages automatic resizing and multiple unique operations

class CustomVector:
    def __init__(self, capacity):
        # Capacity defines number of total indices in array
        # Size defines number of populated indices, or number of elements
        self.arr_capacity = capacity
        self.arr_size = 0
        self.arr = [None]*capacity
    
    def size(self):
        return self.arr_size

    def ret_capacity(self):
        return self.arr_capacity
    
    def is_empty(self):
        if self.arr_size == 0:
            return True
        else:
            return False
    
    def at(self, index):
        if self.is_empty():
            raise Exception("There are no items in the array")
        if index < 0 or index > (self.arr_capacity):
            raise Exception("Index provided is out of bounds of current array.")
        else:
            return self.arr[index]
    
    def push(self, item):
        # Check if at full capacity, and if so resize array
        if self.arr_size == self.arr_capacity:
            self.__resize(self.arr_capacity*2)
        # Add item to array
        self.arr[self.arr_size] = item
        self.arr_size += 1

    # inserts item at index, shifts that index's value and trailing elements to the right
    def insert(self, index, item):
        if index < 0 or index > (self.arr_capacity):
            raise Exception("Index provided is out of bounds of current array.")
        elif self.arr_size == self.arr_capacity:
            self.__resize(self.arr_capacity*2)
        # shift all elements
        if index >= self.arr_size:
            self.arr[index] = item
        else:
            # iterate from last item down to item after index of interest
            for i in range(self.arr_size, index, -1):
                self.arr[i] = self.arr[i-1]
        # Finally, insert new element
        self.arr[index] = item
        # Update size
        self.arr_size += 1
    
    # Performs in insert at index 0
    def prepend(self, item):
        self.insert(0, item)
    
    # removes the last item in the array and returns the value
    def pop(self):
        if not self.is_empty():
            # store last item in array
            temp_val = self.arr[self.arr_size-1]
            self.remove(self.arr[self.arr_size-1])
            return temp_val
        else:
            raise Exception("There are no elements in the array to pop")
    
    # delete item at index, shifting all trailing elements left
    def delete(self, index):
        if self.is_empty():
            raise Exception("There are no items in the array")
        if index < 0 or index > (self.arr_capacity):
            raise Exception("Index provided is out of bounds of current array.")
        # Iterate from index to end shifting all elements left
        for i in range(index, self.arr_size):
            self.arr[i] = self.arr[i+1]
        self.arr_size -= 1

    # Looks for all instances of a value in the array and removes indices holding it
    def remove(self, item):
        item_count = 0
        if self.is_empty():
            raise Exception("There are no items in the array")
        # Check if there is at least one instance of <item> in array
        for j in range(self.arr_size):
            if self.arr[j] == item:
                item_count += 1
        if item_count == 0:
            raise Exception("This item does not exist in the array") 
        # Create entirely new vector and populate with everything that is not 'item'
        new_arr = CustomVector(self.arr_capacity-item_count)
        for i in range(self.arr_size):
            if self.arr[i] != item:
                new_arr.push(self.arr[i])
        # Update main array attributes
        self.arr = new_arr.arr
        self.arr_size = new_arr.arr_size
        self.arr_capacity = new_arr.arr_capacity
    
    # Looks for value and returns first index with that value
    def find(self, item):
        for i in range(self.arr_size):
            if self.arr[i] == item:
                return i
        # Item not found
        return -1

    def __resize(self, new_capacity):
        # 1: Make new array twice the size of old array
        print("New capacity = " + str(new_capacity))
        new_array = [None]*new_capacity
        # 2: Loop over old array and copy all items to new array
        for i in range(self.arr_capacity):
            new_array[i] = self.arr[i]
        # 3: Replace old array with new array
        self.arr = new_array
        # 4: Update capacity (size remains the same)
        self.arr_capacity = new_capacity

def main():
    # Create custom array and perform operations on it
    new_arr = CustomVector(capacity=4)
    print("Appending 6->9")
    new_arr.push(6)
    new_arr.push(7)
    new_arr.push(8)
    new_arr.push(9)
    print(new_arr.arr)
    print("Appending 10 (with forced resize)")
    new_arr.push(10)
    print(new_arr.arr)
    print("Capacity = " + str(new_arr.ret_capacity()))
    print("Size = " + str(new_arr.size()))
    new_arr.push(12)
    new_arr.push(13)
    print(new_arr.arr)
    print("Size = " + str(new_arr.size()))
    print("Inserting 11 into index 5")
    new_arr.insert(5, 11)
    print(new_arr.arr)
    print("Size = " + str(new_arr.size()))
    print("Prepending '5'")
    new_arr.prepend(5)
    print(new_arr.arr)
    print("Value at index 3:")
    print(new_arr.at(3))
    new_arr.push(8)
    print(new_arr.arr)
    print("Removing all instances of the value '8'")
    print(new_arr.remove(8))
    print(new_arr.arr)
    print("Capacity = " + str(new_arr.ret_capacity()))
    print("Size = " + str(new_arr.size()))
    print("Popping!")
    new_arr.pop()
    print(new_arr.arr)
    print("Capacity = " + str(new_arr.ret_capacity()))
    print("Size = " + str(new_arr.size()))
    print("Deleting item at index 2 ('7')")
    new_arr.delete(2)
    print(new_arr.arr)
    print("Capacity = " + str(new_arr.ret_capacity()))
    print("Size = " + str(new_arr.size()))
    print("Finding '11', we expect a return value of 4")
    print(new_arr.find(11))
    print("Return value at index 2, we expect '9'")
    print(new_arr.at(2))

if __name__ == "__main__":
    main()