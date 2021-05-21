from features.pages.BasePage import BasePage


class HomePage(BasePage):

    def click_login_button(self):
         super().get_elements_by_link_text("Log In").click()
        # super().get_element_by_css("div._3YpvX:nth-child(2)").click()
        # super().get_element_by_xpath("a[contains(text(), 'Log In')]").click()
