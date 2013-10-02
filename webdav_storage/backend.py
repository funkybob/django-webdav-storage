
from django.core.files.storage import Storage
import requests

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class WebDavStorage(Storage):
    def open(self, name, mode='rb'):
        """
        Retrieves the specified file from storage.
        """
        pass

    def save(self, name, content):
        """
        Saves new content to the file specified by name. The content should be
        a proper File object or any python file-like object, ready to be read
        from the beginning.
        """
        pass

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
    def exists(self, name):
        """
        Returns True if a file referened by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
    def listdir(self, path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first item being directories, the second item being files.
        """
    def size(self, name):
        """
        Returns the total size, in bytes, of the file specified by name.
        """
    def url(self, name):
        """
        Returns an absolute URL where the file's contents can be accessed
        directly by a Web browser.
        """
    def accessed_time(self, name):
        """
        Returns the last accessed time (as datetime object) of the file
        specified by name.
        """
    def created_time(self, name):
        """
        Returns the creation time (as datetime object) of the file
        specified by name.
        """
    def modified_time(self, name):
        """
        Returns the last modified time (as datetime object) of the file
        specified by name.
        """

