
from django.conf import settings
from django.core.files.storage import Storage
from django.utils.functional import cached_property

import requests
from requests.exceptions import RequestException

from urlparse import urljoin

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

WEBDAV_ROOT = settings.WEBDAV_ROOT
WEBDAV_PULIC = getattr(settings, 'WEBDAV_PUBLIC', WEBDAV_ROOT)

class WebDavStorage(Storage):

    @cached_property
    def session(self):
        return requests.Session()

    def _build_url(self, name, external=False):
        """
        Return the full URL for accessing the name.
        """
        return urljoin(WEBDAV_PUBLIC if external else WEBDAV_ROOT, name)

    def _request(self, method, name, **kwargs):
        resp = self.session.request(method, self._build_url(name), **kwargs)
        return resp

    def _open(self, name, mode='rb'):
        """
        Retrieves the specified file from storage.
        """
        resp = self._request('GET', name)
        assert resp.status_code == 200
        return StringIO(resp.content)

    def _save(self, name, content):
        """
        Saves new content to the file specified by name. The content should be
        a proper File object or any python file-like object, ready to be read
        from the beginning.
        """
        resp = self._request('PUT', name, data=content)
        return name

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
        resp = self._request('DELETE', name)

    def exists(self, name):
        """
        Returns True if a file referened by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
        resp = self._request('HEAD', name)
        return resp.status_code == 200

    def listdir(self, path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first item being directories, the second item being files.
        """
        resp = self._request('GET', path)
        # XXX?

    def size(self, name):
        """
        Returns the total size, in bytes, of the file specified by name.
        """
        resp = self._request('HEAD', name)
        return int(resp['content-lenght'])

    def url(self, name):
        """
        Returns an absolute URL where the file's contents can be accessed
        directly by a Web browser.
        """
        return self._build_url(name, external=True)

    ### django-filebrowser extensions

    def isdir(self, name):
        resp = self._request('HEAD', name)
        if resp.status_code == 404:
            return False
        # ?

    def isfile(self, name):
        resp = self._request('HEAD', name)
        if resp.status_code == 404:
            return False
        # ?

    def move(self, old_file_name, new_file_name, allow_overwrite=False):
        resp = self._request('MOVE', old_file_name,
            headers={
                'Destination': self._build_url(new_file_name),
            }
        )
        return resp.status_code == 201

    def makedirs(self, name):
        return True

    def rmtree(self, name):
        return True
