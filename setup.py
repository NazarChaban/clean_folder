from setuptools import setup

setup(
    name='clean_folder',
    version='1.2',
    description='Sort your directory',
    url='https://github.com/Vivern0/Sorter',
    author='Vivern0',
    author_email='chaban.nazar.2@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sorter']},
    include_package_data=True
)
