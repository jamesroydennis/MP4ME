import argparse
import os

# Function to process the file input
def process_file(file_path: str):
    """ Process the given file. For now, just checks if it exists. """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    print(f"File '{file_path}' has been successfully processed!")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Simple CLI Tool for File Processing")
    
    # Define the argument for the file path
    parser.add_argument("file", type=str, help="Path to the file to be processed")
    
    # Parse the arguments
    args = parser.parse_args()

    try:
        # Process the file
        process_file(args.file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
