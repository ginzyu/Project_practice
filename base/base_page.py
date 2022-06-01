# coding=utf-8
"""
基础方法
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self):
        """
        定义全局变量 Driver，打开浏览器
        """
        global driver
        self.Driver = webdriver.Chrome()
        driver = self.Driver
        self.driver.Driver.get("127.0.0.1")
        """
        定位元素的关键字
        """

    def locator_element(self, loc):
        self.Driver.find_element(By.ID, loc)

        """
        设置值的关键字
        """

    def send_keys(self, loc, values):
        self.locator_element(loc).send_keys(values)

        """
        封装一个点击时间
        """

    def clikc(self, value):
        self.locator_element('value')
