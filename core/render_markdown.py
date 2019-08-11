from collections import OrderedDict
import os
import pandas as pd
from core.config import config
from core.db_info import get_db_table_info_data


def write_table(df, file, order_columns=None):
    SP = " | "
    lines = []
    cols = df.columns.tolist() if order_columns is None else order_columns
    col_str = SP.join(cols)
    lines.append(col_str)
    p = SP.join([":-:"] * len(cols))
    lines.append(p)
    for _, row in df.iterrows():
        d = row.to_dict()
        line = []
        for k in cols:
            line.append(str(d.get(k)))
        lines.append(SP.join(line))
    for i in lines:
        file.write(i + "\n")


def sort_dict(d):
    return OrderedDict(Field=d.get("Field"),
                       Type=d.get("Type"),
                       Key=d.get("Key"),
                       Default=d.get("Default"),
                       Null=d.get("Null"),
                       Extra=d.get("Extra"),
                       )


def write_to_md(table_name, field, file):
    field = [sort_dict(d) for d in field]
    df = pd.DataFrame(data=field)
    df = df.where(df.notnull(), "null")
    file.write("## 表名:{}\n".format(table_name))
    write_table(df=df, file=file, order_columns=df.columns.tolist())
    file.write("\n\n\n")
    file.flush()


def output_md():
    for db in config():
        name = db.get("name")
        markdown_output = "markdown_output"
        if not os.path.exists(markdown_output):
            os.makedirs(markdown_output)
        file_path = os.path.join(markdown_output, name + ".md")
        with open(file_path, "w", encoding="utf8") as file:
            try:
                result = get_db_table_info_data(**db)
                for d in result:
                    table_name = d.get("table_name")
                    table_fields = d.get("table_fields")
                    write_to_md(table_name=table_name, field=table_fields, file=file)
                    file.flush()
            except Exception as e:
                print("exception {}".format(e))
                print("remove {}".format(file_path))
                file.close()
                os.remove(file_path)

# if __name__ == '__main__':
#     main()
