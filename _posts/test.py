import os


def find_markdown_files(folder_path):
    """
    Finds and prints the names of all Markdown files in a given folder.

    Args:
        folder_path (str): The path to the folder to search.
    """
    # --- Check if the provided path is a valid directory ---
    if not os.path.isdir(folder_path):
        print(f"Error: The path '{folder_path}' is not a valid directory.")
        return

    print(f"Searching for Markdown files in: {folder_path}\n")

    # --- List to hold the names of found files ---
    markdown_files = []

    # --- Iterate over every item in the directory ---
    for filename in os.listdir(folder_path):
        # --- Check if the item is a file and ends with .md or .markdown ---
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            if filename.endswith(".md") or filename.endswith(".markdown"):
                markdown_files.append(filename)

    # --- Print the results ---
    if markdown_files:
        print("Found the following Markdown files:")
        for file in markdown_files:
            print(file)
    else:
        print("No Markdown files were found in this directory.")


if __name__ == "__main__":
    # --- IMPORTANT: Change this to the path of your folder ---
    # You can use a relative path (e.g., './my_notes')
    # or an absolute path (e.g., 'C:/Users/YourUser/Documents/Notes')
    target_folder = "."  # '.' represents the current directory

    try:
        find_markdown_files(target_folder)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
