from os import unlink, listdir, getlogin
from tqdm import tqdm

login = getlogin()
link1 = r'C:\Users\{}\AppData\Local\Temp'.format(login)
arr = listdir(r'C:\Windows\Temp')
arr2 = listdir()
for i in tqdm(arr):
    try:
        unlink(r'C:\Windows\Temp\{}'.format(i))
    except:
        pass
print('Windows Temp очищен!')
for i in tqdm(arr2):
    try:
        unlink(link1+r'\{}'.format(i))
    except:
        pass
print('Local Temp очищен!')

input('Нажмите на ENTER , чтобы закрыть программу...')
