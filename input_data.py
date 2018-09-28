import re


def read(file_name):
    '''
    :param file_name: 需要读入的文件名
    :return: 以二维列表形式存储的单词
    以逗号，空格，括号分隔字符串
    '''
    texts = []
    file_object = open(file_name, 'r', encoding='UTF-8')
    for line in file_object.readlines():
        texts.append(
            list(
                filter(None,
                       (word.lower()
                        for word in re.split(r'[(),. ]', line.strip())))))
    file_object.close()
    return texts


if __name__ == "__main__":
    print(read("data/2/trainData.txt"))
