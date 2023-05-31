import os

# Specify the path of the file to be deleted
summarised_suffix = '_summarised'
def delete_file(file_path):

    # Check if the file exists

    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")

def call_delete(filename):
    # delete output file
    output_file_path = f'modular/files/summary/{filename}'+f'{summarised_suffix}.txt'
    delete_file(output_file_path)

    # delete original file
    original_file_path = f'files/original/{filename}.pdf'
    delete_file(original_file_path)

