import cv2
import os

# 設定影片路徑和輸出資料夾
video_path = 'final_project.mp4'  # 替換為您的影片路徑
output_folder = 'output_images/'  # 替換為您的輸出資料夾

# 確認資料夾存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打開影片
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("無法打開影片，請檢查路徑！")
    exit()

# 獲取影片參數
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"影片 FPS: {fps}, 總幀數: {total_frames}")

# 計算提取間隔
frames_to_extract = 500
step = total_frames // frames_to_extract
if step == 0:
    print("影片太短，無法提取500張圖片！")
    exit()

count = 0
saved_count = 0

while cap.isOpened() and saved_count < frames_to_extract:
    ret, frame = cap.read()
    if not ret:
        print("影片讀取完成或出錯")
        break

    # 保存指定幀
    if count % step == 0:
        output_file = f"{output_folder}/frame_{saved_count:04d}.jpg"
        cv2.imwrite(output_file, frame)
        print(f"保存圖片: {output_file}")
        saved_count += 1

    count += 1

cap.release()
print(f"完成，共保存了 {saved_count} 張圖片。")
