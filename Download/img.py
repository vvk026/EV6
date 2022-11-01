from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
import time


class Google(webdriver.Chrome):
    def __init__(self, driver_path=r'C:\Users\svk76\PycharmProjects\Everything_Downloader\chromedriver.exe'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Google, self).__init__()
        self.maximize_window()

    def get_image(self, name, format, max_img, delay):
        try:
            url = f'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={name}.{format.strip()}&oq={name}.{format.strip()}&gs_l=img'
            self.get(url)
        except Exception as e:
            print(e)

        def scroll_to_end(self):
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(delay)

        image_url = set()
        image_count = 0
        result_start = 0
        while image_count < max_img:
            scroll_to_end(self)
            thumbnail = self.find_elements(by=By.CLASS_NAME, value='Q4LuWd')
            number_result = len(thumbnail)
            for img in thumbnail[result_start:number_result]:
                try:
                    img.click()
                    time.sleep(delay)
                except Exception as e:
                    continue
                images = self.find_elements(by=By.CLASS_NAME, value='n3VNCb')
                for i in images:
                    if i.get_attribute('src') and 'http' in i.get_attribute('src'):
                        image_url.add(i.get_attribute('src'))
                image_count = len(image_url)
                if len(image_url) >= max_img:
                    print(f"Found: {len(image_url)} image links, done!")
                    self.quit()
                    break
            else:
                try:
                    time.sleep(30)
                    load_more_button_1 = self.find_element(by=By.CLASS_NAME, value="r0zKGf")
                    load_more_button_1.click()
                except:
                    time.sleep(30)
                    load_more_button = self.find_element(by=By.CSS_SELECTOR, value=".mye4qd")
                    if load_more_button:
                        self.execute_script("document.querySelector('.mye4qd').click();")
            result_start = len(thumbnail)

        return image_url

    def download_image(self, download_path, url, folder_name):
        try:
            img_content = requests.get(url).content
            file_path = download_path + folder_name

            with open(file_path, 'wb') as f:
                f.write(img_content)
        except Exception as e:
            print(e)
    def dir_create(self,a4):
        try:
            dir = a4
            path_dir = r'C:\Users\svk76\PycharmProjects\EV4\App_Downloads'
            if os.path.isdir(path_dir)==True:
                pass
            else:
                os.mkdir(path_dir)
            path_ = os.path.join(path_dir, dir)
            if os.path.exists(path_):
                pass
            else:
                os.mkdir(path_)
        except Exception as e:
            print(e)

