from bs4 import BeautifulSoup

html_doc = "<html><title>Example</title><body><p>Hello, I'm missing my closing-tag!!</body></html>"
soup = BeautifulSoup(html_doc, 'html5lib')
print(soup.p.string)



