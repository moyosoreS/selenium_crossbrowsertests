import sys
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver

__author__ = 'Desmond'

# Please visit http://selenium-python.readthedocs.org/en/latest/index.html for detailed installation and instructions


class SeleniumCBT(unittest.TestCase):

    def setUp(self):
        print('Setting Up...')

    def test_1_login(self):

        wait = WebDriverWait(driver, 10)
        username = driver.find_element_by_name('username')
        username.send_keys('test')
        password = driver.find_element_by_name('password')
        password.send_keys('test')
        button = wait.until(ec.element_to_be_clickable((By.NAME, 'submit')))
        button.click()

    def test_2_review_current(self):
        wait = WebDriverWait(driver, 10)
        button = wait.until(ec.element_to_be_clickable((By.ID, 'review_current_meds')))
        button.click()

        button_group = driver.find_elements_by_tag_name('button')
        button_group[0].click()
        button_group = driver.find_elements_by_tag_name('button')
        button_group[1].click()
        button_group = driver.find_elements_by_tag_name('button')
        button_group[2].click()

    def test_3_add(self):
        wait = WebDriverWait(driver, 10)
        button_group = driver.find_elements_by_tag_name('button')
        button_group[0].click()

        i_frame = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(i_frame)

        textbox = driver.find_element_by_id('addmed_name')
        textbox.send_keys('Lipitor')

        button = wait.until(ec.element_to_be_clickable((By.TAG_NAME, 'button')))
        button.click()

        radio_group = driver.find_elements_by_name('item_oid')
        radio_group[1].click()

        dose = driver.find_element_by_name('dose')
        dose.send_keys(1)
        frequency = driver.find_element_by_name('frequency')
        frequency.send_keys(1)
        submit = wait.until(ec.element_to_be_clickable((By.NAME, 'submit')))
        submit.click()

        driver.switch_to.default_content()

    def test_4_review_recon(self):
        wait = WebDriverWait(driver, 10)
        button_group = driver.find_elements_by_tag_name('button')
        button_group[1].click()

        table = driver.find_element_by_tag_name('table')
        td = table.find_elements(By.TAG_NAME, 'td')

        i = 0
        for line in td:
            print('ENTRY: ', i, '\n', line.text)
            i += 1

        assert 'NEXIUM' in td.__getitem__(2).text
        assert 'LIPITOR' in td.__getitem__(7).text
        assert 'JANUVIA' in td.__getitem__(12).text
        assert 'ABILIFY' in td.__getitem__(17).text

        button = wait.until(ec.element_to_be_clickable((By.TAG_NAME, 'button')))
        button.click()

        code = driver.find_element_by_name('code')
        code.send_keys('1234')

        next_button_group = driver.find_elements_by_tag_name('button')
        next_button_group[1].click()

    def test_5_review_new(self):
        wait = WebDriverWait(driver, 10)
        button_group = driver.find_elements_by_tag_name('button')
        button_group[1].click()

        table = driver.find_element_by_tag_name('table')
        td = table.find_elements(By.TAG_NAME, 'td')

        i = 0
        for line in td:
            print('ENTRY: ', i, '\n', line.text)
            i += 1

        assert 'NEXIUM' in td.__getitem__(2).text
        assert 'LIPITOR' in td.__getitem__(7).text
        assert 'JANUVIA' in td.__getitem__(12).text
        assert 'ABILIFY' in td.__getitem__(17).text

        button = wait.until(ec.element_to_be_clickable((By.TAG_NAME, 'button')))
        button.click()

    def tearDown(self):
        print("Done with session %s" % driver.session_id)


class Site:
    __site_path = None

    def __init__(self, path):
        self.__site_path = path

    def get_path(self):
        return self.__site_path


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    test_mode = sys.argv[1]
    browser_site = sys.argv[2]

    if test_mode.lower() == 'cbt':
        caps = {'name': 'Selenium Test Example', 'build': '1.0', 'browser_api_name': 'Chrome45x64',
                'os_api_name': 'Win7x64-C1', 'screen_resolution': '1024x768', 'record_video': 'true',
                'record_network': 'true', 'record_snapshot': 'false', 'max_duration': 1200}

        driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="your crossbrowser server"
        )

    elif test_mode.lower() == 'firefox':
        driver = webdriver.Firefox()

    else:
        print('You must specify a test mode')

    assert driver is not None

    print('SITE: ', browser_site)

    site = Site(browser_site)
    site_path = site.get_path()

    print('Loading Url: ', site_path)
    driver.get(site_path)
    driver.implicitly_wait(10)

    print('Checking title')
    assert ('Login' in driver.title)

    del sys.argv[1:]
    unittest.main()
