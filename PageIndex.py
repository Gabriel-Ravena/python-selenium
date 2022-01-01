import unittest
import time
from selenium import webdriver


class DemoQa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Usuario\Documents\driver\chromedriver.exe')
        self.driver.get("https://demoqa.com/")
        self.driver.maximize_window()
        time.sleep(5)

    def test_clickOptionElements(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        option_elements = self.driver.find_element_by_xpath('//*[@id=\"app\"]/div/div/div[2]/div/div[1]/div/div[1]')
        option_elements.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()