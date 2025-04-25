import base64

image_path = r"D:\mg-tool\Logo_TUSUR.png"
output_file = "tusur_logo.txt"

with open(image_path, "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")


with open(output_file, "w", encoding="utf-8") as txt_file:
    txt_file.write(encoded)

print(f"Base64 строка сохранена в {output_file}")
