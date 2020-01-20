# -*- coding: utf-8 -*-
import pymysql


class TableField(object):
    def __init__(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        return pymysql.connect(
            host='192.168.3.4',
            user='shejiben',
            password='1982425',
            db='shejiben',
            charset='utf8',
        )

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_table_field(self, table_name):
        sqli = "select * from %s limit 1;" % table_name
        self.cursor.execute(sqli)
        # 显示每列的详细信息
        des = self.cursor.description
        # 获取表头
        field_list = [item[0] for item in des]
        return field_list


if __name__ == '__main__':
    obj = TableField()
    designer_field = obj.get_table_field("to8to_designer")
    num_field = obj.get_table_field("to8to_designer_numinfo")
    user400_field = obj.get_table_field("to8to_user400")
    es_field_list = ["space_tags", "uid", "shen", "mainfield", "truename", "is_show", "case_num", "collect_num", "id",
                     "city", "pic_num", "elite_num", "attention_num", "name_rz", "min_price", "extensionnum",
                     "goodlevel", "spaceStr", "type", "sign_num", "user_score", "cxt_num", "cxt_year", "name_rz_status",
                     "odate", "case_show_num", "apply_status", "ident", "regdate", "yuyue_nums", "otype", "workyears",
                     "otherfield", "max_price", "appraise_num"]
    es_extra_field = set(es_field_list).difference(set(designer_field))
    es_extra_field = es_extra_field.difference(set(num_field))
    es_extra_field = es_extra_field.difference(set(user400_field))
    print es_extra_field
