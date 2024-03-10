from scoring_functions import calculate_score
import os
from openpyxl import Workbook

# Function to extract year from file name
def extract_year(file_name):
    # Extracting year from file name
    year = None
    try:
        year = int(file_name.split("_")[0])
    except ValueError:
        pass
    return year

# Function to create Excel table
def create_excel_table(folder_path, output_file):
    # Create a new workbook
    wb = Workbook()
    sheet = wb.active

    # Get all subfolders
    subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]

    # Write column headers
    years = list(range(2011, 2023))
    sheet.append([''] + years)

    # Process each subfolder
    for subfolder in subfolders:
        row_data = [subfolder]  # First element in row is subfolder name

        # Process PDF files in the subfolder
        for year in years:
            pdf_files = [file for file in os.listdir(os.path.join(folder_path, subfolder)) if file.endswith('.pdf')]
            total = 0
            for file in pdf_files:
                if extract_year(file) == year:
                    total += calculate_score(os.path.join(folder_path, subfolder, file))
            if year in [extract_year(file) for file in pdf_files]:
                row_data.append(total)
            else:
                row_data.append("-")

        # Write row data to Excel sheet
        sheet.append(row_data)

    # Save workbook to output file
    wb.save(output_file)

# Example usage:
folder_path = './reports'
output_file = 'output3.xlsx'
create_excel_table(folder_path, output_file)

