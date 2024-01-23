from bs4 import BeautifulSoup

html_doc = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Sample HTML Document</title>
        </head>
        <body>
            <header>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact Us</a></li>
                    </ul>
                </nav>
                <h1 class="title">Welcome to our website</h1>
            </header>
            <main>
                <section>
                    <article>
                        <p class="article">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum risus non sapien mattis, vehicula tincidunt nulla cursus. Donec lobortis tempor nibh vel elementum. Curabitur imperdiet, elit a pulvinar sagittis, ipsum dolor interdum sapien, eu iaculis nisl massa ac magna. Aliquam sit amet est eu sapien mollis placerat. Aenean quis metus at odio ornare cursus et a lorem. Vivamus sed ullamcorper est. Vivamus accumsan laoreet ex, eu bibendum ex iaculis a. Ut pretium posuere purus, et bibendum est maximus porta. Aliquam in mi tellus. Proin libero nulla, auctor nec velit eu, pharetra sollicitudin quam.</p>
                    </article>
                </section>
                <aside>
                    <h2>Recent Posts</h2>
                    <ul>
                        <li><a href="#">Post 1</a></li>
                        <li><a href="#">Post 2</a></li>
                        <li><a href="#">Post 3</a></li>
                        <li><a href="#">Post 4</a></li>
                    </ul>
                </aside>
            </main>
            <footer>
                <p>&copy; 2021 - All rights reserved.</p>
            </footer>
        </body>
    </html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Find the first paragraph with class 'article'
first_paragraph = soup.find('p', class_='article')
print(first_paragraph)

# Find all links with href attribute
all_links = soup.find_all('a', href=True)
print(all_links)

# Select all paragraphs inside div container
div_paragraphs = soup.select('div.container p')
print(div_paragraphs)

# Find the first link and get its href attribute
a_tag = soup.find('a')
link = a_tag.get('href')
print(link)

# Find the text inside the first h1 element with class 'title'
header = soup.find('h1', class_='title').text
print(header)

# Find the parent elements of the first link
a_tag = soup.find('a')
path = [e.name for e in a_tag.find_parents()[::-1]]
path.append(a_tag.name)
print(path)