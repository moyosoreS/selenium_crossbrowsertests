import sys

__author__ = 'Desmond'

# Please visit http://selenium-python.readthedocs.org/en/latest/index.html for detailed installation and instructions

import unittest
import csv
from selenium import webdriver


class SeleniumCBT(unittest.TestCase):
    def setUp(self):
        caps = {}

        caps['name'] = 'Selenium Test Example'
        caps['build'] = '1.0'
        caps['browser_api_name'] = 'IE10'
        caps['os_api_name'] = 'Win7x64-C2'
        caps['screen_resolution'] = '1024x768'
        caps['record_video'] = 'true'
        caps['record_network'] = 'true'
        caps['record_snapshot'] = 'false'

        # start the remote browser on our server
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="your crossbrowser server"
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):

        # maximize the window - DESKTOPS ONLY
        #print('Maximizing window')
        #self.driver.maximize_window()

        try:
            filename = 'test_cases.csv'
            with open(filename) as cases:
                reader = csv.reader(cases)
                for row in reader:
                    print(row)
                    category = row[0]
                    location = row[1]
                    search_num = row[2]
                    desired_hospital = row[3]
                    hospital_rating = row[4]
                    blob_rating = row[5]
                    cost = row[6]
                    cost_breakdown = row[7]
                    print(
                        category + ',' + location + ',' + search_num + ',' + desired_hospital + ',' + hospital_rating + ','
                        + blob_rating + ',' + cost + ',' + cost_breakdown)

                    #load the page url
                    print('Loading Url')
                    self.driver.get('http://www.cahealthcarecompare.org/search.jsp')

                    #check the title
                    print('Checking title')
                    self.assertTrue('Look-up California Hospital/Medical Group Cost & Quality' in self.driver.title)

                    category = self.driver.find_element_by_id(category)
                    textBox = self.driver.find_element_by_id('sterm')
                    button = self.driver.find_element_by_name('submit')

                    category.click()
                    textBox.clear()
                    textBox.send_keys(location)
                    button.click()

                    desired_hospital_link = self.driver.find_element_by_link_text(desired_hospital)
                    desired_hospital_link.click()
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
