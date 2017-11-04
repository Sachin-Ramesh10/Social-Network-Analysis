from urllib import parse
from html.parser import HTMLParser
from urllib.parse import urlparse
import os


class Operations(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

        # Get sub domain name (name.example.com)
    def get_sub_domain_name(url):
            try:
                return urlparse(url).netloc
            except:
                return ''

    def get_domain_name(url):
        try:
            results = Operations.get_domain_name(url).split('.')
            return results[-2] + '.' + results[-1]
        except:
            return ''

    def create_project_dir(directory):
        if not os.path.exists(directory):
            print('Creating directory ' + directory)
            os.makedirs(directory)

    # Create files (if not created)
    def create_data_files(project_name, base_url):
        queue = os.path.join(project_name, 'queue.txt')
        crawled = os.path.join(project_name, "crawled.txt")
        edges = os.path.join(project_name, "edges.txt")
        url_match = os.path.join(project_name, "url_match.txt")
        name_mapping = os.path.join(project_name, "name_mapping.txt")
        if not os.path.isfile(queue):
            Operations.write_file(queue, base_url)
        if not os.path.isfile(crawled):
            Operations.write_file(crawled, '')
        if not os.path.isfile(edges):
            Operations.write_file(edges, '')
        if not os.path.isfile(url_match):
            Operations.write_file(url_match, '')
        if not os.path.isfile(name_mapping):
            Operations.write_file(name_mapping, '')

    # Create a new file
    def write_file(path, data):
        with open(path, 'w') as f:
            f.write(data)

    # Add data onto an existing file
    def append_to_file(path, data):
        with open(path, 'a') as file:
            file.write(data + '\n')

    # Delete the contents of a file
    def delete_file_contents(path):
        open(path, 'w').close()

    # Read a file and convert each line to set items
    def file_to_set(file_name):
        results = set()
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
        return results

    # Iterate through a set, each item will be a line in a file
    def set_to_file(links, file_name):
        with open(file_name, "w") as f:
            for l in sorted(links):
                f.write(l + "\n")