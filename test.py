logs = [192.168.1.1 - - [11/Dec/2024:14:22:35 +0000] "GET /api/v1/resource HTTP/1.1" 500 3145,
192.168.1.2 - - [11/Dec/2024:14:22:36 +0000] "POST /api/v1/login HTTP/1.1" 200 1024,
192.168.1.3 - - [11/Dec/2024:14:22:37 +0000] "GET /api/v1/resource HTTP/1.1" 500 2356,
192.168.1.4 - - [11/Dec/2024:14:22:38 +0000] "GET /api/v1/resource HTTP/1.1" 404 134,
192.168.1.5 - - [11/Dec/2024:14:22:39 +0000] "POST /api/v1/payment HTTP/1.1" 200 1589,
192.168.1.6 - - [11/Dec/2024:14:22:40 +0000] "GET /api/v1/resource HTTP/1"]

import re
for i in logs:
    if 500 in str(i).rfind(500):
        print(i)