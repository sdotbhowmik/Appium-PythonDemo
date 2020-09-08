from appium import webdriver
from selenium.webdriver.common.by import By

#dc = {  "deviceName": "Galaxy A50",  "platformName": "Android",  "app": "H:\\MyProjects\\QA_Projects\\QA_Resources_and_Dependencies\\apks\\flipcart.apk"}
dc = {
  "deviceName": "Galaxy A50",
  "platformName": "Android",
  "appPackage": "com.flipkart.android",
  "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',dc)
driver.implicitly_wait(20)

driver.find_element_by_id("com.flipkart.android:id/locale_icon_layout").click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout').click()
driver.find_element_by_id("com.flipkart.android:id/select_btn").click()