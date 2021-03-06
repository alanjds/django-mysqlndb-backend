import sys

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


if sys.version_info[0] == 3:
    mysql_req = "mysqlclient>=1.3.6"
else:
    mysql_req = "MySQL-python>=1.2.2"


setup(
    name='django-mysqlndb-backend',
    version='1.1.0',
    author_email='programmers@theatlantic.com',
    packages=['mysqlndb'],
    url='https://github.com/theatlantic/django-mysqlndb-backend',
    description='Provides a django database backend that works with MySQL Cluster\'s NDB storage engine.',
    install_requires=[
        "Django >= 1.4",
        mysql_req,
        'six>=1.7.0',
        'django-transaction-hooks >= 0.2',
    ],
)
