from setuptools import setup, find_packages

setup(
    name='django-webdav-storage',
    version='0.0.1',
    description='WebDAV storage backend for Django',
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    url='http://github.com/funkybob/django-webdav-storage',
    keywords=['django', 'storage'],
    packages = find_packages(exclude=['tests.*']),
    zip_safe=False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    requires = [
        'Django (>=1.5)',
        'requirements (>=2.0)',
    ],
)
