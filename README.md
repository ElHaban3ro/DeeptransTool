# DeeptransTool

[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-yellowgreen.svg?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_DeeptransTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/DeeptransTool/)

*The package is still under development, you may find serious bugs or features like the pdf translator still missing. Any serious bugs please let me know by discord!*


## Summary and details
---
The **perfect** module to make ***translations*** with no character limitations, ***no need to pay and no need to give your bank details*** to access the API of ***DeepL***. Translate the main ***text files*** (soon also pdf's) or give the ***text directly***!

To fulfill the **purpose**, we make use of ***Selenium*** and the browser [Chrome](https://www.google.com/chrome/) therefore, it is ***necessary** to have the browser installed ***on your computer***. If you are on **windows**, download the ***latest version***, if you are on ***linux***, we recommend you to download [this](https://github.com/ElHaban3ro/DeeptransTool/blob/main/packages/google-chrome-linux64-105.0.5195.125.deb?raw=true) version. 



## (v1.3) ¿What's New?
---
- Support for reading and translating PDF's. (Remember that pdf's are a more complex file type than a simple txt or srt, therefore, when creating a new file you may experience line breaks that are not applicable or not applicable at all, this, because of how a pdf is composed). You can use the function to translate PDF's ONLY by creating a new file.
- Error handling.
- Support for more characters (it is a problem how some signs that are passed by the url are translated, therefore, signs like "/", are translated by the translator as "%5C%2F", and if they are not corrected, they can cause serious problems. I will be attentive to your feedback to add this kind of characters to the package so that they do not cause errors).

- A better way to cut the text and pass it to DeepL (apparently, it sometimes caused errors due to words being cut off).


## Functions
---

#### - file_translate(route, string_characters, l_from, l_to, new_file, new_file_extension)
> Use the world's "best translator" to translate files with python, and without API key.
>
- ***Parameters:*** 
    
    - route: **STR** | Path of the file to translate.
    
    - string_characters: **INT** | how many characters will contain the string to be translated (it is done by parts, by the limitation that has the same translator). Use at most 5000, and with margin of error.
    
    - l_from: **STR** | Language of origin. Generally the first acronym of the original language is used! An example of this is "Español", its acronym being "es". If you have any doubts about the acronym of your source or target language, check the website DeepL.

    - l_to: **STR** | Target Language. Generally the first acronym of the original language is used! An example of this is "English", its acronym being "en". If you have any doubts about the acronym of your source or target language, check the website DeepL.

    - new_file: **BOOL** | If you want the translation of the file to be done on a new one, you should activate this option.

    - new_file_extension: **STR** | If the previous option is True (new_file), you have to provide a valid file extension for the new file. If it is not provided, your new extension will be assumed to be txt.




#### - string_translate(text, string_characters, l_from, l_to)
> Use the world's "best translator" to translate any text and make use of it, without any restrictions!
>
- ***Parameters:*** 
    - text: **STR** | Text to translate!
    
    - string_characters: **INT** | how many characters will contain the string to be translated (it is done by parts, by the limitation that has the same translator). Use at most 5000, and with margin of error.
    
    - l_from: **STR** | Language of origin. Generally the first acronym of the original language is used! An example of this is "Español", its acronym being "es".

    - l_to: **STR** | Target Language. Generally the first acronym of the original language is used! An example of this is "English", its acronym being "en".


- ***Return:***
    Return the text translate.
    


## Installation and Use!
---

#### Installation:
To use this package, the best idea is to do it through ***pip***:
```bash
pip install DeeptransTool
```
***IT IS VERY IMPORTANT THAT THE "D" AND THE "T" ARE CAPITALIZED.***


Or, on the contrary, you can **clone** this repository and access it:
```bash
git clone https://github.com/ElHaban3ro/DeeptransTool
```

This will create a folder of the project itself inside your python root project. Next we have to install the necessary dependencies for the project to work correctly, this can be done with:
```bash
pip install -r requirements.txt 
```

This would **ideally** have to install all the necessary libraries for you. This will be installed in the ***virtual environment*** of your project. See how to create a [virtual environment here]('https://docs.python.org/3/tutorial/venv.html').


In addition to this, remember to have the ***Chrome*** browser installed on your ***device***. Remember that, if you are on ***Windows***, you should install the ***latest version***, and if you are on ***linux***, [install the version that ***I leave*** in my repository](https://github.com/ElHaban3ro/DeeptransTool/blob/main/packages/google-chrome-linux64-105.0.5195.125.deb?raw=true) (Any problem, contact me by ***Discord*** or ***Twitter***).



#### Use:
To use this package of this form:
```python
from DTT.deepLTranslate import file_translate


mi_traduccion = file_translate('C:/miruta/archivo.txt', 4999, 'es', 'en', True, 'srt')
```

#### Text Files Allow:
- srt
- txt
- html
- log
- csv
- pdf

***¿more? Send it***



# Autor Contact
---

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro) [![Contact Discord](https://img.shields.io/badge/Discord-!%20Die()%231274-lightgray?style=for-the-badge&logo=discord)](https://discord.com) [![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)