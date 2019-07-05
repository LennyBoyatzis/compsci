import os
import hashlib


# MD5 hash (output always 128 bits 2^7)
def hash_string(string: bytes) -> str:
    m = hashlib.md5(string)
    return m.hexdigest()


if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)
    relative_path = '../data/article.txt'
    path = os.path.join(working_dir, relative_path)

    with open(path, 'rb') as textfile:
        data = textfile.read()
        hash_file_contents = hash_string(data)
