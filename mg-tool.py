import os
import sys
import concurrent.futures
from PIL import Image, ImageEnhance
import base64
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox

PROPORTION = 2.47
PROPORTION_BIGGER = 7.3
UNDER_PADDING = 150
LEFT_PADDING = 110
RIGHT_PADDING = 110


MEDIA_GROUP_LOGO_FILE = "mediagroup_logo.txt"
TUSUR_LOGO_FILE = "tusur_logo.txt"


def get_logo_image(logo_file):
    try:
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        logo_path = os.path.join(base_path, logo_file)

        with open(logo_path, "r", encoding="utf-8") as f:
            logo_base64 = f.read().strip()
        logo_data = base64.b64decode(logo_base64)
        return Image.open(BytesIO(logo_data)).convert("RGBA")
    except Exception as e:
        print(f"Ошибка загрузки логотипа из {logo_file}: {e}")
        sys.exit(1)


def clear():
    return os.system("cls" if os.name == "nt" else "clear")


def get_input():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Некорректный ввод")
            continue


def menu():
    while True:
        print("Меню настроек:")
        print("1) Изменить dpi")
        print("2) Изменить выходное разрешение и dpi")
        print("3) Вставить лого")
        print("4) Выход")
        print("Номер: ")
        choice = get_input()
        if choice in [1, 2, 3, 4]:
            return choice
        print("Некорректный тип данных")


def logo_menu():
    while True:
        print("Выберите логотип:")
        print("1) Вставить логотип MediaGroup")
        print("2) Вставить логотип TUSUR")
        print("3) Вставить оба логотипа")
        print("4) Назад")
        print("Номер: ")
        choice = get_input()
        if choice in [1, 2, 3, 4]:
            return choice
        print("Некорректный тип данных")


def print_progress_bar(iteration, total, prefix="", suffix="", length=50, fill="█"):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    progress_info = f"{iteration}/{total}"
    sys.stdout.write(
        "\r%s |%s| %s%% %s %s" % (prefix, bar, percent, progress_info, suffix)
    )
    sys.stdout.flush()


def process_dpi_image(filename, input_folder, output_folder, dpi):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.info["dpi"] = (dpi, dpi)
        img.save(os.path.join(output_folder, filename), dpi=(dpi, dpi))


def process_resolution_image(filename, input_folder, output_folder, dpi, width, height):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.info["dpi"] = (dpi, dpi)
        img = img.resize((width, height))
        img.save(os.path.join(output_folder, filename), dpi=(dpi, dpi))


def processDPI(input_folder, output_folder, dpi):
    clear()
    print("Все фотографии меняются под dpi ", dpi)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = [
        f
        for f in os.listdir(input_folder)
        if f.endswith((".jpg", ".jpeg", ".JPG", ".JPEG"))
    ]
    total_files = len(files)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, filename in enumerate(files):
            futures.append(
                executor.submit(
                    process_dpi_image, filename, input_folder, output_folder, dpi
                )
            )
            print_progress_bar(
                i + 1,
                total_files,
                prefix="Процесс обработки:",
                suffix="Готово",
                length=50,
            )
        for future in concurrent.futures.as_completed(futures):
            future.result()


def processResolution(input_folder, output_folder, dpi, width, height):
    clear()
    print("Все фотографии меняются под dpi ", dpi, " и разрешение ", width, "х", height)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = [
        f
        for f in os.listdir(input_folder)
        if f.endswith((".jpg", ".jpeg", ".JPG", ".JPEG"))
    ]
    total_files = len(files)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, filename in enumerate(files):
            futures.append(
                executor.submit(
                    process_resolution_image,
                    filename,
                    input_folder,
                    output_folder,
                    dpi,
                    width,
                    height,
                )
            )
            print_progress_bar(
                i + 1,
                total_files,
                prefix="Процесс обработки:",
                suffix="Готово",
                length=50,
            )
        for future in concurrent.futures.as_completed(futures):
            future.result()


def process_image(filename, input_folder, output_folder, logo_choice):
    with Image.open(os.path.join(input_folder, filename)) as img:
        back_img = img.copy()

        if logo_choice in [1, 3]:
            media_logo = get_logo_image(MEDIA_GROUP_LOGO_FILE)
            alpha = media_logo.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.65)
            media_logo.putalpha(alpha)
            logoWidth = int(max(back_img.width, back_img.height) / PROPORTION_BIGGER)
            logoHeight = int(logoWidth / PROPORTION)
            resized_media_logo = media_logo.resize((logoWidth, logoHeight))
            position = (
                LEFT_PADDING,
                back_img.height - resized_media_logo.height - UNDER_PADDING,
            )
            back_img.paste(resized_media_logo, position, resized_media_logo)

        if logo_choice in [2, 3]:
            tusur_logo = get_logo_image(TUSUR_LOGO_FILE)
            alpha = tusur_logo.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.65)
            tusur_logo.putalpha(alpha)
            original_width, original_height = tusur_logo.size
            max_width = back_img.width // 6.3
            max_height = back_img.height // 6.3
            scale = min(max_width / original_width, max_height / original_height)
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)
            resized_tusur_logo = tusur_logo.resize(
                (new_width, new_height), Image.LANCZOS
            )
            if back_img.width > back_img.height:
                position = (
                    back_img.width - new_width - RIGHT_PADDING,
                    back_img.height - new_height - UNDER_PADDING - 80,
                )
            else:
                position = (
                    back_img.width - new_width - RIGHT_PADDING,
                    back_img.height - new_height - UNDER_PADDING - 100,
                )

            back_img.paste(resized_tusur_logo, position, resized_tusur_logo)

        back_img = back_img.convert("RGB")
        back_img.save(os.path.join(output_folder, filename))


def processLogo(input_folder, output_folder, logo_choice):
    clear()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = [
        f
        for f in os.listdir(input_folder)
        if f.endswith((".jpg", ".jpeg", ".JPG", ".JPEG"))
    ]
    total_files = len(files)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, filename in enumerate(files):
            futures.append(
                executor.submit(
                    process_image, filename, input_folder, output_folder, logo_choice
                )
            )
            print_progress_bar(
                i + 1,
                total_files,
                prefix="Процесс обработки:",
                suffix="Готово",
                length=50,
            )
        for future in concurrent.futures.as_completed(futures):
            future.result()


def select_folders():
    root = tk.Tk()
    root.withdraw()

    input_folder = filedialog.askdirectory(title="Выберите папку с изображениями")
    if not input_folder:
        messagebox.showerror(
            "Ошибка", "Папка с изображениями не выбрана. Программа завершена."
        )
        sys.exit(1)

    output_folder = filedialog.askdirectory(
        title="Выберите папку для сохранения обработанных изображений"
    )
    if not output_folder:
        messagebox.showerror(
            "Ошибка", "Папка для сохранения не выбрана. Программа завершена."
        )
        sys.exit(1)

    return input_folder, output_folder


def main():

    input_folder, output_folder = select_folders()

    choice = menu()
    while choice != 4:
        if choice == 1:
            dpi = int(input("Введите значение dpi: "))
            processDPI(input_folder, output_folder, dpi)
            print("\nВсё готово <3")
        elif choice == 2:
            width = int(input("Ширина фоток: "))
            height = int(input("Высота фоток: "))
            dpi = int(input("Введите значение dpi: "))
            processResolution(input_folder, output_folder, dpi, width, height)
            print("\nВсё готово <3")
        elif choice == 3:
            logo_choice = logo_menu()
            if logo_choice == 4:
                choice = menu()
                continue
            processLogo(input_folder, output_folder, logo_choice)
            print("\nВсё готово <3")
        choice = menu()


if __name__ == "__main__":
    main()
