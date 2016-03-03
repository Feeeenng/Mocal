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

    def save_io(self):
        img_io = StringIO()
        self.out.save(img_io, 'png')
        img_io.seek(0)
        return img_io

    def save_fp(self, filename):
        self.out.save(filename)


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
