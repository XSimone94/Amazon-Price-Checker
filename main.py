from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Imposta le opzioni di Chrome
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

# Imposta un User-Agent per evitare blocchi di Amazon
chrome_option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Avvia il browser
driver = webdriver.Chrome(options=chrome_option)

# Apri la pagina di Amazon
driver.get("https://www.amazon.it/dp/B07W8PPQQM")

# Aspetta che il prezzo sia visibile (massimo 10 secondi)
try:
    price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price"))
    )
    print(f"Il prezzo del prodotto è: {price_element.text} €")
except:
    print("❌ Errore: Impossibile trovare il prezzo!")

# Chiude il browser
driver.quit()
