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
    b = base64.b64encode(bytes('davrv93@gmail.com:fWGZl8QImCn5DoxxWWiP0D5B', 'utf-8')) # bytes
    base64_str = b.decode('utf-8') # convert bytes to string

    c = Confluence(url='https://davrv93.atlassian.net/wiki', username='davrv93@gmail.com',password='fWGZl8QImCn5DoxxWWiP0D5B',cloud=True)
    # atlassian API does not raise error on init if credentials are wrong, this only happens on the first request

    # Provide content by type (page, blog, comment)
    print(c.get_page_child_by_type('425985', type='page', start=None, limit=None, expand=None))

    # Provide content id from search result by title and space
    print(c.get_page_id('TEST', 'demo'))

    # Provide space key from content id
    print(c.get_page_space('425985'))

    # Returns the list of labels on a piece of Content
    print(c.get_page_by_title('TEST', 'demo', start=None, limit=None))

    # Get page by ID
    # Example request URI(s):
    #    http://example.com/confluence/rest/api/content/1234?expand=space,body.view,version,container
    #    http://example.com/confluence/rest/api/content/1234?status=any
    #    page_id: Content ID
    #    status: (str) list of Content statuses to filter results on. Default value: [current]
    #    version: (int)
    #    expand: OPTIONAL: A comma separated list of properties to expand on the content.
    #                   Default value: history,space,version
    #                   We can also specify some extensions such as extensions.inlineProperties
    #                   (for getting inline comment-specific properties) or extensions.resolution
    #                   for the resolution status of each comment in the results
    print(c.get_page_by_id('425985', expand=None, status=None, version=None))

    # The list of labels on a piece of Content
    print(c.get_page_labels('425985', prefix=None, start=None, limit=None))

    # Get draft page by ID
    c.get_draft_page_by_id('425985', status='draft')

    # Get all page by label
    c.get_all_pages_by_label('test', start=0, limit=50)

    # Get all pages from Space
    # content_type can be 'page' or 'blogpost'. Defaults to 'page'
    # expand is a comma separated list of properties to expand on the content.
    # max limit is 100. For more you have to loop over start values.
    c.get_all_pages_from_space('TEST', start=0, limit=100, status=None, expand=None, content_type='page')

    # Get list of pages from trash
    c.get_all_pages_from_space_trash('TEST', start=0, limit=500, status='trashed', content_type='page')

    # Get list of draft pages from space
    # Use case is cleanup old drafts from Confluence
    c.get_all_draft_pages_from_space('TEST', start=0, limit=500, status='draft')

    # Search list of draft pages by space key
    # Use case is cleanup old drafts from Confluence
    c.get_all_draft_pages_from_space_through_cql('TEST', start=0, limit=500, status='draft')

    # Info about all restrictions by operation
    c.get_all_restrictions_for_content('131142')
    print(c.page_exists('TEST', 'demo'))

    
except Exception as e:
    logging.error(e)
    print(e)
    print('error')