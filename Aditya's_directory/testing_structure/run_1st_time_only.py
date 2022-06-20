import json

all_usernames_python_object = []
all_usernames_json_object = json.dumps(all_usernames_python_object)
f = open("username_existence_check", "w")
f.write(all_usernames_json_object)
f.close()

f = open("all_transaction_history", "w")
f.write("")
f.close()
