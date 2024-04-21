# phase a webpage after login, url = "https://www.zeczec.com/users/sign_in", email_blank = driver.find_element("id", "user_email"), email_blank.send_keys("nickmomo1524@gmail.com"), but it have a Cloudflare protection
import time

def phase_a(driver):
    driver.get("https://www.zeczec.com/users/sign_in")
    email_blank = driver.find_element("id", "user_email")
    email_blank.send_keys("nickmomo1524@gmail.com")
    password_blank = driver.find_element("id", "user_password")
    password_blank.send_keys("1aqzwx2s")
    driver.find_element("name", "commit").click()
    time.sleep(5)
    return driver



phase_a()