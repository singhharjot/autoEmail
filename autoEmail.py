import time
def switch(arg):
    switcher={
        1: autologin(),
        2: autoemail(),
        3: Break()
    }
    print(switcher.get(arg,"nothing"))
    

def autoemail():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.by import By
    
    br=webdriver.Firefox()
    br.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    email=br.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys("") #place your registered email id between the double quotes
    br.find_element_by_css_selector('#identifierNext > content:nth-child(3) > span:nth-child(1)').click()
    time.sleep(10)

    pas=br.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    pas.send_keys("") #place your password between the double quotes
    br.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span').click()
    br.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div').click()
    time.sleep(4)
    to_user=br.find_element_by_xpath('//*[@id=":oe"]')
    to_user.send_keys("") #place receiver's registered email id between the double quotes
    to_user=br.find_element_by_xpath('//*[@id=":nw"]')
    to_user.send_keys("") #place subject here 
    to_user=br.find_element_by_xpath('//*[@id=":p1"]')
    to_user.send_keys("") #place mail here here
    br.find_element_by_xpath('//*[@id=":nm"]').click()    

def Break():
        print("exiting...")

print("press 1 to autologin.")
print("press 2 to send auto email")
print("press 3 to exit")

a=eval(input())
#switch(a)
autoemail()
