import hashlib
import json
salt = "c8523f1ea081"

with open("dictionary.txt") as file:
    data = json.load(file)

for word_obj in data:
    word = word_obj["word"]

    if len(word) == 7:
        flag = word
        hash_str = flag + salt

        hash_obj = hashlib.md5(hash_str.encode())
        md5_hash = hash_obj.hexdigest()

        if md5_hash == "3b97d1cb41ab60031f802a54b15b4340":
            print("The flag is:", flag)
            break
