#!/usr/bin/env python3
"""
Copyright (c) 2020 Samuel Prevost.
Released under MIT License, see LICENCE.md

Simple recursive PDF scrapper using Scrapy
"""

from urllib.parse import urlparse
import os
import scrapy
from scrapy.http import Request


class pdf_scrapper(scrapy.Spider):
    name = "pdf_scrapper"

    allowed_domains = ["www.licence.math.upmc.fr"]
    start_urls = ["https://www.licence.math.upmc.fr/UE/LM226/"]

    def parse(self, response):
        for href in response.css("a::attr(href)").extract():
            filename = self.get_filename(response.urljoin(href))
            if filename.endswith(".pdf"):
                yield Request(url=response.urljoin(href), callback=self.save_pdf)
            else:
                yield Request(url=response.urljoin(href), callback=self.parse)

    def save_pdf(self, response):
        filename = self.get_filename(response.url)
        self.logger.info("Saving PDF %s", filename)
        with open(filename, "wb") as f:
            f.write(response.body)

    @staticmethod
    def get_filename(url):
        return os.path.split(urlparse(url).path)[-1]
