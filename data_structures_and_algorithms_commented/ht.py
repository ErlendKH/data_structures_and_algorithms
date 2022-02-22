# Should use a prime number of addresses to reduce collisions.

class HashTable:
    def __init__(self, size = 7): # 7 is here a default value.
        self.data_map = [None] * size # 7 of None.

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # 23 prime number. Can use any prime number.
            # modulo with the length ...

            # ord():
            # Return the Unicode code point for a one-character string.
            
            # Unicode code point for a character.
            # So converting characters into an int value?

            # Then, modulo by the length of data_map (see initialization).
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

            # # Debug:
            # o = ord(letter)
            # o23 = ord(letter) * 23
            # l = len(self.data_map)
            # print('ord(letter): ', o)
            # print('o23: ', o23)
            # print('l: ', l)
            # print('my_hash', my_hash)

        return my_hash

    def print_table(self):
        # enumerate() --> Index and value of a hash table
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        # Hm, going to return an index, Ex. 4
        index = self.__hash(key)

        # If that index is None
        if self.data_map[index] == None:
            # Create a list to hold other lists.
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            # Looping the list holding items at that index
            for i in range(len(self.data_map[index])):
                # So the [i] is the index of the item
                # within the outer list.

                # [0] refers to the first value of each
                # key-value pair, e.g. the 'bolts'.
                #['bolts', 1400]
                # 'bolts' is at index 0, while 1400 is at index 1.
                if self.data_map[index][i][0] == key:
                    # returning the value at index 1.
                    # Ex. 1400 in the case of ['bolts', 1400].
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        # First, loop all the indexes (e.g. 0-6)
        for i in range(len(self.data_map)):
            # Only do another loop if something is there.
            if self.data_map[i] is not None:
                # Another loop for the key-value pairs.
                for j in range(len(self.data_map[i])):
                    # Appending the key names of the pairs.
                    # Keys are always first, e.g. 'bolts':
                    # ['bolts', 1400]
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()

# my_hash_table.print_table()

# 1: set

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

# my_hash_table.print_table()

# 2: get

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)

# print(my_hash_table.get_item('bolts')) # 1400
# print(my_hash_table.get_item('washers')) # 50
# print(my_hash_table.get_item('lumber')) # None

# 3: keys

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys()) # ['bolts', 'washers', 'lumber']

# 4: 