from appium import webdriver

dc = {
  "deviceName": "Galaxy S10e",
  "platformName": "Android",
  "appPackage": "io.selendroid.testapp",
  "appActivity": "io.selendroid.testapp.HomeScreenActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",dc)
driver.implicitly_wait(5)

#locate element using ID = resource-id
driver.find_element_by_id("android:id/button1").click()

#locate element using accessibilty_id = content-desc
driver.find_element_by_accessibility_id("startUserRegistrationCD").click()

#sending value in form elemnets

#Hide onscreen keyboar
driver.hide_keyboard()

#driver.find_element_by_id()
usename =driver.find_element_by_id("io.selendroid.testapp:id/inputUsername")
usename.send_keys("s.bhowmik")
email = driver.find_element_by_id("io.selendroid.testapp:id/inputEmail")
email.send_keys("subrata@yopmail.com")
password = driver.find_element_by_id("io.selendroid.testapp:id/inputPassword")
password.send_keys("1234@asdf")
name = driver.find_element_by_id("io.selendroid.testapp:id/inputName")
name.clear()
name.send_keys("Subrata K. Bhowmik")

# Click on dropdown to open list.
driver.find_element_by_id("io.selendroid.testapp:id/input_preferedProgrammingLanguage").click()
programlist = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.CheckedTextView[4]').click()
driver.find_element_by_id("io.selendroid.testapp:id/input_adds").click()
driver.find_element_by_id("io.selendroid.testapp:id/btnRegisterUser").click()
name_result = driver.find_element_by_id("io.selendroid.testapp:id/label_name_data").text
assert "Subrata K. Bhowmik" in name_result
print("Test Passed")
driver.quit()