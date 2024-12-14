import json
import pandas as pd

# # 使用pandas读取对话抽取的.jsonl文件
# data_read_dir = 'data/SGYY.jsonl'
# dialogues = pd.read_json(data_read_dir, lines=True)
# # print(dialogues.head())


# def build_json_data(dialogues, json_file):
#     result = []
#     for i in range(0, len(dialogues)):
#         sample = {
#             "instruction": dialogues.iloc[i]['input'],
#             "input": "",
#             "output": dialogues.iloc[i]['target']
#         }
#         result.append(sample)

#     with open(json_file, 'w', encoding='utf-8') as f:
#         json.dump(result, f, ensure_ascii=False, indent=4)


# data_save_dir = 'data/dataset.json'
# # build_json_data(dialogues, data_save_dir )



# 使用json读取对话抽取的.jsonl文件
data_read_dir = 'data/SGYY.jsonl'
with open(data_read_dir, 'r', encoding='utf-8') as f:
    dialogues = []
    for line in f:
        contennt = json.loads(line)
        dialogues.append(contennt)

# 打印问答数
print(len(dialogues))


# 定义转换json函数
def build_json_data(dialogues, json_file):
    result = []
    for act in dialogues:
        sample = {
            "instruction": act["input"],
            "input": "",
            "output": act["target"]
        }
        result.append(sample)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

# 
data_save_dir = 'data/dataset.json'
build_json_data(dialogues, data_save_dir)







# def data_preprocess(data):
#     sentences = []
#     for sentence in data.split('。'):  # 使用句号作为切分符
#         sentences.append(sentence)

#     # 将句子合并成800字一段的段落
#     paragraphs = []
#     current_paragraph = ''
#     for sentence in sentences:
#         if len(current_paragraph) + len(sentence) <= 800:
#             current_paragraph += sentence+'。'
#         else:
#             paragraphs.append(current_paragraph.strip())
#             current_paragraph = sentence

#     # 将最后一段加入到段落列表中
#     if current_paragraph:
#         paragraphs.append(current_paragraph.strip())
#     return paragraphs


# data_dir = 'data\SGYY.txt'
# with open(data_dir, 'r', encoding='utf-8') as f:
#     content = f.read()
#     # print(content)


# paragraphs = data_preprocess(content)
# # 打印切分后的段落
# for idx, paragraph in enumerate(paragraphs):
#     print(f'段落 {idx + 1}: {paragraph}')
#     break

# data_dir = 'data\content.txt'
# with open(data_dir, 'w') as f:
#     f.writelines(paragraphs)
