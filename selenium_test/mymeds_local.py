from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
__author__ = 'Desmond'

browser = webdriver.Firefox()
browser.get('http://moyosore.ringfulhealth.com/login?e=moyosore%40ringful.com&a=47376669')
print('Checking title')
assert ('Patient Dashboard' in browser.title)

print('In Dashboard...')
wait = WebDriverWait(browser, 10)
button = wait.until(ec.element_to_be_clickable((By.ID, 'sbirt2_screen')))
button.click()

print('Answering mohr questions...')

tables = browser.find_elements_by_tag_name('table')

browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[2].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[3].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[2].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[3].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[4].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[5].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[6].style.display = 'block';")
browser.execute_script(
    "document.getElementById('alcohol_qtable').style.display = 'block';")
browser.execute_script(
    "document.getElementById('alcohol_qtr').style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[4].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[5].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[6].style.display = 'block';")
browser.execute_script(
    "document.getElementById('submit-button').style.display = 'block';")

count = 0
for entry in tables:
    print("ENTRY ", count, ':', entry.text)
    count += 1

fast_food_response = tables[0].find_elements_by_tag_name('td')
fast_food_response[2].click()
fruit_response = tables[1].find_elements_by_tag_name('td')
fruit_response[2].click()
soda_response = tables[2].find_elements_by_tag_name('td')
soda_response[1].click()
strenous_response = tables[3].find_elements_by_tag_name('td')
strenous_response[3].click()
tobacco_response = tables[4].find_elements_by_tag_name('td')
tobacco_response[1].click()
tobacco_response[4].click()
alcohol_drinking_response = tables[5].find_elements_by_tag_name('td')
alcohol_drinking_response[0].click()
alcohol_per_day = tables[6].find_elements_by_tag_name('td')
alcohol_per_day[3].click()
alcohol_per_day[7].click()
illegal_drug_response = tables[7].find_elements_by_tag_name('td')
illegal_drug_response[1].click()
general_health_response = tables[8].find_elements_by_tag_name('td')
general_health_response[2].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[2].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[3].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[2].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[3].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[4].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[5].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table')[6].style.display = 'none';")
browser.execute_script(
    "document.getElementById('alcohol_qtable').style.display = 'none';")
browser.execute_script(
    "document.getElementById('alcohol_qtr').style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[4].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[5].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[6].style.display = 'none';")

button.click()

print('Answering phq9 questions...')

table = browser.find_element_by_tag_name('table')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[8].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[9].style.display = 'block';")
browser.execute_script(
            "document.getElementById('submit-button').style.display = 'block';")

print("ENTRY ", ':', table.text)

phq_questions = table.find_elements_by_tag_name('td')

count = 0
for entry in phq_questions:
    print("ENTRY: ", count, entry.text)
    count += 1

phq_questions[2].click()
phq_questions[7].click()
phq_questions[13].click()
phq_questions[17].click()
phq_questions[23].click()
phq_questions[27].click()
phq_questions[33].click()
phq_questions[37].click()
phq_questions[43].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[8].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[9].style.display = 'none';")

button.click()

print('Answering auditc questions...')

tables = browser.find_elements_by_tag_name('table')

browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[2].style.display = 'block';")

browser.execute_script(
    "document.getElementById('submit-button').style.display = 'block';")

count = 0
for entry in tables:
    print("ENTRY ", count, ':', entry.text)
    count += 1

drink_alcohol_often = tables[0].find_elements_by_tag_name("td")
drink_alcohol_often[2].click()
standard_drinks_alcohol = tables[1].find_elements_by_tag_name("td")
standard_drinks_alcohol[2].click()
six_more_drinks_once = tables[2].find_elements_by_tag_name("td")
six_more_drinks_once[1].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('question_table question_table_whole')[2].style.display = 'none';")

button.click()

print('Answering dast10 questions...')

table = browser.find_element_by_tag_name('table')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[8].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[9].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[10].style.display = 'block';")
browser.execute_script(
            "document.getElementById('submit-button').style.display = 'block';")

print("ENTRY ", ':', table.text)

dast10_questions = table.find_elements_by_tag_name('td')

count = 0
for entry in dast10_questions:
    print("ENTRY ", count, ':', entry.text)
    count += 1

dast10_questions[1].click()
dast10_questions[5].click()
dast10_questions[7].click()
dast10_questions[11].click()
dast10_questions[14].click()
dast10_questions[17].click()
dast10_questions[20].click()
dast10_questions[23].click()
dast10_questions[26].click()
dast10_questions[29].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[8].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[9].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[10].style.display = 'none';")

button.click()

print('Answering drug types questions...')

tables = browser.find_elements_by_tag_name('table')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'block';")
browser.execute_script(
    "document.getElementById('other-detail').style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'block';")

count = 0
for entry in tables:
    print("ENTRY ", count, ':', entry.text)
    count += 1

table1_questions = tables[0].find_elements_by_tag_name('td')
table1_questions[1].click()
table1_questions[7].click()
table1_questions[13].click()
table1_questions[18].click()
table1_questions[24].click()

table2_questions = tables[1].find_elements_by_tag_name('td')
table2_questions[2].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'none';")

button.click()

print('Answering drug treatment questions...')

tables = browser.find_elements_by_tag_name('table')

browser.execute_script(
    "document.getElementsByClassName('table no')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('table no')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByClassName('table no')[2].style.display = 'block';")
browser.execute_script(
            "document.getElementById('q3-row').style.display = 'block';")
browser.execute_script(
            "document.getElementById('submit-button').style.display = 'block';")

count = 0
for entry in tables:
    print("ENTRY ", count, ':', entry.text)
    count += 1

table1_questions = tables[0].find_elements_by_tag_name('td')
table1_questions[1].click()
table2_questions = tables[1].find_elements_by_tag_name('td')
table2_questions[0].click()
table3_questions = tables[2].find_elements_by_tag_name('td')
table3_questions[2].click()
table3_questions[4].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementsByClassName('table no')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('table no')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByClassName('table no')[2].style.display = 'none';")
browser.execute_script(
            "document.getElementById('q3-row').style.display = 'none';")

button.click()

print('Answering select substance questions...')

table = browser.find_element_by_tag_name('table')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'block';")
browser.execute_script(
            "document.getElementById('submit-button').style.display = 'block';")

substance_questions = table.find_elements_by_tag_name('td')

count = 0
for entry in substance_questions:
    print("ENTRY: ", count, entry.text)
    count += 1

substance_questions[10].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'none';")

button.click()

print('Answering computer bi questions...')

skip_link = browser.find_element_by_link_text('Skip this')
skip_link.click()

print('Answering pros cons questions...')

tables = browser.find_elements_by_tag_name('table')

browser.execute_script(
    "document.getElementById('form').style.display = 'block';")

count = 0
for entry in tables:
    print("ENTRY ", count, ':', entry.text)
    count += 1

table1_questions = tables[0].find_elements_by_tag_name('td')
table1_questions[0].click()
table1_questions[2].click()
table1_questions[4].click()
table1_questions[6].click()
table1_questions[8].click()
table1_questions[10].click()
table2_questions = tables[1].find_elements_by_tag_name('td')
table3_questions = tables[2].find_elements_by_tag_name('td')
table3_questions[0].click()
table3_questions[2].click()
table3_questions[4].click()
table3_questions[6].click()
table4_questions = tables[3].find_elements_by_tag_name('td')

button = browser.find_element_by_tag_name('button')

button.click()

print('Answering pros rate questions...')

table = browser.find_element_by_tag_name('table')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'block';")
browser.execute_script(
            "document.getElementById('submit-button').style.display = 'block';")

pros_rate_questions = table.find_elements_by_tag_name('td')

print("ENTRY ", ':', table.text)

count = 0
for entry in pros_rate_questions:
    print("ENTRY: ", count, entry.text)
    count += 1

pros_rate_questions[4].click()
pros_rate_questions[10].click()
pros_rate_questions[16].click()
pros_rate_questions[22].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'none';")

button.click()

print('Answering change ready questions...')

table = browser.find_element_by_tag_name('table')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'block';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'block';")
browser.execute_script(
            "document.getElementById('submit-button').style.display = 'block';")

change_ready_questions = table.find_elements_by_tag_name('td')

print("ENTRY ", ':', table.text)

count = 0
for entry in change_ready_questions:
    print("ENTRY: ", count, entry.text)
    count += 1

change_ready_questions[6].click()
change_ready_questions[15].click()
change_ready_questions[25].click()
change_ready_questions[35].click()
change_ready_questions[52].click()
change_ready_questions[64].click()
change_ready_questions[75].click()

button = browser.find_element_by_tag_name('button')

browser.execute_script(
    "document.getElementById('questions-table').style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[0].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[1].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[2].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[3].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[4].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[5].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[6].style.display = 'none';")
browser.execute_script(
    "document.getElementsByTagName('tr')[7].style.display = 'none';")

button.click()

print('Answering done questions...')

button = browser.find_element_by_tag_name('button')
button.click()

print('Answering patient need auth questions...')

textbox = browser.find_element_by_id('code')
textbox.send_keys('1234')

buttons = browser.find_elements_by_tag_name('button')
buttons[1].click()

print('Reviewing clinical review questions...')

button = browser.find_element_by_tag_name('button')
button.click()

print('Answering goals questions...')

table = browser.find_element_by_tag_name('table')

print("ENTRY ", ':', table.text)

goals_questions = table.find_elements_by_tag_name('td')

count = 0
for entry in goals_questions:
    print("ENTRY: ", count, entry.text)
    count += 1

goals_questions[4].click()
tobacco_goal = browser.find_element_by_id('tobacco')
tobacco_goal.send_keys('Be Better')
goals_questions[18].click()
ecig_goal = browser.find_element_by_id('ecig')
ecig_goal.send_keys('Be Better')
goals_questions[29].click()
alcohol_goal = browser.find_element_by_id('alcohol')
alcohol_goal.send_keys('Be Better')
goals_questions[38].click()
cannabis_goal = browser.find_element_by_id('cannabis')
cannabis_goal.send_keys('Be Better')
goals_questions[58].click()
cocaine_goal = browser.find_element_by_id('cocaine')
cocaine_goal.send_keys('Be Better')
goals_questions[70].click()
stimulant_goal = browser.find_element_by_id('stimulants')
stimulant_goal.send_keys('Be Better')
goals_questions[80].click()
opoids_goal = browser.find_element_by_id('opioids')
opoids_goal.send_keys('Be Better')

button = browser.find_element_by_tag_name('button')
button.click()

print('Answering goals signature questions...')

buttons = browser.find_elements_by_tag_name('button')
canvas = browser.find_element_by_tag_name('canvas')

drawing = ActionChains(browser)\
    .click_and_hold(canvas)\
    .move_by_offset(-10, -15)\
    .move_by_offset(20, 32)\
    .move_by_offset(10, 25)\
    .release()
drawing.perform()

buttons[1].click()

print('Done answering questions...')
