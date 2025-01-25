import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

acccounts = int(len(sys.argv[1:])/2)
print(f'Config {acccounts} accounts')
for i in range(acccounts):
    email = sys.argv[1+i]
    passwd = sys.argv[1+i+acccounts]
    print('----------------------------')

    # 1. Open browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i+1} loading game...')
    sleep(20)  # wait for page load

    # 2. Input email
    screen = driver.find_element(By.ID, 'layaCanvas')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, -100)\
        .click()\
        .perform()
    driver.find_element(By.NAME, 'input').send_keys(email)
    print('Input email successfully')

    # 3. Input password
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, -50)\
        .click()\
        .perform()
    driver.find_element(By.NAME, 'input_password').send_keys(passwd)
    print('Input password successfully')

    # 4. Click login
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, 50)\
        .click()\
        .perform()
    print('Entering game...')

    # 5. Wait for game page to load (first time)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'gameMain'))  # Replace 'gameMain' with actual element ID
        )
        print('Game loaded successfully')
    except:
        print('Game did not load in time')

    # 6. Click login again after waiting for page to load
    print('Clicking login again...')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, 50)\
        .click()\
        .perform()

    # 7. Wait for game page to load again after second click
    print('Waiting for game page to load after second click...')
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'gameMain'))  # Replace 'gameMain' with actual element ID
        )
        print('Game loaded successfully after second click')
    except:
        print('Game did not load in time after second click')

    # 8. Quit the driver after finishing
    driver.quit()
