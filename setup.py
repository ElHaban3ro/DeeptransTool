from setuptools import setup


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()




setup(
    name = 'DeeptransTool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['DTT'],
    version = '1.1',
    license = 'GPLv3',
    description = "Want to translate using the world's best translator, DeepL, but don't want to give out your credit card? Use DeeptransTool and translate EVERYTHING you want, for FREE! Here is a solution for accessing the DeepL API with Python. 🐸",
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/DeeptransTool',
    keywords = ['Translate', 'DeepL', 'Traduccion', 'API', 'Translation'],
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=['selenium==4.5.0', 'webdriver-manager==3.8.3']
)