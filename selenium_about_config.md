#Test user agent set
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriver_path = 'C:\\tools\\geckodriver.exe'    
profile = webdriver.FirefoxProfile() 
profile.set_preference("general.useragent.override", "whatever you want")
browser = webdriver.Firefox(firefox_profile=profile,
                                         executable_path=webdriver_path)
browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")                                         
browser.profile.set_preference("general.useragent.override", "whatever you wanat")  
browser.profile.__init__()
browser.profile.update_preferences()     
browser.execute_script("return navigator.userAgent")
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')                                           
browser.execute_script("window.open('https://google.com','_blank')")
browser.get('about:config')    
if(browser.title == "Advanced Preferences"):
    try:
        #showWarningNextTime for radio
        warnButton = browser.find_element_by_id("warningButton")    
        warnButton.click()                               
    except:
        print("looks like we skipped the caution page, batman")

searchPref = browser.find_element_by_id("about-config-search")
searchPref.send_keys('general.useragent.override')

#check if the user-agent element was added
if browser.find_element_by_class_name("add"):
    #Search for the String radio button
    string_radio = [i for i in browser.find_elements_by_tag_name("span") if i.text == "String" ][0]
    if string_radio.is_enabled():
        string_radio.click()
add_button = browser.find_element_by_class_name("button-add")
add_button.click()
