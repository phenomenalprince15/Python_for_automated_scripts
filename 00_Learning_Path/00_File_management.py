import os

'''
File Handling and Directory management
'''

# Get the directory of the curent script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define path for 'test_dir' in same folder as script
test_dir_path = os.path.join(script_dir, 'test_dir')

# To create a directory
os.makedirs('test_dir_path', exist_ok=True)

# Writing to a file
with open('test_dir_path/sample.txt', 'w') as f:
    f.write("Hello, world")


# Read from a file
with open('test_dir_path/sample.txt', 'r') as f:
    content = f.read()
    print(content)


# List directory contents
files = os.listdir('test_dir_path')
print(files)


