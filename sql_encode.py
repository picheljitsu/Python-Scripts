#!/usr/bin/env python3

import sys
import urllib.parse

#Process query arg to apply filters
query_param = ''.join([(i*2) if i == "'" else i for i in sys.argv[1]])

query_template = '''
SELECT * from users WHERE name like '%{query}%' OR name like '%{query}%';
'''
query = query_template.format(query=query_param).strip()
encoded_query = urllib.parse.quote(query)

print('{}\n\n{}'.format(query, encoded_query))
