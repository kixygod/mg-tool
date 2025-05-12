import os
import sys
import concurrent.futures
from PIL import Image, ImageEnhance
import base64
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox
import multiprocessing

PROPORTION = 2.47
MEDIA_LOGO_WIDTH_PERCENT = 13.7
TUSUR_LOGO_WIDTH_PERCENT = 15.8
UNDER_PADDING_PERCENT = 3.0
LEFT_PADDING_PERCENT = 5.0
RIGHT_PADDING_PERCENT = 5.0

MEDIA_GROUP_LOGO_FILE = "mediagroup_logo.txt"
TUSUR_LOGO_FILE = "tusur_logo.txt"


def init_logos():
    try:
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        media_logo_path = os.path.join(base_path, MEDIA_GROUP_LOGO_FILE)
        if not os.path.exists(media_logo_path):
            raise FileNotFoundError(f"Logo file not found: {media_logo_path}")
        with open(media_logo_path, "r", encoding="utf-8") as f:
            logo_base64 = f.read().strip()
        logo_data = base64.b64decode(logo_base64)
        media_logo = Image.open(BytesIO(logo_data)).convert("RGBA")
        alpha = media_logo.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(0.65)
        media_logo.putalpha(alpha)

        tusur_logo_path = os.path.join(base_path, TUSUR_LOGO_FILE)
        if not os.path.exists(tusur_logo_path):
            raise FileNotFoundError(f"Logo file not found: {tusur_logo_path}")
        with open(tusur_logo_path, "r", encoding="utf-8") as f:
            logo_base64 = f.read().strip()
        logo_data = base64.b64decode(logo_base64)
        tusur_logo = Image.open(BytesIO(logo_data)).convert("RGBA")
        alpha = tusur_logo.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(0.65)
        tusur_logo.putalpha(alpha)

        return media_logo, tusur_logo
    except Exception as e:
        print(f"Ошибка загрузки логотипов: {e}")
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
        img.save(
            os.path.join(output_folder, filename),
            dpi=(dpi, dpi),
            quality=85,
            optimize=True,
        )


def process_resolution_image(filename, input_folder, output_folder, dpi, width, height):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.info["dpi"] = (dpi, dpi)
        img = img.resize((width, height), Image.LANCZOS)
        img.save(
            os.path.join(output_folder, filename),
            dpi=(dpi, dpi),
            quality=85,
            optimize=True,
        )


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

    with concurrent.futures.ProcessPoolExecutor(
        max_workers=os.cpu_count() + 2
    ) as executor:
        futures = []
        for filename in files:
            futures.append(
                executor.submit(
                    process_dpi_image, filename, input_folder, output_folder, dpi
                )
            )
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            future.result()
            completed += 1
            print_progress_bar(
                completed,
                total_files,
                prefix="Процесс обработки:",
                suffix="Готово",
                length=50,
            )


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

    with concurrent.futures.ProcessPoolExecutor(
        max_workers=os.cpu_count() + 2
    ) as executor:
        futures = []
        for filename in files:
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
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            future.result()
            completed += 1
            print_progress_bar(
                completed,
                total_files,
                prefix="Процесс обработки:",
                suffix="Готово",
                length=50,
            )


def process_image(
    filename, input_folder, output_folder, logo_choice, media_logo, tusur_logo
):
    with Image.open(os.path.join(input_folder, filename)) as img:
        back_img = img.copy()
        img_width, img_height = back_img.size

        if logo_choice in [1, 3]:
            logo_width = int(img_width * MEDIA_LOGO_WIDTH_PERCENT / 100)
            logo_height = int(logo_width / PROPORTION)
            resized_media_logo = media_logo.resize(
                (logo_width, logo_height), Image.LANCZOS
            )

            left_padding = int(img_width * LEFT_PADDING_PERCENT / 100)
            under_padding = int(img_height * UNDER_PADDING_PERCENT / 100)
            position = (
                left_padding,
                img_height - logo_height - under_padding,
            )
            back_img.paste(resized_media_logo, position, resized_media_logo)

        if logo_choice in [2, 3]:
            original_width, original_height = tusur_logo.size
            logo_width = int(img_width * TUSUR_LOGO_WIDTH_PERCENT / 100)
            logo_height = int(logo_width * original_height / original_width)
            resized_tusur_logo = tusur_logo.resize(
                (logo_width, logo_height), Image.LANCZOS
            )

            right_padding = int(img_width * RIGHT_PADDING_PERCENT / 100)
            under_padding = int(img_height * UNDER_PADDING_PERCENT / 100)
            vertical_offset = int(img_height / 100)

            position = (
                img_width - logo_width - right_padding,
                img_height - logo_height - under_padding - vertical_offset,
            )
            back_img.paste(resized_tusur_logo, position, resized_tusur_logo)

        back_img = back_img.convert("RGB")
        back_img.save(os.path.join(output_folder, filename), quality=85, optimize=True)


def processLogo(input_folder, output_folder, logo_choice, media_logo, tusur_logo):
    clear()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = [
        f
        for f in os.listdir(input_folder)
        if f.endswith((".jpg", ".jpeg", ".JPG", ".JPEG"))
    ]
    total_files = len(files)

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=os.cpu_count() + 2
    ) as executor:
        futures = []
        for filename in files:
            futures.append(
                executor.submit(
                    process_image,
                    filename,
                    input_folder,
                    output_folder,
                    logo_choice,
                    media_logo,
                    tusur_logo,
                )
            )
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            future.result()
            completed += 1
            print_progress_bar(
                completed,
                total_files,
                prefix="Процесс обработки:",
                suffix="Готово",
                length=50,
            )


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
    media_logo, tusur_logo = init_logos()
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
            processLogo(
                input_folder, output_folder, logo_choice, media_logo, tusur_logo
            )
            print("\nВсё готово <3")
        choice = menu()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
