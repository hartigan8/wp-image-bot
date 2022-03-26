from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def doIt(number):
    name = input('Enter the name of user or group : ')
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')

    input('Enter anything after scanning QR code')




    user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
    user.click()
    for i in range (1, number):
        attachment_box = driver.find_element(By.XPATH, '//div[@title = "Ekle"]')
        attachment_box.click()
        filepath = r"C:\Users\Can\PycharmProjects\otowp\hentais\hentai_" + str(i) + ".png"
        image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        sleep(2)

        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()

    sleep(5)
    driver.close()