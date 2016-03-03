# -*- coding: utf-8 -*-

from PIL import Image
from cStringIO import StringIO


class ImgOperate:
    def __init__(self, fp_or_buffer):
        self.im = Image.open(fp_or_buffer)
        self.format = self.im.format
        self.mode = self.im.mode
        self.out = None

    # 缩略图（按最长的边来， 较短的边填充）
    def real_thumbnail(self, width_or_height, border=0, border_color=(255, 255, 255)):
        inner_len = width_or_height - 2 * border
        size = inner_len, inner_len
        self.im.thumbnail(size)
        w, h = self.im.size
        if max(w, h) >= inner_len:
            self.out = Image.new('RGB', (width_or_height, width_or_height), border_color)  # 背景
            out = Image.new('RGB', (inner_len, inner_len), (255, 255, 255))  # 内嵌背景
            if w > h:
                y1 = (inner_len - h) / 2
                y2 = y1 + h
                box = (0, y1, inner_len, y2)
                out.paste(self.im, box)
                self.out.paste(out, (border, border, border + inner_len, border + inner_len))
            else:
                x1 = (inner_len - w) / 2
                x2 = x1 + w
                box = (x1, 0, x2, inner_len)
                out.paste(self.im, box)
                self.out.paste(out, (border, border, border + inner_len, border + inner_len))

    # 缩略图（按最长的边来， 较短的边不填充）
    def thumbnail(self, width, height):
        size = width, height
        self.im.thumbnail(size)
        self.out = self.im

    # 固定大小（失真）
    def resize(self, width, height):
        self.out = self.im.resize((width, height))

    # 裁剪
    def center_cut(self, width, height):
        w, h = self.im.size
        x1 = (w - width) / 2
        y1 = (h - height) / 2
        x2 = x1 + width
        y2 = y1 + height
        box = (x1, y1, x2, y2)  # 以左上角为（0，0）的坐标系统， 参数（左，上，右，下）
        self.out = self.im.crop(box) # 按box在im图片对象中裁剪出一个区域

    # 水印
    def water_mark(self, im, text=u'mocal.cn', font_size=25, position='right_bottom', opacity=0.9, font_color=(0, 0, 0)):
        mark = text2img(text, font_color, font_size)
        image = watermark(im, mark, position, opacity)
        if image:
            self.out = image
        else:
            print "Sorry, Failed."

    def save_io(self):
        img_io = StringIO()
        self.out.save(img_io, 'png')
        img_io.seek(0)
        return img_io

    def save_fp(self, filename):
        self.out.save(filename)


import Image, ImageEnhance, ImageDraw, ImageFont


def text2img(text, font_color=(0, 0, 0), font_size=25):
    """生成内容为 TEXT 的水印"""

    font = ImageFont.truetype('static/font/DRUMSN__.TTF', font_size)
    #多行文字处理
    text = text.split('\n')
    mark_width = 0
    for i in range(len(text)):
        (width, height) = font.getsize(text[i])
        if mark_width < width:
            mark_width = width
    mark_height = height * len(text)

    #生成水印图片
    mark = Image.new('RGBA', (mark_width, mark_height))
    draw = ImageDraw.ImageDraw(mark, "RGBA")
    draw.setfont(font)
    for i in range(len(text)):
        (width, height) = font.getsize(text[i])
        draw.text((0, i * height), text[i], fill=font_color)
    return mark


def set_opacity(im, opacity):
    """设置透明度"""

    assert opacity >=0 and opacity < 1
    if im.mode != "RGBA":
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def watermark(im, mark, position, opacity=1):
    """添加水印"""

    try:
        if opacity < 1:
            mark = set_opacity(mark, opacity)
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        if im.size[0] < mark.size[0] or im.size[1] < mark.size[1]:
            print "The mark image size is larger size than original image file."
            return False

        #设置水印位置
        if position == 'left_top':
            x = 0
            y = 0
        elif position == 'left_bottom':
            x = 0
            y = im.size[1] - mark.size[1]
        elif position == 'right_top':
            x = im.size[0] - mark.size[0]
            y = 0
        elif position == 'right_bottom':
            x = im.size[0] - mark.size[0]
            y = im.size[1] - mark.size[1]
        else:
            x = (im.size[0] - mark.size[0]) / 2
            y = (im.size[1] - mark.size[1]) / 2

        layer = Image.new('RGBA', im.size,)
        layer.paste(mark, (x, y))
        return Image.composite(layer, im, layer)
    except Exception as e:
        print ">>>>>>>>>>> WaterMark EXCEPTION:  " + str(e)
        return False


# img_op = ImgOperate('4.jpg')
# img_op.real_thumbnail(256, border=10, border_color=(128, 128, 128))
# img_op.out.show()

# img_op = ImgOperate('3.jpg')
# img_op.thumbnail(256, 256)
# img_op.out.show()

# img_op = ImgOperate('3.jpg')
# img_op.resize(256, 256)
# img_op.out.show()

# img_op = ImgOperate('4.jpg')
# img_op.center_cut(100, 100)
# img_op.out.show()

# from urllib import urlopen
# src = 'http://cdn.17zuoye.com/fs-image/fc46cf853b767771f6dd49790c6dd743'
# file = StringIO(urlopen(src).read())
# img_op = ImgOperate(file)
# img_op.real_thumbnail(46)
# if img_op.out:
#     img_op.out.show()
