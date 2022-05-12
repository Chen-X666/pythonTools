import os
import sys
import logging
from configparser import ConfigParser
from concurrent.futures import ProcessPoolExecutor

cwd = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))

from pdf2docx import Converter


def pdf_to_word(pdf_file_path, word_file_path):
    cv = Converter(pdf_file_path)
    cv.convert(word_file_path)
    cv.close()


def main():
    logging.getLogger().setLevel(logging.ERROR)

    config_parser = ConfigParser()
    config_parser.read("config.cfg")
    config = config_parser["default"]

    for file in os.listdir(config["pdf_folder"]):
        extension_name = os.path.splitext(file)[1]
        if extension_name != ".pdf":
            continue
        file_name = os.path.splitext(file)[0]
        pdf_file = cwd+"/"+config["pdf_folder"] + "/" + file
        word_file = cwd+"/"+config["word_folder"] + "/" + file_name + ".docx"
        print("正在处理: ", pdf_file)
        print("word文件地址: ", word_file)
        pdf_to_word(pdf_file_path=pdf_file,word_file_path=word_file)
    print("完成")


if __name__ == "__main__":
    main()
