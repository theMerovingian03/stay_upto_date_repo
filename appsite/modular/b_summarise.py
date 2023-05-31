import os
import PyPDF2
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words

summarised_suffix = '_summarised'
def summarise_downloaded_text(filename):
    # Open the PDF file
    pdf_file = open(f'modular/files/original/{filename}.pdf', 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize an empty string to store the text
    text = ''

    # Loop through the pages of the PDF and extract the text
    for page in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page].extract_text()
        text += page_text

    # Tokenize the text
    tokens = word_tokenize(text)

    # Initialize the summarizer
    summarizer = LsaSummarizer()
    summarizer.stop_words = get_stop_words('english')

    # Set the number of sentences in the summary
    summary_size = 25

    # Create a parser object for the text
    parser = PlaintextParser.from_string(text, Tokenizer('english'))

    # Summarize the text
    summary = summarizer(parser.document, summary_size)
    pdf_file.close()
    # Print the summary
    # for sentence in summary:
    #     print(sentence)
    summary_path = 'modular/files/summary'
    # Write the summary to a file
    if not os.path.exists(summary_path):
        os.makedirs(summary_path)
    with open(f'modular/files/summary/{filename}'+f'{summarised_suffix}.txt', 'w') as file:
        for sentence in summary:
            file.write(str(sentence) + '\n')
        file.close()


