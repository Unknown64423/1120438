from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

def download_images(search_query, output_folder, num_images=1000):
    # 建立資料夾
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 啟動 WebDriver（確保您已下載相應的瀏覽器驅動程式）
    driver = webdriver.Chrome()  # 或其他瀏覽器驅動程式
    driver.get(f"https://www.google.com/search?q={search_query}&tbm=isch")
    time.sleep(2)

    # 滑動加載更多圖片
    scrolls = num_images // 20  # 每次加載約20張圖片
    for _ in range(scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # 抓取圖片 URL
    images = driver.find_elements(By.CSS_SELECTOR, "img")
    print(f"找到 {len(images)} 張圖片，開始下載...")

    count = 0
    for i, img in enumerate(images):
        if count >= num_images:
            break
        try:
            src = img.get_attribute("src")
            if src:
                response = requests.get(src, stream=True)
                file_path = os.path.join(output_folder, f"image_{count:04d}.jpg")
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"下載完成：{file_path}")
                count += 1
        except Exception as e:
            print(f"下載失敗：{e}")
    
    driver.quit()
    print(f"已下載 {count} 張圖片到 {output_folder}")

# 使用範例
download_images("negative sample images", "negative_samples", num_images=1000)
