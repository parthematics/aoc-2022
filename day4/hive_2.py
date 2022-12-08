'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.

void put(int key, int value) inserts a (key, value) pair into the HashMap. 
If the key already exists in the map, update the corresponding value.

int get(int key) returns the value to which the specified key is mapped, 
or -1 if this map contains no mapping for the key.

int remove(key) removes the key and its corresponding value if the map 
contains the mapping for the key return -1 if key not found in hashmap.

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.

get, put, remove functions should complete their operations in constant O(1) time.

We would want to resize the hashmap based on the number of key/value pairs present inside the hashmap.

The main thing to remember would be that we care more about the time complexity,
as opposed to the space complexity. Although the space complexity should be reasonable.
'''

class HashMap:
  def __init__(self, capacity=100):
    self.capacity = capacity
    self.hashmap = self.make_buckets(capacity)
    self.size = 0
    self.size_up_threshold = 0.9
    self.size_down_threshold = 0.2
    
  def make_buckets(self, size):
    return [[] for _ in range(size)]
  
  # return val associated with key
  def get(self, key):
    bucket = self.get_bucket(key)
    
    for stored_tup in bucket:
      stored_key, stored_val = stored_tup
      if stored_key == key:
        return stored_val
      
    return -1
  
  # associate val with key
  def put(self, key, val):
    self.resize()
    
    bucket = self.get_bucket(key)
    key_exists = False
    
    for stored_tup in bucket:
      stored_key, stored_val = stored_tup
      if stored_key == key:
        key_exists = True
        stored_tup[1] = val
        return
        
    bucket.append([key, val])
    
    if not key_exists:
    	self.size += 1
      
  # remove key val pair
  def remove(self, key):
    bucket = self.get_bucket(key)
    
    for idx, stored_tup in bucket:
      stored_key, stored_val = stored_tup
      if key == stored_key:
        bucket.pop(idx)
        return key
    
    return -1
  
  # resize original hash table once we have reacher bucket capacity
  def resize(self):
    if self.size >= self.size_up_threshold * self.capacity:
      self.capacity *= 2
    # size down
    elif self.size <= self.size_down_threshold * self.capacity:
      self.capacity //= 2
      
    self.hashmap = self.populate_new_map()
      
	def populate_new_map(self):
    new_hashmap = self.make_buckets(self.capacity)
      
    for bucket_key, bucket in enumerate(self.hashmap):
      for key, val in bucket:
        new_bucket_key = hash_key(key) % self.capacity
        new_hashmap[new_bucket_key].append([key, val])
    
    return new_hashmap
  
  def get_bucket(self, key):
    bucket_key = self.hash_key(key) % self.capacity
    return self.hashmap[bucket_key]
  
  def hash_key(self, key):
    return (key * 1001) % 100019
  
  
  
  
  
  
  
  
  
  
  