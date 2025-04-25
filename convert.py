import base64

# For MediaGroup
with open("path/to/mediagroup_logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")
    with open("mediagroup_logo.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(encoded)

# For TUSUR
with open("path/to/tusur_logo.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")
    with open("tusur_logo.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(encoded)
