# Selenium Imports!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Web Driver Import:
from webdriver_manager.chrome import ChromeDriverManager


# PDF reader.
from PyPDF2 import PdfReader




# Others Imports:
import time
import os





def file_translate(route:str, string_characters = 4999, l_from = 'en', l_to = 'es', new_file = True, new_file_extension = 'txt'):
    """
       Use the world's "best translator" to translate files with python, and without API key.
    
    
    Params
    =======
    
    route: STR | Path of the file to translate.
    
    string_characters: INT | how many characters will contain the string to be translated (it is done by parts, by the limitation that has the same translator). Use at most 5000, and with margin of error.
    
    l_from: STR | Language of origin. Generally the first acronym of the original language is used! An example of this is "Español", its acronym being "es". If you have any doubts about the acronym of your source or target language, check the website DeepL.

    l_to: STR | Target Language. Generally the first acronym of the original language is used! An example of this is "English", its acronym being "en". If you have any doubts about the acronym of your source or target language, check the website DeepL.

    new_file: BOOL | If you want the translation of the file to be done on a new one, you should activate this option.

    new_file_extension: STR | If the previous option is True (new_file), you have to provide a valid file extension for the new file. If it is not provided, your new extension will be assumed to be txt.


    Return
    =======

    No return new values, only save the file!

    
    """
    
    # Sacar el nombre del archivo sin extensión.
    file_without_extension = os.path.basename(route)[::-1]
    file_without_extension = file_without_extension[file_without_extension.find('.'):][::-1][:-1]


    # Ahora, por separado, sacamos la extensión del archivo.
    extension_file = os.path.basename(route)[::-1]
    extension = extension_file[:extension_file.find('.')][::-1]
    


    # Extensiones de texto validas que usaremos!
    text_files_extensions = ['srt', 'txt', 'html', 'log', 'csv', 'pdf']



    # ============================
    # Exceptions!!

    if string_characters >= 5000:
        raise Exception('(MaxCharactersError, error 01) Sorry :(, we have limitations with the web, therefore, as maximum characters at a time, we can translate 4999 per string. What we do, is that we pass strings of this length to the browser, when we already split your text into small pieces.')

    elif extension not in text_files_extensions:
        raise ValueError('(FileExtensionError, error 03) The file you provided seems not to be a valid text file :c')


    elif new_file_extension == 'pdf':
        raise ValueError("(PDFCreateError, error 04) Sorry, we can't build a pdf from your main file (is pdf file) :( Choose as output of your new file, a valid plain text extension!")

    elif new_file == False and extension == 'pdf':
        raise ValueError('(PDFNewFileError, error 05) If you want to translate a pdf file, it is mandatory to create a new file :/. Fix this error by setting new_file to True.')
    # ============================




    if extension != 'pdf':
        f = open(route, 'r+', encoding = 'utf-8')
        lines = f.readlines()

    else:
        print('(EXPERIMENTAL PDF FUNCTION ALERT!) Your file is a PDF! Remember, working with PDF files can lead to serious problems with how paragraphs and text are constructed, so you may experience line breaks and tab errors in your text.\n\n')



        lines = []
        pdf_r = PdfReader(route)
        pdf_number_page = len(pdf_r.pages)

        for page_n in list(range(0, pdf_number_page, 1)):
            page = pdf_r.pages[page_n]


            text = str(page.extract_text()).split('\n')

            for line in text:
                lines.append(line)


    
    lines_to_translate = []
    raw_consult_url = f'https://www.deepl.com/translator#{l_from}/{l_to}/' # URL del traductor
    raw_text = ''

    
    for raw_line in lines: # Inserto TODO en una sola linea. Esto para trabajar
                           # mejor con la cantidad de carácteres.
        raw_text = raw_text + raw_line


    if len(raw_text) > 5000:
        jumps = list(range(0, len(raw_text), string_characters)) # Generamos una lista con los 
                                                                 # saltos necesarios de con saltos 
                                                                 # de {string_characters}
        
        jumps.append(len(raw_text))
        

    else:
        jumps = [0, len(raw_text)]

        
    
    
    text_list = []
    
    # ====================================
    text_re = raw_text.split(' ')


    # print(text_re)
    temp_list = []
    temp_text = ''

    for tb in text_re:

        if len(tb) > string_characters:
            print(f'Algún texto contiene más de {string_characters} letras. Quiere decir que tiene más de 5000 carácteres sin ningún espacio, cosa extraña.')


        elif len(temp_text) + len(tb) <= string_characters:
            temp_text = temp_text + f' {tb}'
            temp_list.append(temp_text)

        else:
            temp_text = tb
            temp_list.append(tb)





    # for c, tb in enumerate(text_re):
    #     if len(re) + len(tb) <= string_characters:
    #         re = re + f' {tb}'
        
    #     else:
    #         re_list.append(re)
    #         re = ''

            
    #         for d in range(c):
    #             text_re.pop(0)
                
            
    #     continue

            
    # print(text_re)
        




    # for r in range(len(text_re)):
    #     for c, tb in enumerate(text_re):
    #         if len(re) + len(tb) <= string_characters:
    #             re = re + f' {tb}'

    #         text_re.remove(tb)
    #     re_list.append(re)
    #     continue

    # print(re_list)


    # =====================================
    
    
    for e, jump in enumerate(jumps[:-1]): # Separamos el string teniendo en cuenta los saltos.
        
        
        if e != len(jumps) - 2:
            text_list.append(raw_text[jump:jumps[e + 1]])   
            
        elif e == len(jumps) - 2:
            text_list.append(raw_text[jump:])
            
            # print(len(raw_text[jump:]))
    
        
    
    processed_list = []
    
    for string in text_list: # Remplazamos con los caracteres clave que usa DeepL. Luego usaremos
                             # esto mismo, pero a la inversa, para obtener nuevamente el string
                             # virgen.
                
        string = string.replace(' ', '%20') # Para los espacios!
        string = string.replace(',', '%2C') # Para los espacios!
        string = string.replace('\t', r'%20%20%20%20') # Para los espacios!
        string = string.replace('\n', '%0A') # Para los saltos de linea!
        string = string.replace('?', '%3F') # Para los signos de interrogación.
        
    
        string = string.replace('<i>', '--i--') # Para éstas etiquetas, que al parecer daban bug.
        string = string.replace('</i>', '--ci--') # Para éstas etiquetas, que al parecer daban bug.
        string = string.replace('/', r'%5C%2F')
        string = string.replace('\\', r'%5C%5C')
        string = string.replace('\\', r'%5C%5C')
        
        
        string = string.replace('-->', '--8') # Para este tipo de signo (o conjunto de singos) y que no de bug. Luego volvemos todo a la normalidad.
        
        

        processed_list.append(string)

    
    
    
    # Generemos la URL de consulta con cada uno de los strings.
    
    urls_list = []
    
    for string_processed in processed_list:
        url_pro = raw_consult_url + string_processed
        urls_list.append(url_pro)
        
    

    
    
    
    chrome_options = Options()
    chrome_options.headless = True # Para que se ejecute sin una interfaz grafica.
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--version')
    
    
    
    text_translate = ''
    
    # print(urls_list)
    
    print('Traduciendo archivo!!')

    browser = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
    
    for link_part in urls_list:


        browser.get(link_part)
        
        time.sleep(5) #TODO USAR ES NECESARIO. EL TIEMPO DE ESPERA PUEDE VARIAR, VER QUE TAL FUNCIONA CON UN TIEMPO MÁS BAJO. 

        translate_save = browser.find_element(By.ID, 'target-dummydiv')

        text_translate = text_translate + translate_save.get_attribute('outerHTML')
        text_f = text_translate[text_translate.find('>') + 1:-8]



    
    text_f = text_f.replace('--8', '-->') # Para los espacios!
    text_f = text_f.replace('--i--', '<i>') # Para éstas etiquetas, que al parecer daban bug.
    text_f = text_f.replace('--ci--', '</i>')




    
    # Si el usuario decide que quiere la traducción en un nuevo archivo, creamos el archivo.
    if new_file == True:
        if new_file_extension in text_files_extensions:
            new_name = f'{os.path.dirname(route)}/[DTT] {file_without_extension}.{new_file_extension}'
            new_f = open(new_name, 'w+')
            new_f.close()


            translate_web = open(new_name, 'wb+')
            translate_web.write(text_f.encode())

            translate_web.close()

        else:
            raise ValueError('(NewFileExtensionError, error 02): The text extension for the new file is wrong or does not exist! Check it.')

        

    else:
        translate_web = open(route, 'wb+')
        translate_web.truncate()
        
        translate_web.write(text_f.encode())
        
        
        translate_web.close()



    browser.close() # Se cierra el navegador para que no consuma recursos obviamente.
    
    
    
    print(f'\n\nSe ha traducido correctamente el archivo de texto {route}\n\n')






def string_translate(text, string_characters = 4999, l_from = 'en', l_to = 'es'):
    """
    Use the world's "best translator" to translate any text and make use of it, without any restrictions!
    
    
    Params
    =======
    
    text: STR | Text to translate!
    
    string_characters: INT | how many characters will contain the string to be translated (it is done by parts, by the limitation that has the same translator). Use at most 5000, and with margin of error.
    
    l_from: STR | Language of origin. Generally the first acronym of the original language is used! An example of this is "Español", its acronym being "es".

    l_to: STR | Target Language. Generally the first acronym of the original language is used! An example of this is "English", its acronym being "en".


    Return
    =======

    Return the text translate.

    
    """



    # ============================
    # Exceptions!!

    if string_characters >= 5000:
        raise Exception('(MaxCharactersError, error 01) Sorry :(, we have limitations with the web, therefore, as maximum characters at a time, we can translate 4999 per string. What we do, is that we pass strings of this length to the browser, when we already split your text into small pieces.')

    # ============================



                                                                # saltos necesarios de con saltos 
                                                                # de {string_characters}
    
    

    if len(text) >= 5000: # A comparación con la función anterior, acá directamente espliteamos el texto, haciendo el proceso más rápido.
        jumps = list(range(0, len(text), string_characters)) # Generamos una lista con los 
        jumps.append(len(text))


    else:
        jumps = [0, len(text)]

        
    
    # =====================================
    
    
    
    
    text_list = []
    
    for e, jump in enumerate(jumps[:-1]): # Separamos el string teniendo en cuenta los saltos.
        
        
        if e != len(jumps) - 2:
            text_list.append(text[jump:jumps[e + 1]])   
            
        elif e == len(jumps) - 2:
            text_list.append(text[jump:])
            
    

    
    raw_consult_url = f'https://www.deepl.com/translator#{l_from}/{l_to}/' # URL del traductor



    
    processed_list = []
    
    for string in text_list: # Remplazamos con los caracteres clave que usa DeepL. Luego usaremos
                             # esto mismo, pero a la inversa, para obtener nuevamente el string
                             # virgen. 
                             #TODO: VER SI NECESITO AÑADIR/CAMBIAR OTROS CARACTERES (que casi seguro que sí).
                
        string = string.replace(' ', '%20') # Para los espacios!
        string = string.replace(',', '%2C') # Para los espacios!
        string = string.replace('\t', r'%20%20%20%20') # Para los espacios!
        string = string.replace('\n', '%0A') # Para los saltos de linea!
        string = string.replace('?', '%3F') # Para los signos de interrogación.
        
    
        string = string.replace('<i>', '--i--') # Para éstas etiquetas, que al parecer daban bug.
        string = string.replace('</i>', '--ci--') # Para éstas etiquetas, que al parecer daban bug.
        string = string.replace('/', r'%5C%2F')
        string = string.replace('\\', r'%5C%5C')
        string = string.replace('\\', r'%5C%5C')
        
        
        string = string.replace('-->', '--8') # Para este tipo de signo (o conjunto de singos) y que no de bug. Luego volvemos todo a la normalidad.
        
        

        processed_list.append(string)

    
    
    
    # Generemos la URL de consulta con cada uno de los strings.
    
    urls_list = []
    
    for string_processed in processed_list:
        url_pro = raw_consult_url + string_processed
        urls_list.append(url_pro)
        
    # print(urls_list[-1])
    
        

        
        
        # break # TODO: quitar este break.
    

    
    
    
    chrome_options = Options()
    chrome_options.headless = True # Para que se ejecute sin una interfaz grafica.
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--version')
    
    
    
    text_translate = ''
    
    
    
    print('Traduciendo el texto!!')

    browser = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
    
    for link_part in urls_list:
        browser.get(link_part)
        time.sleep(5) # USAR ES NECESARIO.

        translate_save = browser.find_element(By.ID, 'target-dummydiv')

        text_translate = text_translate + translate_save.get_attribute('outerHTML')
        text_f = text_translate[text_translate.find('>') + 1:-8]


        



    
    text_f = text_f.replace('--8', '-->') # Para los espacios!
    text_f = text_f.replace('--i--', '<i>') # Para éstas etiquetas, que al parecer daban bug.
    text_f = text_f.replace('--ci--', '</i>') # Para las de cierre.
    browser.close() # Se cierra el navegador para que no consuma recursos obviamente.



    
    
    
    print(f'\n\nSe ha traducido correctamente el texto!\n\n')

    return text_f




a = file_translate('C:/Users/ferdh/Downloads/Izquierda.txt', 4999, 'es', 'en', True, 'txt')