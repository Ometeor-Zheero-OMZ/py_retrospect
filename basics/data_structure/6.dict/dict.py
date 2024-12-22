d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

d["feature"] = ["slash with a blade", "pig out Mapo Tofu"]

# {'id': '01', 'work': 'Angel Beats!', 'name': '立華', 'gender': 'female', 'feature': ['slash with a blade', 'pig out Mapo Tofu']}
print(d)

#################
# JSON形式に整形 #
#################
import json


# {
#     "id": "01",
#     "work": "Angel Beats!",
#     "name": "立華",
#     "gender": "female",
#     "feature": [
#         "slash with a blade",
#         "pig out Mapo Tofu"
#     ]
# }
print(json.dumps(d, ensure_ascii=False, indent=4))

#### JSONを出力
import os

# スクリプトが存在するディレクトリの絶対パスを取得
current_dir = os.path.dirname(os.path.abspath(__file__))

# JSONファイルのパスを作成
path = os.path.join(current_dir, "data.json")

# JSON形式でファイルに保存
with open("./data.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=4)