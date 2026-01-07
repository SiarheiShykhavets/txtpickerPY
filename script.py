from pathlib import Path
import shutil 

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
for file in input_dir.iterdir(): #проходимся по каждому файлу в папке input_dir
    if file.is_file() and file.suffix == ".txt": #ЕСЛИ файл вообще является файлом и расширение файла (suffix, библиотека Path) является txt, то
        txt_files.append(file)
if len(txt_files) == 0:
    print('чет пусто')

        