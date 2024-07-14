import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range):
    """
    Переименовывает файлы в текущем каталоге.

    Параметры:
    desired_name (str): желаемое конечное имя файлов
    num_digits (int): количество цифр в порядковом номере
    source_ext (str): расширение исходного файла
    target_ext (str): расширение конечного файла
    name_range (tuple): диапазон сохраняемого оригинального имени
    """
    # Получаем текущую рабочую директорию
    current_dir = os.getcwd()
    
    # Получаем список файлов с заданным расширением в текущей директории
    files = [f for f in os.listdir(current_dir) if f.endswith(f".{source_ext}")]
    
    if not files:
        print(f"Файлы с расширением '{source_ext}' не найдены в текущей директории.")
        return
    
    # Перебираем файлы и переименовываем их
    for i, file in enumerate(files, start=1):
        # Извлекаем оригинальное имя файла в заданном диапазоне
        original_name = file[name_range[0]-1:name_range[1]]
        
        # Формируем новое имя файла
        new_name = f"{desired_name}_{str(i).zfill(num_digits)}.{target_ext}"
        
        # Составляем полные пути к исходному и целевому файлам
        src_path = os.path.join(current_dir, file)
        dest_path = os.path.join(current_dir, new_name)
        
        # Переименовываем файл
        try:
            os.rename(src_path, dest_path)
            print(f"Переименован файл: {file} -> {new_name}")
        except OSError as e:
            print(f"Ошибка при переименовании файла {file}: {e}")

# Пример использования
rename_files(desired_name="new_file", num_digits=3, source_ext="txt", target_ext="docx", name_range=(3, 6))
