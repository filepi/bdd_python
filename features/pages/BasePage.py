class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def access_url(self, url):
        self.driver.get(url)

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def get_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def get_elements_by_link_text(self, link_text):
        oi = self.driver.find_elements_by_link_text(link_text)
        print("Size")
        for x in oi:
            print(x)
        return oi


    def get_element_by_css(self, css):
        return self.driver.find_element_by_css_selector(css)
