from pybrowser import Window
import pybrowser


def test_window():
    crawler = Window()
    webdrivers_list = pybrowser.window.webdrivers.keys()
    assert crawler.driver.name in webdrivers_list, "Valid webdriver."
