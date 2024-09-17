import subprocess
import os

# Run a shell command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

with open('test_dir_path/os_operation.txt', 'w') as f:
    f.write(result.stdout)

with open('test_dir_path/os_operation.txt', 'r') as f:
    content = f.read()
    #print(content)

# Running multiple commands in a script
commands = ["echo Hello", "mkdir test", "ls"]

for cmd in commands:
    subprocess.run(cmd, shell=True)

