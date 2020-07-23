from shutil import copyfile

path_json = open("/media/minhhoang/Data/dataPerson/Datatest/easy_json.txt").read().splitlines()
path_images = open("/media/minhhoang/Data/dataPerson/Datatest/easy_img.txt").read().splitlines()

dir_data = "/media/minhhoang/Data/dataPerson/"

for p_img, p_json in zip(path_json, path_images):
    name_img = p_img.split("/")[-1]
    name_json = p_json.split("/")[-1]
    copyfile(dir_data + p_json, "/home/minhhoang/Desktop/Data_analysis/data_test/json/"+name_json)
    copyfile(dir_data + p_img, "/home/minhhoang/Desktop/Data_analysis/data_test/img/"+name_img)
