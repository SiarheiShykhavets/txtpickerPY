from pathlib import Path #библиотека для нормальной работы путей и файлов
import shutil #модуль для копирования файлов

base_dir = Path(__file__).parent # «Возьми путь к этому скрипту и возьми папку, в которой он лежит» (папка project)
input_dir = base_dir / "input" # «В папке проекта есть папка input» (папка input)
output_dir = base_dir / "output" # папка output

if not input_dir.exists():
    print("братан папка инпут куда делась?? ща создам")
    input_dir.mkdir()
if not output_dir.exists():
    print("братан папка аутпут куда делась?? ща создам")
    output_dir.mkdir()

txt_files = []
#фор отсеивает пути к тхт файлам в список, чтобы в будущем их скопировать 
for file in input_dir.iterdir(): #проходимся по каждому файлу в папке input_dir
    if file.is_file() and file.suffix == ".txt": #ЕСЛИ файл вообще является файлом и расширение файла (suffix, библиотека Path) является txt, то
        txt_files.append(file)

#конечные условия для дебага, если что то пойдет не так
if len(list(input_dir.iterdir())) == 0: #если длина пути инпут который мы переформатировали в список является нулем то (ну короче файлов нету ваще)
    print("папка input пуста") #спиздил у чата гпт это условие, но в целом понимаю       
elif len(txt_files) == 0:
    print('в папке input нету txt файлов')
else:
    ready = []
    for file in txt_files:
        shutil.copy(file, output_dir)
        ready.append(file)
    if ready:
        print("тхт файлы были успешно скопированы")
    else:
        print("Что то пошло не так...")        