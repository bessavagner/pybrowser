import sys
import polling2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


from .common.logger import log
# from common.exceptions import WindowError

enter = Keys.RETURN
esc = Keys.ESCAPE
delete = Keys.DELETE

webdrivers = {
    'firefox': {
        'driver': webdriver.Firefox,
        'options': webdriver.firefox.options.Options()
    }
}


class Window:

    def __init__(self, browser='firefox', headless=False) -> None:
        self.__driver = None
        self.logger = log(self.__class__.__name__)
        try:
            self.__options = webdrivers[browser]['options']
            if headless:
                self.__options.headless = True
            self.__driver = webdrivers[browser]['driver']()
        except WebDriverException as err:
            message = "You need to add the driver"
            message += f" for {browser} to you environment variables."
            message += " See more in"
            message += " https://selenium-python.readthedocs.io/installation.html#drivers" # noqa E501
            # print(err, message)
            self.logger.error(message)
            print(str(err))
            sys.exit(1)

    @property
    def driver(self,):
        return self.__driver

    def goto(self, url: str):
        self.driver.get(url)

    def google(self, query, step=0.5, timeout=10):
        self.goto("https://google.com")
        search_bar = polling2.poll(
            lambda: self.driver.find_element(By.NAME, 'q'),
            step=step, timeout=timeout
        )
        search_bar.send_keys(query)
        search_bar.send_keys(enter)

    def close(self,):
        """Closes the current window.
        """
        self.driver.close()

    def quit(self,):
        """Quits the driver and close every associated window.
        """
        self.driver.quit()


def main():
    crawler = Window()
    crawler.goto("https://google.com")


if __name__ == '__main__':
    main()
