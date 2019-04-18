from urllib.request import quote
import random

BEFORE_ENCODE_PATH = "./valid_xss_to_encode.txt"
VALID_XSS_PATH = "./data/valid_xss.txt"

def ReadFileDatas():
    FileNamelist = []
    file = open(BEFORE_ENCODE_PATH, 'r+')
    for line in file:
        line = line.strip('\n')  # 删除每一行的\n
        FileNamelist.append(line)
    print('len ( FileNamelist ) = ', len(FileNamelist))
    file.close()
    return FileNamelist


def WriteDatasToFile(listInfo):
    fileInfo = ""
    for each_info in listInfo:
        url_code_name = quote(each_info)
        fileInfo += url_code_name + '\n'
    with open(VALID_XSS_PATH, 'w') as f:
        f.write(fileInfo)



if __name__ == "__main__":
    listFileInfo = ReadFileDatas()
    # 打乱列表中的顺序
    random.shuffle(listFileInfo)
    WriteDatasToFile(listFileInfo)

