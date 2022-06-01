# coding=utf-8
"""
登录界面
"""
from base.base_page import BasePage


class LoginPage(BasePage):
    """
    获取页面的元素
    """
    loc_username = (By.NAME, '')
    loc_password = (By.NAME, '')
    loc_click = (By.NAME)
    """
    获取页面动作
    """
    def login(self, username, password):
        self.send_keys(LoginPage.loc_username, username)
        self.send_keys(LoginPage.loc_password, password)
        self.clikc(LoginPage.loc_click)