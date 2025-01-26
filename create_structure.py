import os

# Define the folder structure
structure = {
    "mp4me": {
        "input": ["__init__.py", "file_reader.py", "validation.py"],
        "processing": ["__init__.py", "repair_algorithm.py", "comparison.py"],
        "output": ["__init__.py", "file_writer.py", "reporting.py"],
        "cli_tool.py": None,
        "main.py": None,
        "README.md": None,
        "requirements.txt": None
    }
}

def create_structure(base_path, structure):
    """
    Recursively create the folder structure and files as per the given 'structure' dict.
    :param base_path: The base directory where the structure will be created.
    :param structure: A dictionary representing the folder and file structure.
    """
    for folder_name, content in structure.items():
        folder_path = os.path.join(base_path, folder_name)

        # Create folder if it doesn't exist
        if content is None:
            # Create file
            with open(folder_path, "w") as f:
                pass  # Just create an empty file
        else:
            # Create directory
            os.makedirs(folder_path, exist_ok=True)

            # Recursively create files in the folder
            for file_name in content:
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "w") as f:
                    pass  # Create an empty file

if __name__ == "__main__":
    # Define the base path where the structure will be created
    base_path = os.getcwd()  # Current working directory
    
    # Start creating the structure
    create_structure(base_path, structure)
    print("Folder and file structure created successfully.")
