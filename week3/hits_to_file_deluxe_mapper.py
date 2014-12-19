#!/usr/bin/python

import sys

# format of input file is %h %l %u %t \"%r\" %>s %b
# where:
# %h is the IP address of the client
# %l is identity of the client, or "-" if it's unavailable
# %u is username of the client, or "-" if it's unavailable
# %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
# %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
# %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
# %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
#
# we want to find the number of hits made to a file
# we want to form the tupple file -> 1
# and write the tab delimited tupple to standart out

for line in sys.stdin:
    data = line.strip().split()

    resource = data[6].strip()
    
    # there are file resources preceded by a we site domain
    # we want to strip the domain if it exists
    if resource[0:7] == "http://":
        file = resource.split("http://")[1]
        # some web addresses are only a domain address without a file resource at the end
        # we want to skip them
        try:
            print "{0}\t1".format(file[file.index("/"):])
        except:
            continue
    else:
        print "{0}\t1".format(resource)


