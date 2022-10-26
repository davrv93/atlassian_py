from atlassian import Jira
from atlassian import Confluence
from atlassian import Crowd
from atlassian import Bitbucket
from atlassian import ServiceDesk
from atlassian import Xray
import base64


import logging

logging.basicConfig(filename='conf_connect.log', filemode='w', level=logging.DEBUG)

try: 
    #Replace localhost with your url. This is working for confluence 7.0.1
    c = Confluence(url='http://confluence-cluster-701-lb:2701', username='admin',password='Confluence2022',cloud=False)

    c.create_page('ds', 'This is my sample page', '<h1>Hello world </h1>', parent_id=None,
     type='page', representation='storage', editor='v2', full_width=False)

    #Getting page id
    print(c.get_page_id('ds', 'This is my sample page'))

    #Getting the page!
    page =c.get_page_by_title('ds', 'This is my sample page', start=None, limit=None)

    #Printing the page!
    print(page)
    
except Exception as e:
    logging.error(e)
    print(e)
    print('error')