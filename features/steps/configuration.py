from appium import webdriver

caps = {"appPackage": "co®m.android.calculator2",
        "appActivity": "com.android.calculator2.Calculator",
        "platformName": "Android",
        'deviceName': 'Qualquer nome Funciona',
        'avd': 'MeuEmulador'
        }

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


def execute_frontend_test():
    print("Oi Felipe")
    el1 = driver.find_element_by_id("com.android.calculator2:id/digit_4")
    el1.click()
    el2 = driver.find_element_by_id("com.android.calculator2:id/digit_0")
    el2.click()
    el3 = driver.find_element_by_accessibility_id("multiply")
    el3.click()
    el4 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
    el4.click()
    el5 = driver.find_element_by_id("com.android.calculator2:id/digit_5")
    el5.click()
    el6 = driver.find_element_by_accessibility_id("multiply")
    el6.click()
    el5.click()
    el8 = driver.find_element_by_accessibility_id("point")
    el8.click()
    el9 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
    el9.click()
    el10 = driver.find_element_by_accessibility_id("equals")
    el10.click()

    driver.quit()



