from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def selenium_pars(part):
    url = 'https://avtopro.ua/'

    # If needed, you can enable headless mode
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    """

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    try:
        driver.get(url)
        # You can change the waiting time depending on the power of your PC
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'pro-input.pro-input--framed.ap-search__input').send_keys(part)
        # You can change the waiting time depending on the power of your PC
        time.sleep(2)
        result = driver.find_elements(By.CSS_SELECTOR, "span[style='overflow: visible;']")
        if len(result) > 1:

            choice = 1
            data = []

            for i in result:
                data.append(i.text)
                print(f'{choice}. {i.text}')
                choice += 1

            choice_result = int(input('Choose your search result: '))

            if choice_result == choice_result:
                print(f'Your choice is: {data[choice_result - 1]}')
                driver.find_element(By.XPATH,
                                    f'//*[@id="ap-search"]/div/div[2]/div/div[1]/div[3]/div/a[{choice_result}]').click()
        else:
            driver.find_element(By.XPATH, '//*[@id="ap-search"]/div/div[2]/div/div[1]/div[3]/div/a[1]').click()

        # You can change the waiting time depending on the power of your PC
        time.sleep(3)
        page = 0

        while True:
            try:
                btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'show-more-btn__icon')))
                driver.execute_script("arguments[0].scrollIntoView();", btn)
                btn.click()
                time.sleep(2)
                page += 1
                print(f'Loaded another page {page}')
            except NoSuchElementException:
                break

    except Exception:
        pass

    finally:
        current_url = driver.current_url
        main_page = driver.page_source
        with open('page.html', 'w', encoding='utf-8') as file:
            file.write(main_page)
            file.close()
        driver.quit()
    return current_url
