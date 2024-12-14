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
