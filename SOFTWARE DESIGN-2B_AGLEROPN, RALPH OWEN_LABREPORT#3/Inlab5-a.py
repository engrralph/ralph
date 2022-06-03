# Function to display hashtable
def display_hash(hashTable):
    for a in range(len(hashTable)):
        print(a, end=" ")

        for b in hashTable[a]:
            print("-->", end=" ")
            print(b, end=" ")

        print()


# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(10)]


# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

# Driver Code
insert(HashTable, 1, 'Owen')
insert(HashTable, 2, 'Darienne')
insert(HashTable, 3, 'Nicole')
insert(HashTable, 5, 'Ralph')
insert(HashTable, 5, 'Yanyan')
insert(HashTable, 8, 'Darlene')

display_hash(HashTable)