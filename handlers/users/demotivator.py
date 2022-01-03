from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import os

# Тема автора скрипта - https://lolz.guru/threads/3115189/

class Demotivator:
    def __init__(self, top_text='', bottom_text=''):
        self._top_text = top_text
        self._bottom_text = bottom_text

    def create(self, file: str, watermark=None, result_filename='demresult.jpg',
               font_color='white', fill_color='black',
               font_name='times.ttf', top_size=80, bottom_size=60,
               arrange=False, use_url=False, delete_file=False) \
            -> bool:  # Returns True if method executed successfully

        if use_url:
            p = requests.get(file)
            out = open(r'demotivator_picture.jpg', "wb")
            out.write(p.content)
            out.close()

            file = 'demotivator_picture.jpg'

        """
        Создаем шаблон для демотиватора
        Вставляем фотографию в рамку
        """

        if arrange:
            user_img = Image.open(file).convert("RGBA")
            (width, height) = user_img.size
            img = Image.new('RGB', (width + 250, height + 260), color=fill_color)
            img_border = Image.new('RGB', (width + 10, height + 10), color='#000000')
            border = ImageOps.expand(img_border, border=2, fill='#ffffff')
            img.paste(border, (111, 96))
            img.paste(user_img, (118, 103))
            drawer = ImageDraw.Draw(img)
        else:
            img = Image.new('RGB', (1280, 1024), color=fill_color)
            img_border = Image.new('RGB', (1060, 720), color='#000000')
            border = ImageOps.expand(img_border, border=2, fill='#ffffff')
            user_img = Image.open(file).convert("RGBA").resize((1050, 710))
            (width, height) = user_img.size
            img.paste(border, (111, 96))
            img.paste(user_img, (118, 103))
            drawer = ImageDraw.Draw(img)

        """Подбираем оптимальный размер шрифта
        
        Добавляем текст в шаблон для демотиватора

        """
        font_1 = ImageFont.truetype(font=font_name, size=top_size, encoding='UTF-8')
        text_width = font_1.getsize(self._top_text)[0]

        while text_width >= (width + 250) - 20:
            font_1 = ImageFont.truetype(font=font_name, size=top_size, encoding='UTF-8')
            text_width = font_1.getsize(self._top_text)[0]
            top_size -= 1

        font_2 = ImageFont.truetype(font=font_name, size=bottom_size, encoding='UTF-8')
        text_width = font_2.getsize(self._bottom_text)[0]

        while text_width >= (width + 250) - 20:
            font_2 = ImageFont.truetype(font=font_name, size=bottom_size, encoding='UTF-8')
            text_width = font_2.getsize(self._bottom_text)[0]
            bottom_size -= 1

        size_1 = drawer.textsize(self._top_text, font=font_1)
        size_2 = drawer.textsize(self._bottom_text, font=font_2)

        if arrange:
            drawer.text((((width + 250) - size_1[0]) / 2, ((height + 190) - size_1[1])),
                        self._top_text, fill=font_color,
                        font=font_1)
            drawer.text((((width + 250) - size_2[0]) / 2, ((height + 235) - size_2[1])),
                        self._bottom_text, fill=font_color,
                        font=font_2)
        else:
            drawer.text(((1280 - size_1[0]) / 2, 840), self._top_text, fill=font_color, font=font_1)
            drawer.text(((1280 - size_2[0]) / 2, 930), self._bottom_text, fill=font_color, font=font_2)

        if watermark is not None:
            (width, height) = img.size
            idraw = ImageDraw.Draw(img)

            idraw.line((1000 - len(watermark) * 5, 817, 1008 + len(watermark) * 5, 817), fill=0, width=4)

            font_2 = ImageFont.truetype(font=font_name, size=20, encoding='UTF-8')
            size_2 = idraw.textsize(watermark.lower(), font=font_2)
            idraw.text((((width + 729) - size_2[0]) / 2, ((height - 192) - size_2[1])),
                       watermark.lower(), font=font_2)

        img.save(result_filename)

        if delete_file:
            os.remove(file)

        return True
