import tkinter as tk
from PIL import Image, ImageTk
import title_ganerate as title
import comparison_image as cpimage
import re
from tkinter import PhotoImage
# import dw

def copy_text():
    root.clipboard_clear()  # 清空剪贴板
    root.clipboard_append(title_label.cget("text"))  # 将标签文本复制到剪贴板
    root.update()  # 更新剪贴板

# 創建一個Tkinter視窗
root = tk.Tk()
root.title("新聞相片比對程式")
root.geometry("800x800")

# 加载背景图像
background_image = PhotoImage(file="01010.png")

# 创建Label来显示背景图像
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # 填充整个窗口

# 创建全局变量来存储PhotoImage对象
image_labels = []
image_labels_right=[]


    
def exit_app():
    root.quit()

def resize(result_image):
    # 調整圖像大小，寬度為200像素，保持比例
    new_width = 200
    width_percent = (new_width / float(result_image.size[0]))
    new_height = int((float(result_image.size[1]) * float(width_percent)))
    result_image = result_image.resize((new_width, new_height))
    return result_image

def compare_photos():
    news_in=news_text.get("1.0", "end-1c")
    news_in = news_in.replace("在這裡輸入您的新聞內容，我們會進行比對:", "")
    news_title=title.reply(news_in)
    result = cpimage.compare(news_in)

    image_files = ["similar_image_0.jpg","similar_image_1.jpg","similar_image_2.jpg","similar_image_3.jpg","similar_image_4.jpg"]
    for label in image_labels:
        label.destroy()
        image_labels.clear()

    for label in image_labels_right:
        label.destroy()
    image_labels_right.clear()

    for i, image_file in enumerate(image_files):
        result_photo = ImageTk.PhotoImage(resize(Image.open(image_file)))
        label = tk.Label(root, image=result_photo)
        label.image = result_photo
        label.grid(row=i + 1, column=1, padx=0, pady=0)
        image_labels.append(label)

        # 添加标注到右侧
    # 获取相似度的文本
        similarity_match = re.search(r'相似度:\s(\d+\.\d+)%', result[i])
        similarity_text = similarity_match.group(1) if similarity_match else "N/A"

    # 创建 label_right 标签
        label_right = tk.Label(root, text=f"相似度:{similarity_text}%", width=10, wraplength=100, anchor="nw", justify="left")
        label_right.grid(row=i + 1, column=2, padx=10, pady=10, sticky="w")
        image_labels_right.append(label_right)
    ####
    # download_button=dw.togo()
    title_label.config(text="我們生成的新聞標題是: " + news_title, anchor="nw",justify="left",width=40, height=10,wraplength=350)
    copy_button = tk.Button(root, text="複製生成的標題", command=copy_text)
    copy_button.grid(row=4, column=0, padx=10, pady=10)
    
##下載按鈕

# 新聞輸入區
news_text = tk.Text(root, width=50, height=10)
news_text.grid(row=1, column=0, padx=10, pady=10)
news_in = news_text.insert("1.0", "在這裡輸入您的新聞內容，我們會進行比對:")

# 顯示新聞標題的標籤
title_label = tk.Label(root, anchor="w")
title_label.grid(row=1, column=0, padx=1, pady=1,rowspan=4)

# 比對按鈕
compare_button = tk.Button(root, text="產生標題與圖片", command=compare_photos)
compare_button.grid(row=0, column=0, padx=1, pady=1)

exit_button = tk.Button(root, text="關閉應用程式", command=exit_app, bg="red")
exit_button.grid(row=0, column=1, padx=1, pady=1)

# 创建一个标签来显示 "圖片詳細資料"
detail_label = tk.Label(root, text="圖片相似度",anchor="center")
detail_label.grid(row=0, column=2, padx=10, pady=10)


# 啟動Tkinter主迴圈
root.mainloop()