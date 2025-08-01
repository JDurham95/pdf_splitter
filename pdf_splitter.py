import os
import fitz

scan_folder_path = r""

def check_for_pdf_files(folder_path, file_path_array):
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
                file_path_array.append(full_path)

    if len(file_path_array)> 0:
        print(f"Folder: {folder_path} has {len(file_path_array)} PDF files")
        return file_path_array
    else:
        print(f"Folder: {folder_path} does not have PDF files in it.")
        return False 

def split_pdf_files(folder_path, file_path_array):
    """
    splits the first multipage pdf into multiple pages 
    """
    new_doc_count = 0

    for file_path in file_path_array:
        
        try:
            document = fitz.open(file_path)

            print(f"Opened PDF: {file_path} with {document.page_count} pages.")

            for page_num in range(document.page_count):
                page = document.load_page(page_num)

                new_pdf = fitz.open()
                new_pdf.insert_pdf(document, from_page=page_num, to_page=page_num)

                base_name = new_doc_count + 1
                output_paf_name = f"{base_name}.pdf"
                output_pdf_path = os.path.join(folder_path,output_paf_name)

                new_pdf.save(output_pdf_path)
                new_pdf.close 
                new_doc_count += 1
            
            document.close()

        except Exception as e:
            print(f"An error occured during PDF splitting: {e}")


def main():

    pdf_file_path_array = []
    pdf_file_path_array = check_for_pdf_files(scan_folder_path, pdf_file_path_array)

    if pdf_file_path_array:
        split_pdf_files(scan_folder_path, pdf_file_path_array)


    
    



if __name__ == "__main__":
    main()
