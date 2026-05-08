#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()

# 1. Test Non-existent file
print("Testing non-existent file...")
res1 = CustomObject.deserialize("does_not_exist.pkl")
print(f"Result: {res1}") # Should be None

# 2. Test Malformed file
print("\nTesting malformed file...")
with open("bad_data.txt", "w") as f:
    f.write("This is not a pickle object!")

res2 = CustomObject.deserialize("bad_data.txt")
print(f"Result: {res2}") # Should be None