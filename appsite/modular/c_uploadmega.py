from mega import Mega
mega = Mega()
m = mega.login('example@email.com', 'example_password') # Replace email and password with your Mega account credentials
summarised_suffix = '_summarised'

def upload_to_mega(filename):
    # Upload file
    file_path = f'modular/files/summary/{filename}'+f'{summarised_suffix}.txt'
    mega_file = m.upload(file_path)

    # Get download link
    download_link = m.get_upload_link(mega_file)

    print("File uploaded successfully. Download link: ", download_link)
    return download_link
    mega_recovery_key='exapmle_recovery_key'

