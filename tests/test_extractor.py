import os
import pandas
import unittest
from PIL import Image
from thatscraper import Crawler
from thatscraper import extractor
from thatscraper.browser import WebElement
from thatscraper.browser import webdrivers
from thatscraper.common.exceptions import CrawlerError


class TestExtractor(unittest.TestCase):

    def test_html(self,):
        crawler = Crawler(headless=True)
        url = "https://s1.demo.opensourcecms.com/wordpress/wp-admin/install.php"
        crawler.goto(url)
        form_element = crawler.element_id("setup")
        form_html = extractor.html(form_element)
        message = "Supposed to start with '<' and end with '>'" 
        assert "<" == form_html[0] and ">" == form_html[-1], message
        crawler.quit()       

    def test_unorderedlist(self,):
        crawler = Crawler(browser='chrome', headless=True)
        crawler.goto("https://www.techlistic.com/p/demo-selenium-practice.html")

        items = extractor.UnorderedList(crawler, "(//div[@dir=\'ltr\'])[7]", "xpath")

        for item in items:
            li = extractor.html(item)
            assert "<li" in li, "Not a li element"
        crawler.quit()

    def test_download(self,):
        link = "https://selenium-python.readthedocs.io/_static/logo.png"
        path = "selogo.png"
        extractor.download(link, path)
        assert Image.open(path), "There should've been Selenium's logo"
        os.remove(path)

    def test_table(self,):
        crawler = Crawler(browser='chrome')

        crawler.goto("https://www.techlistic.com/p/demo-selenium-practice.html")
        pandas.core.frame.DataFrame
        assert type(
            extractor.Table(crawler, "customers", "id").data[0]
        ) == pandas.core.frame.DataFrame, "Must be a dataframe"
        crawler.quit()