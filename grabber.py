# Dependencies - pandoc, selenium, firefox
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException        
from os import system
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--login', required=True, help="Redmine login")
parser.add_argument('--password', required=True, help="Redmine password")
parser.add_argument('--project', required=True, help="Project ID from redmine URLs")
parser.add_argument('--host', required=True, help="Redmine host")
parser.add_argument('--start_id', required=True, type=int, help="Id of the first template")
parser.add_argument('--end_id', required=True, type=int, help="Id of the last template")

results = parser.parse_args()


login=results.login
password=results.password
project=results.project
host=results.host
start=results.start_id
end=results.end_id

url_template='https://{}/projects/{}'.format(host, project) + '/crm_templates/{}/edit'
login_url = 'https://{}/login'.format(host)

# authorize
driver = webdriver.Firefox()
print(login_url)
driver.get(login_url)
driver.find_element_by_id('username').send_keys(login)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('autologin').click()
driver.find_element_by_id('login-submit').click()
# save each url

for i in range(start,end+1):
    url = url_template.format(i)
    print(url)
    sleep(3)    
    driver.get(url)
    # take title and content
    # if error then it is probably deleted page
    try:
        title = driver.find_element_by_id('crm_template_title').get_attribute('value')
        content = driver.find_element_by_id('crm_template_content').text
    except NoSuchElementException:
        continue
    # save to file
    print(title)
    print(content)
    # Hacks for importing cyrillic CRM templates to Confluence 
    content = "<br>".join(content.split("\n"))
    f = open(title+".html","wb")
    f.write(content.encode('utf-8'))
    f.close()
    system("pandoc -s \"{0}.html\" -o \"{0}.docx\"".format(title))
driver.close()
