import argparse
from core.render_markdown import output_md
from core.render_html import output_html
from core.export_ddl import output_ddl_sql

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="输出数据库信息到markdown/html/pdf",
        usage="""
            python main.py -t [type]
            """,
        description="""
                输出数据库表结构信息到markdown/html/pdf
            """,
        epilog="That's all. Thank you for using it ！",
        add_help=True
    )
    parser.add_argument('-t', "--type", default='md', help="输出类型")
    args = parser.parse_args()
    output_type = args.type
    if output_type in ('md', 'markdown', 'MD', 'MARKDOWN'):
        output_md()
    elif output_type in ('html', 'HTML'):
        output_html()
    elif output_type in ('pdf', 'PDF'):
        print("TODO 暂未实现")
    elif output_type in ('ddl', "DDL"):
        output_ddl_sql()
    else:
        print("参数错误")
