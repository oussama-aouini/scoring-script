import os
import PyPDF2

def pdf_to_text(pdf_path):
    """
    Converts a PDF file to a text file.
    """
    text = ''
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error converting {pdf_file}: {e}")
        return None
    return text

def convert_folder_to_text(input_folder, output_folder):
    """
    Converts all PDF files within a folder and its subfolders to text files.
    Retains the same folder structure.
    """
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                relative_path = os.path.relpath(pdf_path, input_folder)
                output_path = os.path.join(output_folder, relative_path[:-4] + '.txt')  # Change extension to .txt
                output_dir = os.path.dirname(output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                text = pdf_to_text(pdf_path)
                if text is not None:
                    with open(output_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(text)

# Example usage:
input_folder = r'C:\Users\oussama\Downloads\oussema'
output_folder = r'C:\Users\oussama\Downloads\result'

convert_folder_to_text(input_folder, output_folder)
