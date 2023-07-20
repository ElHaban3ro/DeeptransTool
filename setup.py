from setuptools import setup


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()




setup(
    name = 'DeeptransTool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['DTT'],
    version = '1.4',
    license = 'GPLv3',
    description = "Use the world's best translator (DeepL) to translate your text files or text itself!! All without having to provide your credit card or be limited by the API. 🐸",
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/DeeptransTool',
    keywords = ['Translate', 'DeepL', 'Traduccion', 'API', 'Translation'],
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=['selenium==4.5.0', 'webdriver-manager==3.8.3', 'PyPDF2', 'beautifulsoup4==4.12.2']
)