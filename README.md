django-webdav-storage
=====================

A storage backend for Django that works across authenticated WebDAV

Configuring nginx
-----------------

http://wiki.nginx.org/HttpDavModule

- to support PUT, your temporary file path (given by directive
  `client_body_temp_path` in the location section) must be on the same
  partition as the destination.

- The `create_full_put_path` setting must be 'on'


Settings
--------

`WEBDAV_ROOT`

Where the storage should pass requests.
e.g. "http://media.mysite.com/path/to/media/"

`WEBDAV_PUBLIC`

(Optional) the public root for accessing files.
Defaults to `WEBDAV_ROOT`
