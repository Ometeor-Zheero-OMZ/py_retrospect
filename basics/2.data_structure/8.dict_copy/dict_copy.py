########
# 辞書 #
########
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

# {'id': '01', 'work': 'Angel Beats!', 'name': '立華', 'gender': 'female'}
print(d)

###############
# 辞書のコピー #
###############
copied_d = d.copy()
copied_d["birth"] = "Feb 25"

# {'id': '01', 'work': 'Angel Beats!', 'name': '立華', 'gender': 'female', 'birth': 'Feb 25'}
print(copied_d)
