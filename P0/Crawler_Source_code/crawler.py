from urllib.request import urlopen
from operations import Operations
import sys


class Crawler:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    edges_file = ''
    queue = set()
    crawled = set()
    edges = set()
    url_match = set()
    name_mapping = set()
    node_list = []



    def __init__(self, project_name, base_url, domain_name):
          Crawler.project_name = project_name
          Crawler.base_url = base_url
          Crawler.domain_name = domain_name
          Crawler.queue_file = Crawler.project_name + '/queue.txt'
          Crawler.crawled_file = Crawler.project_name + '/crawled.txt'
          Crawler.edges_file = Crawler.project_name + '/edges.txt'
          Crawler.url_match_file = Crawler.project_name + '/url_match.txt'
          Crawler.name_mapping_file = Crawler.project_name + '/name_mapping.txt'
          Crawler.node_count = 0
          Crawler.node_list = []
          Crawler.node_list.insert(0,"List of User Profiles")
          Crawler.name_mapping.add(str(0) + "----->" + "List of User Profiles")
          self.boot()
          self.crawl_page('First Crawler', Crawler.base_url)


    # Creates directory and files for project on first run and starts the Crawler
    @staticmethod
    def boot():
        Operations.create_project_dir(Crawler.project_name)
        Operations.create_data_files(Crawler.project_name, Crawler.base_url)
        Crawler.queue = Operations.file_to_set(Crawler.queue_file)
        Crawler.crawled = Operations.file_to_set(Crawler.crawled_file)
        Crawler.edges = Operations.file_to_set(Crawler.edges_file)
        Crawler.url_match = Operations.file_to_set(Crawler.url_match_file)
        Crawler.name_mapping = Operations.file_to_set(Crawler.name_mapping_file)


    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Crawler.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Crawler.queue)) + ' | Crawled  ' + str(len(Crawler.crawled)))
            if len(Crawler.crawled) > 11000:
                Crawler.update_files()
                sys.exit("Crawling finished")
            linkedurls = Crawler.gather_links(page_url)
            for everylink in linkedurls:
                        if "profiles/" in everylink and "mode" not in everylink:
                             if page_url != everylink:
                                   Crawler.create_edges(page_url, everylink)
                                   Crawler.url_match.add(page_url + "," + everylink)
            Crawler.add_links_to_queue(linkedurls)
            Crawler.queue.remove(page_url)
            Crawler.crawled.add(page_url)
            Crawler.update_files()


    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = Operations(Crawler.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Crawler.queue) or (url in Crawler.crawled):
                continue
            if Crawler.domain_name != Operations.get_domain_name(url):
                continue
            if "profiles/" in url and "mode" not in url:
                 Crawler.queue.add(url)
#updates all the text files
    @staticmethod
    def update_files():
        Operations.set_to_file(Crawler.queue, Crawler.queue_file)
        Operations.set_to_file(Crawler.crawled, Crawler.crawled_file)
        Operations.set_to_file(Crawler.edges, Crawler.edges_file)
        Operations.set_to_file(Crawler.url_match, Crawler.url_match_file)
        Operations.set_to_file(Crawler.name_mapping, Crawler.name_mapping_file)
		
#creates edges and maps the user and node number
    @staticmethod
    def create_edges(node1, node2):

            if node1 not in Crawler.node_list and node2 not in Crawler.node_list:
                Crawler.node_list.insert(len(Crawler.node_list), node1)
                Crawler.name_mapping.add(str(Crawler.node_list.index(node1)) + "," + node1)
                Crawler.node_list.insert(len(Crawler.node_list), node2)
                Crawler.name_mapping.add(str(Crawler.node_list.index(node2)) + "," + node2)
                Crawler.edges.add(str(Crawler.node_list.index(node1)) + "," + str(Crawler.node_list.index(node2)))

            elif node1 not in Crawler.node_list and node2 in Crawler.node_list:
                Crawler.node_list.insert(len(Crawler.node_list), node1)
                Crawler.name_mapping.add(str(Crawler.node_list.index(node1)) + "," + node1)
                Crawler.edges.add(str(Crawler.node_list.index(node1)) + "," + str(Crawler.node_list.index(node2)))


            elif node1 in Crawler.node_list and node2 not in Crawler.node_list:
                Crawler.node_list.insert(len(Crawler.node_list), node2)
                Crawler.name_mapping.add(str(Crawler.node_list.index(node2)) + "," + node2)
                Crawler.edges.add(str(Crawler.node_list.index(node1)) + "," + str(Crawler.node_list.index(node2)))

            else:
                Crawler.edges.add(str(Crawler.node_list.index(node1)) + "," + str(Crawler.node_list.index(node2)))

