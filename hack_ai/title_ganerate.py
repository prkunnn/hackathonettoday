import openai

openai.api_key = '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'

def reply(t_input):
# 使用OpenAI API生成文章標題和標籤
    response = openai.Completion.create(
        engine="text-davinci-003",
        # 使用文章内容作为提示
        prompt=f"幫我整理出三個適合這篇文章的新聞標題(標題請使用數字列點表示)，和十個適合這篇文章的標籤(標籤請使用#表示)：\n{t_input}\n標題：",
        max_tokens=300,  # 最大長度
        n=1  # 只生成一組標題和標籤
    )

    # 提取生成的文章標題和標籤
    generated_text = response['choices'][0]['text']
    return generated_text

