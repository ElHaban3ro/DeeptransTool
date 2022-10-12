from urllib.request import Request, urlopen
import requests

from requests_html import HTMLSession
# a


from selenium import webdriver
# from webdriver_manager.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

import time


def file_translate(route:str, string_characters = 4999, l_from = 'en', l_to = 'es'):
    """
    Usa el "mejor traductor" del mundo para traducir archivos con python, y sin API key.
    
    
    Params
    =======
    
    route: Ruta del archivo a traducir.
    
    string_characters: cuantos caracteres contendrá el string que se traducirá (se hace por partes, por la limitación que tiene el mismo traductor). Usar como máximo 5000, y con margen de error.
    
    """
    
    
    
    
    
    f = open(route, 'r+')
    lines = f.readlines()
    
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
        # print(jumps)
        
    
    
    text_list = []
    
    
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
        string = string.replace('\n', '%0A') # Para los saltos de linea!
        string = string.replace('?', '%3F') # Para los signos de interrogación.
        
    
        string = string.replace('<i>', '--i--') # Para éstas etiquetas, que al parecer daban bug.
        string = string.replace('</i>', '--ci--') # Para éstas etiquetas, que al parecer daban bug.
        
        
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
    
    
    text_translate = ''
    
    
    
    print('Traduciendo subtitulos!')
    
    browser = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
    
    for link_part in urls_list:
        browser.get(link_part)
        time.sleep(5) # Verificar si es necesario usar esto!

        translate_save = browser.find_element(By.ID, 'target-dummydiv')

        text_translate = text_translate + translate_save.get_attribute('outerHTML')[103:-8]
        # print(translate_save.get_attribute('outerHTML')[103:-8])



        



    
    text_translate = text_translate.replace('--8', '-->') # Para los espacios!
    text_translate = text_translate.replace('--i--', '<i>') # Para éstas etiquetas, que al parecer daban bug.
    text_translate = text_translate.replace('--ci--', '</i>')

    translate_web = open(route, 'w+')
    translate_web.truncate()
    
    translate_web.write(text_translate)
    
    
    translate_web.close()
    browser.close()
    
    
    
    print(f'Se ha traducido correctamente el archivo de texto {route}')