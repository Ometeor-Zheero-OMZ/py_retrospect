d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

#############
# キーを取得 #
#############
# dict_keys(['id', 'work', 'name', 'gender'])
print(d.keys())

###########
# 値を取得 #
###########
# dict_values(['01', 'Angel Beats!', '立華', 'female'])
print(d.values())

########################
# 辞書を別の辞書で上書き #
########################
other_d = { "work": "かぎなど", "death_cause": "unknown" }
d.update(other_d)

# {'id': '01', 'work': 'かぎなど', 'name': '立華', 'gender': 'female', 'death_cause': 'unknown'}
print(d)

########################
# キーを指定して値を取得 #
########################
# 立華
print(d.get("name"))

########################
# 指定した要素を取り出す #
########################
d.pop("gender")
# del でも可能
# del d["gender"]

# {'id': '01', 'work': 'かぎなど', 'name': '立華', 'death_cause': 'unknown'}
print(d)

#################
# 辞書を空にする #
#################
d.clear()

# {}
print(d)