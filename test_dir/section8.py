# #ファイルの操作

# # f = open('test.txt', 'w')
# # f.write('Test\n')
# # # print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
# # f.close()


# # with open('test.txt', 'w') as f:
# #   f.write('Test\n')


# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# with open('test.txt', 'r') as f:
#   # while True:
#   #   chunk = 2
#   #   line = f.readline()
#   #   print(line, end='')
#   #   if not line:
#   #     break
#   # print(f.tell())
#   # print(f.read(1))
#   # print(f.tell())
#   # print(f.read(1))
#   # f.seek(5)
#   # print(f.read(1))








#csvファイルへの書き込み


# import csv

# with open('test.csv', 'w') as csv_file:
#   fieldnames = ['Name', 'Count']
#   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#   writer.writeheader()
#   writer.writerow({'Name': 'A', 'Count': 1})

# with open('test.csv', 'r') as csv_file:
#   reader = csv.DictReader(csv_file)
#   for row in reader:
#     print(row['Name'], row['Count'])

 
#terminalで open test.csv




#ファイル操作

# import os
# import pathlib
# import glob
# import shutil

# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('test.txt'))

# # os.rename('test.txt', 'renamed.txt')
# os.symlink('renamed.txt', 'symlink.txt')

# os.mkdir('test_dir')
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))
# shutil.rmtree('test_dir')

# print(os.getcwd())



# tarfileの圧縮展開

# import tarfile

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#   tr.add('test_dir')

# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#   # tr.extractall(path='test_tar')
#   with tr.extractfile('test_dir/sub_dir/sub_text.txt') as f:
#     print(f.read())








# import zipfile

# with zipfile.ZipFile('test.zip', 'w') as z:






# import tempfile

# with tempfile.TemporaryFile



# import subprocess

# subprocess.run(['ls', '-al'])





