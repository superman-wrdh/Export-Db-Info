# -*- coding: utf-8 -*-
# -*- author: hechao -*-

import os
from core.config import config
from core.db_info import get_db_table_info_data
from jinja2 import PackageLoader, Environment


def render_html(db_name, db_real_name, tables):
    env = Environment(loader=PackageLoader("html", "templates"))
    template = env.get_template('index.html')
    table_count = len(tables)
    html = template.render(tables=tables, db_name=db_name, table_count=table_count, db_real_name=db_real_name)
    out_put_path = os.path.join("html", "output")
    if not os.path.exists(out_put_path):
        os.makedirs(out_put_path)
    file = open(os.path.join(out_put_path, "{}.html".format(db_name)), "w", encoding="utf8")
    file.write(html)
    file.close()


def output_html():
    for db in config():
        name = db.get("name")
        try:
            db_info = get_db_table_info_data(**db)
            render_html(db_name=name, db_real_name=db.get("db"), tables=db_info)
        except Exception as e:
            print("exception {}".format(e))
