import unittest
import thatscrapper
from thatscrapper import Crawler
from thatscrapper.browser import WebElement
from thatscrapper.browser import webdrivers
from urllib3.exceptions import MaxRetryError
from thatscrapper.common.exceptions import CrawlerError


class TestCrawler(unittest.TestCase):

    def test_unsuported_browser(self,):
        with self.assertRaises(CrawlerError):
            crawler = Crawler(browser='dummy')
            crawler.quit()

    def test_valid_browser(self, ):
        crawler = Crawler(headless=True)
        webdrivers_list = list(thatscrapper.browser.webdrivers.keys())
        message = f"Expected valid browser: {list(webdrivers.keys())}"
        assert crawler.driver.name in webdrivers_list, message
        crawler.quit()

    def test_got_url(self, url="https://google.com/"):
        crawler = Crawler(headless=True)
        crawler.goto(url)
        current_url = crawler.driver.current_url
        assert len(current_url) > 0, "Expected non empty page"
        crawler.quit()

    def test_page_source(self, url="https://google.com/"):
        crawler = Crawler(headless=True)
        crawler.goto(url)
        assert "<html" in crawler.driver.page_source, "Expected page source."
        crawler.quit()

    def test_got_element(self,):
        crawler = Crawler(headless=True)
        crawler.goto("https://google.com/")
        search_bar = crawler.element("q", "name")
        message = "Expected WebElement instance."
        assert isinstance(search_bar, WebElement), message
        crawler.quit()

    def test_expected_tag(self,):
        crawler = Crawler(headless=True)
        crawler.goto("https://google.com/")
        search_bar = crawler.element("q", "name")
        assert search_bar.tag_name == 'input', "Expected 'input' element tag"
        crawler.quit()

    def test_child_elements(self, ):
        crawler = Crawler(headless=True)
        crawler.goto("https://phptravels.com/demo/")
        form_element = crawler.element("form", "class name")
        fields = crawler.children_of(form_element, "input", "tag name")
        for idx, field in enumerate(fields):
            message = f"Expected {idx} as WebElement instance. "
            message = f"Got {type(field)}"
            assert isinstance(field, WebElement), message
        crawler.quit()

    def test_click(self,):
        crawler = Crawler(headless=True)
        crawler.goto("http://the-internet.herokuapp.com/dropdown")
        assert crawler.click("dropdown", "id"), "Expected click"

    def test_click_element(self,):
        crawler = Crawler(headless=True)
        crawler.goto("http://the-internet.herokuapp.com/dropdown")
        dropdown_menu = crawler.element("dropdown", "id")
        clicked = crawler.click_element(dropdown_menu)
        assert dropdown_menu == clicked, "Expected click."

    def test_driver_quit(self,):
        with self.assertRaises(MaxRetryError):
            crawler = Crawler(headless=True)
            crawler.goto("https://google.com")
            crawler.driver.current_url
            crawler.quit()
            crawler.driver.current_url
