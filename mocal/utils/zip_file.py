# -*- coding: utf-8 -*-
import zipfile
from cStringIO import StringIO


class InMemoryZip(object):
    def __init__(self):
        # Create the in-memory file-like object
        self.in_memory_zip = StringIO()

    def append(self, filename_in_zip, file_contents):
        '''Appends a file with name filename_in_zip and contents of
        file_contents to the in-memory zip.'''

        # Get a handle to the in-memory zip in append mode
        zf = zipfile.ZipFile(self.in_memory_zip, "a", zipfile.ZIP_DEFLATED, False)

        # Write the file to the in-memory zip
        zf.writestr(filename_in_zip, file_contents)  # 添加压缩文件的子文件名和内容

        # Mark the files as having been created on Windows so that
        # Unix permissions are not inferred as 0000
        for zfile in zf.filelist:
            zfile.create_system = 0
        return self

    def read(self):
        '''Returns a string with the contents of the in-memory zip.'''
        self.in_memory_zip.seek(0)
        return self.in_memory_zip.read()

    def write(self, filename=None):
        if filename:
            f = file(filename, "w")
            f.write(self.read())
            f.close()
            return None
        else:
            self.out_memory_zip = StringIO()
            self.out_memory_zip.write(self.read())
            self.out_memory_zip.seek(0)
            return self.out_memory_zip

# if __name__ == "__main__":
#     # Run a test
#     imz = InMemoryZip()
#     imz.append("test.txt", "Another test").append("test2.txt", "Still another")
#     imz.write("test.zip")  # have a file in local
#     f = imz.write()  # io stream, send_file(io, attachment_filename='test.zip', as_attachment=True)
