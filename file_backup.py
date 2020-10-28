import tarfile
import pickle
import datetime
from funDemo import fun_getfname as fp
def fullbackup():
    source_dir=r"E:\pythonProject1\FileIO"
    md5_file=r"E:\pythonProject1\file02\md5.txt"
    current_time=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    full_tar_file_name=r"e:\pythonProject1\file02\data_%s.tar.gz"%current_time
    full_tar_obj=tarfile.open(full_tar_file_name,mode="w:gz")
    file_md5_list={}
    # sou_file=fp.getfname(source_dir)
    # print(sou_file)
    source_file_list=fp.getfname(source_dir)
    for file_name in source_file_list:
        full_tar_obj.add(file_name)
        source_file_md5=fp.fileMD5(file_name)
        file_md5_list[file_name]=source_file_md5
    full_tar_obj.close()
    with open(md5_file,mode="wb")as fobj:
        pickle.dump(file_md5_list,fobj)

def increBackup():
    source_dir = r"E:\pythonProject1\FileIO"
    current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    incr_tar_file_name = r"e:\pythonProject1\file02\data_%s.tar.gz" % current_time
    incre_tar_obj = tarfile.open(incr_tar_file_name, mode="w:gz")
    md5_file=r"E:\pythonProject1\file02\md5.txt"
    with open(md5_file,mode="rb") as fobj:
        file_md5_dict=pickle.load(fobj)

    source_file_list=fp.getfname(source_dir)
    for file_name in source_file_list:
        if file_name not in file_md5_dict.keys():
            incre_tar_obj.add(file_name)
            new_md5=fp.fileMD5(file_name)
            file_md5_dict[file_name]=new_md5
        else:
            new_md5=fp.fileMD5(file_name)
            old_md5=file_md5_dict.get(file_name)
            if new_md5!=old_md5:
                incre_tar_obj.add(file_name)
                file_md5_dict[file_name]=new_md5
    incre_tar_obj.close()
    with open(md5_file,mode="wb") as fobj:
        pickle.dump(file_md5_dict,fobj)

if __name__ == '__main__':
    # fullbackup()
    increBackup()


























# if __name__ == '__main__':
#     fullbackup()