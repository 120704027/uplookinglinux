import os
import hashlib

def getfname(directory):
    file_list = []
    for dir_name, sub_dir_list, file_name_list in os.walk(directory):
        if len(file_name_list) > 0:
            for f_name in file_name_list:
                # full_file_name = dir_name + "\\" + f_name
                file_list.append(dir_name + "\\" + f_name)

    return file_list


def fileMD5(file_name):
    md5=hashlib.md5()
    with open(file_name,mode="rb") as f:
        while True:
            data=f.read(4096)
            if data:
                md5.update(data)
            else:
                break
    return md5.hexdigest()





if __name__ == '__main__':
    data=getfname(r"E:\pythonProject1\FileIO")
    print(data)
    # for i in data:
    #     print(i)
    # print(data)
    # data_01=fileMD5(r"E:\pythonProject1\funDemo\test01.py")
    # if len(data_01)>0:
    #     print("Y")
# for dir_name, sub_dir_name, file_name in os.walk(r"E:\pythonProject1\FileIO"):
#     if len(file_name) > 0:
#         for f_name in file_name:
#             print(dir_name + "\\" + f_name)
