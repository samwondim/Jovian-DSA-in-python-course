def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0
    
    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number
    
    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None]*max_size


    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key,value)


    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value


    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list,key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key,value)

class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)
    
    
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list,key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            k,v = kv
            return v
        
    
    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list,key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key,value)

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]
    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]
