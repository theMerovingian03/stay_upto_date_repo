import requests
import os

def download_from_link(url,filename):
    path_directory = 'modular/files/origial'
    path_directory2 = 'modular/files/summary'
    if not os.path.exists(path_directory):
        os.makedirs(path_directory)
    if not os.path.exists(path_directory2):
        os.makedirs(path_directory2)
    response = requests.get(url)
    with open(f'modular/files/original/{filename}.pdf', 'wb') as file:
        file.write(response.content)
    file.close()


