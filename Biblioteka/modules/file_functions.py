import pickle

def read_file(file_name):
    with open(file_name, "rb") as reader:
        books = pickle.load(reader)
        return books