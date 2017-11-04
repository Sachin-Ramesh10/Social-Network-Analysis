import threading
from queue import Queue
from crawler import Crawler
from operations import Operations


PROJECT_NAME = 'Gaiaonline'
HOMEPAGE = 'http://www.gaiaonline.com/profiles/ie-batman/9487660/'
DOMAIN_NAME = Operations.get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
EDGES_FILE = PROJECT_NAME + '/edges.txt'
URL_MATCH_FILE = PROJECT_NAME + '/url_match.txt'
NAME_MAPPING = PROJECT_NAME + '/name_mapping.txt'
NUMBER_OF_THREADS = 128
queue = Queue()
Crawler(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exits)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in Operations.file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = Operations.file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()
