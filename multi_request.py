import time
import urllib2
from multiprocessing import Pool
 
 
def request_worker(args):
    (worker_num, url) = args
    print "[Worker-%s] send request: %s, start time: %s" % (worker_num, url, time.time())
    status_code = urllib2.urlopen(url).getcode()
    print "[Worker-%s] status code: %s, end time: %s" % (worker_num, status_code, time.time())
 
if __name__ == '__main__':
    num_of_threads = 3
    number_of_request = 10
    url = "http://google.com"
 
    requests = []
    for worker_num in range(number_of_request):
        requests.append([worker_num, url])
 
    pool = Pool(num_of_threads)
    result = pool.map(request_worker, requests)
 
    # Prevents any more tasks from being submitted to the pool.
    pool.close()
    # Wait for the worker processes to exit.
    pool.join()