import os

def print_file_structure(root_dir, indent_level=0):
    # Iterate through all files and directories in the given folder
    with os.scandir(root_dir) as entries:
        for entry in entries:
            # Skip hidden files and directories
            if entry.name.startswith('.'):
                continue
            
            # Print the current entry (file or directory)
            print('    ' * indent_level + entry.name)
            
            # If it's a directory, recursively print its contents
            if entry.is_dir():
                print_file_structure(entry.path, indent_level + 1)

# Automatically get the root directory where the script is run from
root_directory = os.getcwd()

# Call the function
print_file_structure(root_directory)
