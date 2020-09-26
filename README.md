# Simple PDF scrapper

## Usage:

Install the dependencies: `pip3 install urllib3 scrapy`

Then, modify the link in 

```python3
allowed_domains = ["www.licence.math.upmc.fr"]
start_urls = ["https://www.licence.math.upmc.fr/UE/LM226/"]
```

and finally run:

```bash
scrapy runspider spider.py | tee logs
```

This will download all the pdfs available when crawling the provided domains/urls.

## How it works:

You give it start urls and a domain, and it will do the following:

1. Look for all links (`<a href=..>`) in the HTML source code
2. If the link points to a PDF file, download it
3. If the link doesn't point to a PDF file, use that link and go to step 1.

It's really crude but it does its job. The most important part is correctly 
parsing the file name (to check if it's a pdf) because if you bodge that part,
you could end up with taking the GET arugments (stuff like ?id=1&truc=machin)
as the file name. That's why Python's urllib.parse.urlparse is use as its supposed
to be robust.

Scrapy makes this works in multiprocess, handles the smart recursion, checks that we 
don't exit the domain(s) and such. I previously wrote code for that and it's hell to 
do manually. Thank you Scrapy.
