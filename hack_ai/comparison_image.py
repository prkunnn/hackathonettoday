import pandas as pd
from sentence_transformers import SentenceTransformer, util
from googletrans import Translator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # BERT語言模型
translator = Translator()

def compare(news_in):
    translated_text = translator.translate(news_in, src='zh-TW', dest='en').text
    embedding1 = model.encode([translated_text], convert_to_tensor=True) 
    
    # 從excel的特定欄位中抓取資料
    df = pd.read_excel('IC_image.xlsx')
    text_b = df['標籤'].tolist()
    text_a = df['圖像'].tolist()

    similarity = []  # 相似度包含（相似值、文本和圖像）

    # 提前計算嵌入向量
    embedding2_list = model.encode(text_b, convert_to_tensor=True)

    for i, embedding2 in enumerate(embedding2_list):
        cosine_similarity = util.pytorch_cos_sim(embedding1, embedding2)
        similarity.append((cosine_similarity[0][0].item() * 100, text_b[i], text_a[i]))

    similarity = sorted(similarity, key=lambda x: x[0], reverse=True)

    # 輸出前五名的排序，包括相似的圖像
    result = []  # 由高至低

    for a in range(5):
        s, t, text_a = similarity[a]
        result.append("此串文字與 {} 相似度: {:.2f}%，對應的 A：{}".format(t, s, text_a))
        # 顯示相似的圖像
        img_path = "IC_image/" + text_a
        img = mpimg.imread(img_path)
        plt.imshow(img)
        plt.axis('off')
        plt.savefig(f"similar_image_{a}.jpg", format="jpg")  # 將圖像保存為 JPG 文件
        
    return result

