import os
from PIL import Image

# 圖片目錄和輸出檔案
images_dir = r"C:\Users\Unknown\Desktop\視覺\images"  # 替換為您的圖片目錄
output_file = r"C:\Users\Unknown\Desktop\視覺\all_images_pixels.txt"  # 最終整合的輸出文件

# 檢查目錄是否存在
if not os.path.exists(images_dir):
    print(f"Error: Directory does not exist: {images_dir}")
    exit(1)

# 開啟輸出文件
with open(output_file, "w") as output:
    processed_count = 0
    for image_name in os.listdir(images_dir):
        if image_name.lower().endswith(('.jpg', '.png', '.jpeg')):  # 支援常見圖片格式
            image_path = os.path.join(images_dir, image_name)
            try:
                print(f"Processing image: {image_name}")  # 新增日誌
                # 讀取圖片
                image = Image.open(image_path)
                pixels = list(image.getdata())
                width, height = image.size

                # 將圖片資訊寫入 TXT
                output.write(f"Image: {image_name}\n")
                output.write(f"Size: {width}x{height}\n")
                output.write("Pixels (R, G, B):\n")
                
                # 每個像素值寫成單獨一行
                for y in range(height):
                    row = pixels[y * width:(y + 1) * width]
                    for r, g, b in row:
                        output.write(f"({r},{g},{b})\n")
                output.write("\n")  # 分隔每張圖片的數據
                processed_count += 1
            except Exception as e:
                print(f"Error processing {image_name}: {e}")

if processed_count == 0:
    print("No images were processed. Please check the image directory and file formats.")
else:
    print(f"All images processed successfully. Total: {processed_count}. Output saved to {output_file}")
