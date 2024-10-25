class Image:
    def __init__(self, title, resolution, extension):
        self.title = title
        self.resolution = resolution
        self.extension = extension

    def resize(self, new_resolution):
        """Метод для изменения разрешения изображения."""
        self.resolution = new_resolution
        print(f"Изображение '{self.title}' изменено на разрешение {
              self.resolution}")


image1 = Image("Пейзаж", "1920x1080", "jpg")
image2 = Image("Портрет", "800x600", "png")
image3 = Image("Архитектура", "2560x1440", "bmp")

image1.resize("1280x720")
image2.resize("1024x768")
image3.resize("3840x2160")

print(f"{image1.title}: {image1.resolution}, {image1.extension}")
print(f"{image2.title}: {image2.resolution}, {image2.extension}")
print(f"{image3.title}: {image3.resolution}, {image3.extension}")
