from pathlib import Path
import shutil 

base_dir = Path(__file__).parent # «Возьми путь к этому скрипту и возьми папку, в которой он лежит» (папка project)
input_dir = base_dir / "input" # «В папке проекта есть папка input» (папка input)
output_dir = base_dir / "output" # папка output

for file in input_dir.iterdir(): #проходимся по каждому файлу в папке input_dir
    if file.is_file() and file.suffix == ".txt": #ЕСЛИ файл вообще является файлом и расширение файла (suffix, библиотека Path) является txt, то
        shutil.copy(file, output_dir)

        