#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

USER_NAME = unicode('', 'utf-8')
USER_PWD = ''
PRODUCT_LINE_NAME = ''
PRODUCT_NUMBER_LIST = []
PRODUCT_FAIL_LIST = []
PRODUCT_STATUS = 0


def doWorkWithSold(self):
    print "doWork start"
    with open('product_number_file.txt', 'r') as product_number_file:
        for product_number in product_number_file:
            PRODUCT_NUMBER_LIST.append(product_number.strip('\n').split(',')[0])
    product_number_file.close()
    product_fail_file = open('product_fail_file.txt', 'w')
    product_fail_file.truncate()

    # 选择铺货TAB
    sleep(1)
    self.browser.implicitly_wait(10)
    self.browser.find_element_by_xpath("//*[@onclick='return gotoTab(1)']").click()

    for data in PRODUCT_NUMBER_LIST:
        try:

            # 清除商品编号输入框内容
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_name('productNumber').clear()

            # 输入查询的商品编号
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_name('productNumber').send_keys(unicode(data, 'utf-8'))

            # 点击查询按钮
            sleep(1)
            self.browser.find_element_by_xpath("//*[@class='sui-btn btn-primary btn-large']").click()

            # 点击更改按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_xpath("//*[@class='J_Modify_Productline_Btn']").click()

            # 点击下拉框
            sleep(1)
            self.browser.implicitly_wait(10)
            menu = self.browser.find_element_by_xpath("//div[@class='ui-dialog-window']//select[@name='productLineId']")
            actions = ActionChains(self.browser)
            actions.move_to_element(menu)
            actions.click(menu)
            actions.perform()
            actions.release()
            select = Select(menu)
            select.select_by_visible_text(PRODUCT_LINE_NAME)

            # 点击确认按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            buttons = self.browser.find_elements_by_xpath(
                "//*[@class='sui-btn btn-primary J_Confirm']")
            for element in buttons:
                if element.text == unicode('确定', 'utf-8'):
                    element.click()

            # 点击确认按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            buttons = self.browser.find_elements_by_xpath(
                "//*[@class='J_Submit']")
            for element in buttons:
                if element.text == unicode('确定', 'utf-8'):
                    element.click()

        except:
            PRODUCT_FAIL_LIST.append(data)
            product_fail_file.write(data)
            product_fail_file.write('\n')
            product_fail_file.flush()
            continue
    for data in PRODUCT_FAIL_LIST:
        print "fail --> " + data
    product_fail_file.close()
    sleep(10)
    self.browser.quit()
    print "doWork done"


def doWorkWithUnsold(self):
    print "doWork start"
    with open('product_number_file.txt', 'r') as product_number_file:
        for product_number in product_number_file:
            PRODUCT_NUMBER_LIST.append(product_number.strip('\n').split(',')[0])
    product_number_file.closed
    product_fail_file = open('product_fail_file.txt', 'w')
    product_fail_file.truncate()

    # 选择未铺货TAB
    sleep(1)
    self.browser.implicitly_wait(10)
    self.browser.find_element_by_xpath("//*[@onclick='return gotoTab(2)']").click()

    for data in PRODUCT_NUMBER_LIST:
        try:

            # 清除商品编号输入框内容
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_name('productNumber').clear()

            # 输入查询的商品编号
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_name('productNumber').send_keys(unicode(data, 'utf-8'))

            # 点击查询按钮
            sleep(1)
            self.browser.find_element_by_xpath("//*[@class='sui-btn btn-primary btn-large']").click()

            # 点击更改按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_xpath("//*[@class='J_Modify_Productline_Btn']").click()

            # 点击下拉框
            sleep(1)
            self.browser.implicitly_wait(10)
            menu = self.browser.find_element_by_xpath("//div[@class='ui-dialog-window']//select[@name='productLineId']")
            actions = ActionChains(self.browser)
            actions.move_to_element(menu)
            actions.click(menu)
            actions.perform()
            actions.release()
            select = Select(menu)
            select.select_by_visible_text(PRODUCT_LINE_NAME)

            # 点击确认按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            buttons = self.browser.find_elements_by_xpath(
                "//*[@class='sui-btn btn-primary J_Confirm']")
            for element in buttons:
                if element.text == unicode('确定', 'utf-8'):
                    element.click()

            # 点击确认按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            buttons = self.browser.find_elements_by_xpath(
                "//*[@class='J_Submit']")
            for element in buttons:
                if element.text == unicode('确定', 'utf-8'):
                    element.click()

        except:
            PRODUCT_FAIL_LIST.append(data)
            product_fail_file.write(data)
            product_fail_file.write('\n')
            continue
    for data in PRODUCT_FAIL_LIST:
        print "fail --> " + data
    product_fail_file.close()
    sleep(10)
    self.browser.quit()
    print "doWork done"


class gongxiao_platform:

    # 对象初始化
    def __init__(self):
        # webdriver version 74.0.3729.x
        chromedriver_path = "/Users/bugman/PycharmProjects/GXPlatformHelper/chromedriver"  # chromedriver的完整路径地址
        url = 'https://portal.gongxiao.tmall.com'
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 最大化浏览器窗口
        self.browser.maximize_window()
        # 打开网页
        self.browser.get(self.url)

        # 切换至密码登录
        sleep(1)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_class_name('login-switch').click()

        # 输入淘宝账号
        sleep(1)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('TPL_username_1').send_keys(USER_NAME)

        # 输入淘宝密码
        sleep(1)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('TPL_password_1').send_keys(USER_PWD)

        # 点击确认登录按钮
        sleep(1)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id('J_SubmitStatic').click()

        # 强制等待登录完成
        sleep(30)

        # 打开供销平台网页
        self.browser.get("https://goods.gongxiao.tmall.com/supplier/product/product_list.htm")
        try:
            # 点击我知道了按钮
            sleep(1)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_xpath("//*[@class='introjs-button introjs-skipbutton']").click()
        except:
            print "click '我知道了' except"
            if(PRODUCT_STATUS==0):
                doWorkWithSold(self)
            else:
                doWorkWithUnsold(self)

        else:
            if (PRODUCT_STATUS == 0):
                doWorkWithSold(self)
            else:
                doWorkWithUnsold(self)

# if __name__ == "__main__":
#     gongxiao_platform = gongxiao_platform()
#     gongxiao_platform.login()
