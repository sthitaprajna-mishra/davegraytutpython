band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(type(band2))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# verify if a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({ "bass": "JPG" })

print(band)

# Remove items
print(band.pop("bass")) # -> returns value only
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # -> removes last item added to the dictionary and returns key value pair as a tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# band2 = band # creates a reference
# band2.update({ "song": "Jama Jamaloo" })
# print(band)
# print(band2)

band2 = band.copy() # creates a deep copy
band2.update({ "song": "Jama Jamaloo" })
print(band)
print(band2)

band3 = dict(band) # deep copy also!
band3.update({ "lead": "Lord Bobby" })
print(band)
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member2"])

# Sets

nums = { 1,2,3,4 }

nums2 = set((1,2,3,4,5))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums2))

# no duplicates allowed
nums = {1,2,2,2,3,4}
print(nums)

# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an idnex position or a key

# add a new element to the set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries too

# merge 2 sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1,2,3}
two = {2,3,7}

one.intersection_update(two)
print(one)

# keep only the unique values from 'one'
one = {1,2,3}
two = {2,3,7}

one.intersection(two)
print(one)

# keep everything except the duplicates
one = {1,2,3}
two = {2,3,7}

one.symmetric_difference_update(two)
print(one)