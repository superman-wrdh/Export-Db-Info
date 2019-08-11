import yaml


def config():
    data = yaml.load(open("db.yaml", "r", encoding="utf8"))
    data_list = [{
        "name": data[k].get("name"),
        "host": data[k].get("master").get("host"),
        "port": data[k].get("master").get("port"),
        "user": data[k].get("master").get("user"),
        "pass": data[k].get("master").get("pass"),
        "db": data[k].get("master").get("db"),
    } for k in data]
    return data_list
