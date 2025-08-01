import os
import fitz

scan_folder_path = r"\\SCANOPS0LAB01\Scan Documents\Health\Labs\Jacob"

def has_pdf_files(folder_path):
    """
    checks is the given folder path has pdf files in it. 
    """

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory")
        return False
    
    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path,entry)
        if os.path.isfile(full_path):

            file_name, file_extension = os.path.splitext(entry)
            print(file_extension)
            if file_extension.lower() == ".pdf":
                print(f"Folder: '{folder_path}' has PDF files in it.")
                return True
    print(f"Folder: {folder_path} does not have PDF files in it.")
    return False 

def main():

    has_pdf_files(scan_folder_path)



if __name__ == "__main__":
    main()
