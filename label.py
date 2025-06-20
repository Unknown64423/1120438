import cv2
import os

# 設定路徑
image_folder = "images"
output_txt = "annotations/positives.txt"

# 建立輸出資料夾
os.makedirs("annotations", exist_ok=True)

# 取得圖片清單
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))]

index = 0
drawing = False
ix, iy = -1, -1
rectangles = []

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rectangles

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rectangles.append((ix, iy, x - ix, y - iy))

while index < len(image_files):
    img_path = os.path.join(image_folder, image_files[index])
    img = cv2.imread(img_path)
    temp_img = img.copy()
    rectangles = []

    cv2.namedWindow("Label")
    cv2.setMouseCallback("Label", draw_rectangle)

    while True:
        for (x, y, w, h) in rectangles:
            cv2.rectangle(temp_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Label", temp_img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):  # 儲存
            with open(output_txt, "a") as f:
                line = f"{image_folder}/{image_files[index]} {len(rectangles)}"
                for (x, y, w, h) in rectangles:
                    line += f" {x} {y} {w} {h}"
                f.write(line + "\n")
            break
        elif key == ord("r"):  # 重設
            temp_img = img.copy()
            rectangles = []
        elif key == ord("n"):  # 跳下一張
            break
        elif key == ord("q"):  # 結束
            exit()

    index += 1
    cv2.destroyAllWindows()