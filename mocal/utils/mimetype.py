# -*- conding: utf-8-*-
import mimetypes
import os


def get_mimetype(filename):
    ext = os.path.splitext(filename)[-1]
    return mimetypes.types_map[ext]
