import multiprocessing
import datetime


def read_info(*name):
    all_data = []

    with open(name[0], 'r') as f:
        for line in f:
            if line != '':
                all_data.append(line)


files_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
'''0:00:05.967046'''
#start = datetime.datetime.now()
#for i in files_names:
#    read_info(i)
#end = datetime.datetime.now()
#print(end - start)
if __name__ == '__main__':
    files_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    with multiprocessing.Pool(processes=4) as pool:
        for i in files_names:
            """0:00:02.434201"""
            start = datetime.datetime.now()
            pool.map(read_info, files_names)
    end = datetime.datetime.now()
    print(end - start)

