# with open("example.txt","r") as file:
#     content = file.read()
#     print(content)

# file.close()

# with open("example.txt", "w") as f:
#     f.write("Rop is writing into this file")

# with open("example.txt", "a") as f:
# #     f.write("Rop is \"writing\" into this file\nAdded a message")
 
# try:
#     with open("example.txt", "x") as f:
#         f.write("Rop is \"writing\" into this file\nAdded a message")
#         f.close
# except FileExistsError:
#     print("File already exist")


import os


# os.rename("example.txt", "differentfile")


import os

os.remove("differentfile")
