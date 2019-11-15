# -*- coding: utf-8 -*-
import re


def another():
    sql = u"啊"
    reg = ur"[\u4e00-\u9fa5]+"
    match_obj = re.match(reg, sql)
    if match_obj and match_obj.group() == sql:
        print match_obj.group()


def main():
    sql = u'SELECT t.`id`,m.uid,t.`name`, e.`str`AS 联系方式 FROM to8to_it.`tit_account` t  LEFT JOIN t8t_sys_pms.`to8to_encode` e ON t.phone_id = e.eid  LEFT JOIN to8to.to8to_members m ON t.`id` = m.account_id WHERE m.`uid` IN(11503550,11791416,12083619,11148351,12142005,11003484,10597983,10933637,11442128,11710545,12099146,11274723,12236015,10960661)'
    # sql = u'SELECT t.`id`,m.uid,t.`name`, e.`str` FROM to8to_it.`tit_account` t  LEFT JOIN t8t_sys_pms.`to8to_encode` e ON t.phone_id = e.eid  LEFT JOIN to8to.to8to_members m ON t.`id` = m.account_id WHERE m.`uid` IN(11503550,11791416,12083619,11148351,12142005,11003484,10597983,10933637,11442128,11710545,12099146,11274723,12236015,10960661)'

    reg = ur"^(select|explain)\s*[\s\w`*(),.\u4e00-\u9fa5]*?from.*"

    match_obj = re.match(reg, sql, re.I)
    if match_obj and match_obj.group() == sql:
        print "match"
    else:
        print "not match"


if __name__ == '__main__':
    main()
    # another()
