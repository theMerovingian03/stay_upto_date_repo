import requests
import os
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words
from mega import Mega

nltk.download('punkt')

def download_from_link(url, filename):
    path_directory = 'file_directory/files/original/'
    path_directory2 = 'file_directory/files/summary/'
    if not os.path.exists(path_directory):
        os.makedirs(path_directory)
    if not os.path.exists(path_directory2):
        os.makedirs(path_directory2)
    response = requests.get(url)
    with open(f'file_directory/files/original/{filename}.pdf', 'wb') as file:
        file.write(response.content)

def summarise_downloaded_text(filename):
    # Open the PDF file
    pdf_file = open(f'file_directory/files/original/{filename}.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page].extract_text()
        text += page_text

    tokens = word_tokenize(text)
    summarizer = LsaSummarizer()
    summarizer.stop_words = get_stop_words('english')
    summary_size = 25
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summary = summarizer(parser.document, summary_size)
    pdf_file.close()

    summary_path = 'file_directory/files/summary/'
    if not os.path.exists(summary_path):
        os.makedirs(summary_path)
    with open(f'file_directory/files/summary/{filename}_summarised.txt', 'w', encoding='utf-8') as file:
        for sentence in summary:
            file.write(str(sentence) + '\n')

def upload_to_mega(filename):
    mega = Mega()
    m = mega.login('stayuptodate23@outlook.com', 'RRAM2423258#ok')  # Replace email and password with your Mega account credentials

    file_path = f'file_directory/files/summary/{filename}_summarised.txt'
    mega_file = m.upload(file_path)
    download_link = m.get_upload_link(mega_file)

    print("File uploaded successfully. Download link:", download_link)
    return download_link

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")

def call_delete(filename):
    output_file_path = f'file_directory/files/summary/{filename}_summarised.txt'
    delete_file(output_file_path)
    original_file_path = f'file_directory/files/original/{filename}.pdf'
    delete_file(original_file_path)

def process_file(url, filename):
    download_from_link(url, filename)
    summarise_downloaded_text(filename)
    link = upload_to_mega(filename)
    call_delete(filename)
    return link
