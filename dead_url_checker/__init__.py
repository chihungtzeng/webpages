# -*- coding: utf-8 -*-
"""
Analyze the dead links of a webpage.
"""
import logging
from io import BytesIO
import pycurl
from selenium import webdriver
import selenium


class DeadURLChecker(object):
    """
    Given a webpage, report dead links in the page.
    """
    def __init__(self, url):
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.url = url

    def _check_dead_link(self, dest_url):
        self.browser.get(dest_url)
        if "404" in self.browser.title or "404" in self.browser.page_source:
            logging.warn("DEAD: {}".format(dest_url))
        else:
            logging.info("LIVE: {}".format(dest_url))
        self._go_back()

    def _check_hrefs(self):
        hrefs = []
        for element in self.browser.find_elements_by_tag_name("a"):
            hrefs.append(element.get_attribute("href"))

        for href in hrefs:
            self._check_dead_link(href)

    def _go_back(self):
        """
        Navigate the browser to the previous page.
        """
        self.browser.execute_script("window.history.go(-1)")
        return True

    def run(self):
        self.browser.get(self.url)
        self._check_hrefs()
        self.quit()

    def quit(self):
        self.browser.quit()
