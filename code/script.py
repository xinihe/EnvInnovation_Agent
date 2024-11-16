import os
from transformers import MarianMTModel, MarianTokenizer, PegasusForConditionalGeneration, PegasusTokenizer

# 加载中文到英文的MarianMT翻译模型
model_name_translation = "Helsinki-NLP/opus-mt-zh-en"
tokenizer_translation = MarianTokenizer.from_pretrained(model_name_translation)
model_translation = MarianMTModel.from_pretrained(model_name_translation)

# 加载英文总结的Pegasus模型
model_name_summary = "google/pegasus-xsum"
tokenizer_summary = PegasusTokenizer.from_pretrained(model_name_summary)
model_summary = PegasusForConditionalGeneration.from_pretrained(model_name_summary)

# 设置文件夹路径
input_folder = "outputtxt"
output_folder_translation = "outputtxt(英文)"
output_folder_summary = "outputtxt(总结)"

# 创建输出文件夹（如果不存在的话）
os.makedirs(output_folder_translation, exist_ok=True)
os.makedirs(output_folder_summary, exist_ok=True)

# 分割文本为基于 Token 的段落
def split_text_by_tokens(text, tokenizer, max_tokens):
    """将文本按 Token 数分割为多个段"""
    inputs = tokenizer(text, return_tensors="pt", padding=False, truncation=False)
    input_ids = inputs["input_ids"][0]  # 获取 Token 化后的 ID 列表
    # 按 max_tokens 分割 Token
    segments = [input_ids[i:i + max_tokens] for i in range(0, len(input_ids), max_tokens)]
    return segments

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    input_file_path = os.path.join(input_folder, filename)
    
    if os.path.isfile(input_file_path):
        print(f"正在处理文件: {filename}")
        
        # 读取中文文本文件
        with open(input_file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # 提取原文的第一行（假设第一行是1或0）
        lines = text.splitlines()
        first_line = lines[0].strip()  # 读取原文的第一行（"1" 或 "0"）
        remaining_text = "\n".join(lines[1:])

        # 按 Token 数分割文本
        max_translation_tokens = 512  # 翻译模型的最大 Token 数
        translation_segments = split_text_by_tokens(remaining_text, tokenizer_translation, max_translation_tokens)

        # 翻译后的文本
        translated_text = "
        # 逐段翻译
        for segment in translation_segments:
            # 将分段 ID 转回原文本
            inputs = {"input_ids": segment.unsqueeze(0)}
            translated = model_translation.generate(**inputs)
            translated_segment = tokenizer_translation.decode(translated[0], skip_special_tokens=True)
            translated_text += translated_segment + "\n"  # 加换行符分隔段落

        # 保存翻译结果
        output_file_path_translation = os.path.join(output_folder_translation, f"{filename}_translated.txt")
        with open(output_file_path_translation, "w", encoding="utf-8") as output_file:
            output_file.write(translated_text)

        print(f"翻译后的文本已保存到: {output_file_path_translation}")

        # 生成摘要
        max_summary_tokens = 1024  # 摘要模型的最大 Token 数
        summary_segments = split_text_by_tokens(translated_text, tokenizer_summary, max_summary_tokens)

        summaries = []
        for segment in summary_segments:
            inputs = {"input_ids": segment.unsqueeze(0)}
            summary_ids = model_summary.generate(inputs["input_ids"], max_length=60, num_beams=4, length_penalty=2.0, early_stopping=True)
            summary = tokenizer_summary.decode(summary_ids[0], skip_special_tokens=True)
            summaries.append(summary)

        # 将所有批次的摘要合并，并在首行添加原文的第一行
        final_summary = first_line + "\n" + " ".join(summaries)

        # 保存摘要结果
        output_file_path_summary = os.path.join(output_folder_summary, f"{filename}_summary.txt")
        with open(output_file_path_summary, "w", encoding="utf-8") as output_file:
            output_file.write(final_summary)

        print(f"摘要已保存到: {output_file_path_summary}")