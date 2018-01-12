from setuptools import setup, find_packages


with open("README.rst", "r") as f:
	readme = f.read()

setup(
	name="pgbackup",
	version="0.1.0",
	description="Database backups",
	long_description=readme,
	author='Ayoubensalem',
	author_email='ayoubensalem@gmail.com',
	packages=find_packages('src'),
	package_dir={'':'src'},
	install_requires=[],
    entry_points={
            'console_scripts': [
                'pgbackup=pgbackup.cli:main'],
        }
)
