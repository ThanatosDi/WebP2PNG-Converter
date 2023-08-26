from PIL import Image

class ImageConvert():
    def __init__(self): ...

    def convert(self, webp:str):
        image = Image.open(webp).convert("RGB")
        image.save(webp.replace(".webp", ".png"), "png")
