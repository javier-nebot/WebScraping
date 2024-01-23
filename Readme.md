# Web Scraping
Tutorial extraido del curso gratuito Udemy ["The Ultimate Web ScrapingWith Python Bootcamp 2024"](https://www.udemy.com/course/mastering-web-scraping-using-python-the-complete-course/)

## Indice
* [Descripción](#descripción)
* [Instalación](#instalación)
* [Finding Techniques](#finding-techniques)
* [Beautiful Soup](#beautiful-soup)
    * [Parsers](#parsers)
    * [Accediendo a los elemntos Html](#accediendo-a-los-elementos-html)




## Descripción
Web scraping o raspado web es una técnica utilizada mediante programas de software para extraer información de sitios web.​ Usualmente, estos programas simulan la navegación de un humano en la World Wide Web ya sea utilizando el protocolo HTTP manualmente, o incrustando un navegador en una aplicación

## Instalación


## Finding Techniques
Como encontrar el esquema de la pagina web para el Web Scraping.

* HTML Page Source:
Con el boton derecho del raton se abre el menu y aqui encontramos "View Page Source".


* Developer Tools:
Es en paquete o herramienta de desarrollo: POdemos observar HTML, CSS y JavaScript, asi como monitorizar el trafico de la red.
Con el boton derecho del raton se abre el menu y aqui encontramos "Inspect".


* Sitemaps:
Alguna webs publican la lista de todas las paginas de su web en formato estructurado. Puedes encontralo añadiendo "/sitemap.xml" al final de la URL. Puedes rapidamente determinar la estructura de la web y la localizacion de la información que estas buscando.


* Robots.txt:
Nos permite conocer que paginas no quieren ser visibles o utilizadas por el propietario. Podemos conocerlas poniendo "robots.txt" al final de la URL.


## Beautiful Soup
Libreria Python utilizada para web scraping.

Es buena practica crear un ambiente virtual de Python antes de instalar Beautiful Soup para evitar conflictos con otras versiones de libreias en el sistema.

```
python -m venv my_env
source my_env/bin/activate
```

```
pip install beautifilsoup
```


### Parsers

En la libreria hay varios parsers (analizadores) a elegir. Los mas comunes son:

* ***html.parser*** :
Es el analizador que viene por defecto. Es implementación Python, es mas lento que otros pero no requiere complementos externos (external dependencies).

    ```
    from bs4 import BeautifulSoup
    html_doc = "<html><title>Example</title><body><p>Hello World!</p></body></html>"
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.p.string)
    ```

* ***lxml*** :
Esta basado en C, conocido por su velocidad y habilidad para manejar grandes documentos. Requiere instalar la libreria **lxml**. Se instala mediante comando pip. Puede soportar analizadores XML y HTML, incluso analizar documentos HTML rotos.

    ```
    from bs4 import BeautifulSoup
    html_doc = "<html><title>Example</title><body><p>Hello World!</p></body></html>"
    soup = BeautifulSoup(html_doc, 'lxml')
    print(soup.p.string)
    ```

* ***html5lib*** : Conocido por analizar malamente los documentos HTML. Es implementación pura de Python y necesita la libreria **html5lib** instalada. Es mas lento que otros analizadores pero puede manejar tags no cerrados o erroneos.

    ```
    from bs4 import BeautifulSoup
    html_doc = "<html><body><p>Hello World!</body></html>"
    soup = BeautifulSoup(html_doc, 'html5lib')
    print(soup.p.string)
    ```
    En la carpeta se encuentra el fichero "bs4Parser.py".

La selección de un analizador u otro, dependerá de las necesidades específicas del proyecto, como son el tamaño y la complejidad del documento HTML, asi como la deseada velocidad de análisis.


### Accediendo a los elementos Html

Estos métodos son esencialmente métodos o localizadores.

#### **find()**

El método find() se utiliza par localizar la primera ocurrencia de un elemento con atru¡ibutos especificos.
Por ejemplo, el primer elemnto "< p >" con clase "article" puede ser encontrado utilizando el siguiente código:


```
soup.find('p', class_='article')
```

#### **find_all()**

El método find_all() se utiliza para localizar todas las ocurrencias de un elemento con atributos específicos.
Por ejemplo, todos los elemntos 'a' con el atributo 'href' pueden encontrarse utilizando el siguiente código:

```
soup.find_all('a', href=True)
```

#### **select()**

El método select() utiliza sintaxis de selección CSS en lugar de atributos etiquetqdos (Tags). Por ejemplo, para localizar todos los elementos 'p' dentro de un elemento 'div' con la clase 'container', este método puede ser utilizado asi:

```
soup.select('div.container p')
```

#### **get()**

El método get() puede recuperar el valor de un atributo especifico de un elemento. Por ejemplo, para obtener el valor del atributo 'href' para un elemento 'a', podemos utilizar el siguiente código:

```
a_tag = soup.find('a')
link = a_tag.get('href')
```

### **Encadenar métodos** 
Es una técnica que engloba la utilización de multiples métodos en la misma linea de código. Esto lo hace mas facil de leer y de seguir.

Por ejemplo, para encontrar el primer elemento 'h1' con clase 'title' y acceder al contenido de su texto encadenando métodos, podemos utilizar el siguiente código:

```
soup.find('h1', class_='title').text
```

### **Encontrar el "Path"**
Path se refiere a la localización de un elemento con un documento Html. Para obteener el path de un elemento, hay dos métodos:

- **find_parents()**
- **find_parent()**

Estos métodos pueden usarse para navegar por el arbol jerarquico, obtener una lista de etiquetas padres, y añadir la etiqueta actual al final de la lista.
Por ejemplo para obtener el path de un elemento 'a' del elemento 'body', podemos utilizar el siguiente codigo:

```
a_tag = soup.find('a')
path = [e.name for e in a_tag.find_parents()[::-1]]
path.append(a_tag.name)
```