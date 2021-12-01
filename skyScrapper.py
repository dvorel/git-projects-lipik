import time
import undetected_chromedriver.v2 as webdriver
from webdriver_manager.chrome import ChromeDriverManager


#pip install undetected-chromedriver
#mozda treba napraviti folder -> C:\chrome_temp
#python=3.10.0




destination = []
price = []
airline = []
departure_date = []
date_of_arrival = []

if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.user_data_dir = "C:\chrome_temp"
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')


    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.delete_all_cookies()
    driver.start_client()
    time.sleep(1)
    driver.get("https://www.skyscanner.net/hr/en-gb/hrk/flights/last-minute-deals/")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//*[@id=\"acceptCookieButton\"]").click()
    except:
        print("No Cookie")
    time.sleep(5)
    while True:
        try:
            driver.find_element_by_xpath("//*[@id=\"flight-deals-root\"]/div/div[2]/button").click()
            time.sleep(1)
        except:
            break

    gradovi = driver.find_elements_by_class_name("BpkText_bpk-text__1KKbW.BpkText_bpk-text--xl__2xBzx.DealCard_DealCard__placeName__1CMcr")  
    for grad in gradovi:
        destination.append(grad.text)
        print(grad.text)

    cijene = driver.find_elements_by_class_name("BpkText_bpk-text__1KKbW.BpkText_bpk-text--lg__212sq.DealCard_DealCard__price__1O9CP")
    for cijena in cijene:
        print(cijena.text)
    
    
    letovi = driver.find_elements_by_class_name("BpkText_bpk-text__1KKbW.BpkText_bpk-text--base__1zXAn")
    for let in letovi:
        print(let.text)
    

    # for cj in cijena:
    #     print(cj.text)



    print("end")
