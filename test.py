# -*- coding: utf-8 -*-
import json
import os
import time


def test_input():
    print "hahaha"
    name = input("hello, what's your name?")
    print name
    pass


def split_str():
    a_str = '{"error":0,"message":"refresh token","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTg0NDIsIm5hbWUiOiJ3YXRzb24uemVuZyIsImVtYWlsIjoiIiwiZXhwIjoxNTY4ODYwODU2LCJpc3MiOiJlZC5kZW5nIn0.75MM0ddu03RxXBFkTRtW3XPd9KNb3iLmpI05P-kjHhA"}{"code":200,"data":{"appName":"t8t-scm-oos","env":"pro","switchVersion":"","currentVersion":" sc_108 rpc_proxy","versionType":"","localType":false,"SwitchType":"","userName":"","passCode":"","registery":[{"name":"eureka","env":"pro","service":["http://idceureka.we.com:9761/eureka"],"route_path":"","report_path":"","last_version":"106","version":"sc_108","enable":false},{"name":"zk","env":"pro","service":["idczk.we.com:29090"],"route_path":"/biz/t8t-scm-oos/app/policy/default/route","report_path":"/biz/t8t-scm-oos/app/instance","last_version":"proxy","version":"rpc_proxy","enable":false},{"name":"apollo","env":"pro","service":["http://idcapollo.we.com:9098"],"route_path":"/apps/t8t-sc-architecture-public/envs/IDC/clusters/default/namespaces/1.service-route-info/item/password/yunwei","report_path":"/apps/t8t-sc-architecture-public/envs/IDC/clusters/default/namespaces/1.t8t-sc-service-name-adaptive/items","last_version":"0","version":"0","enable":false}],"instance":[{"name":"10.10.11.65:t8t-scm-oos:40925","env":"pro","version":"108","report_ip":"10.10.11.65","status":"UP","register":"eureka","start_time":"2019-09-17 11:31:45","bind_ip":"0.0.0.0","pid":35047,"port":40925,"type":1,"proxyed":"false","merge":""},{"name":"10.10.11.50:t8t-scm-oos:40211","env":"pro","version":"108","report_ip":"10.10.11.50","status":"UP","register":"eureka","start_time":"2019-09-17 11:27:46","bind_ip":"0.0.0.0","pid":92929,"port":40211,"type":1,"proxyed":"false","merge":""},{"name":"proxy_e6763","env":"pro","version":"proxy","report_ip":"10.10.10.99","status":"UP","register":"zk","start_time":"2019-09-16 12:02:47","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_a933c","env":"pro","version":"proxy","report_ip":"10.10.11.60","status":"UP","register":"zk","start_time":"2019-09-16 16:49:40","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_8d172","env":"pro","version":"proxy","report_ip":"10.10.10.114","status":"UP","register":"zk","start_time":"2019-09-09 17:43:44","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_1693d","env":"pro","version":"proxy","report_ip":"10.10.11.61","status":"UP","register":"zk","start_time":"2019-09-16 21:53:41","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_0872e","env":"pro","version":"proxy","report_ip":"10.10.11.46","status":"UP","register":"zk","start_time":"2019-09-16 12:29:32","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_94f33","env":"pro","version":"proxy","report_ip":"10.10.10.51","status":"UP","register":"zk","start_time":"2019-09-16 15:25:41","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_0d11e","env":"pro","version":"proxy","report_ip":"10.10.10.30","status":"UP","register":"zk","start_time":"2019-09-16 21:23:55","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_b3052","env":"pro","version":"proxy","report_ip":"10.10.10.82","status":"UP","register":"zk","start_time":"2019-09-16 21:37:46","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""}],"version":[{"value":"108","label":"sc_108","appName":"t8t-scm-oos","versionType":"sc","env":"pro","merge":""},{"value":"proxy","label":"rpc_proxy","appName":"t8t-scm-oos","versionType":"proxy","env":"pro","merge":""}]},"msg":""}'
    # a_str = '{"code":200,"data":{"appName":"t8t-scm-oos","env":"pro","switchVersion":"","currentVersion":" sc_108 rpc_proxy","versionType":"","localType":false,"SwitchType":"","userName":"","passCode":"","registery":[{"name":"eureka","env":"pro","service":["http://idceureka.we.com:9761/eureka"],"route_path":"","report_path":"","last_version":"106","version":"sc_108","enable":false},{"name":"zk","env":"pro","service":["idczk.we.com:29090"],"route_path":"/biz/t8t-scm-oos/app/policy/default/route","report_path":"/biz/t8t-scm-oos/app/instance","last_version":"proxy","version":"rpc_proxy","enable":false},{"name":"apollo","env":"pro","service":["http://idcapollo.we.com:9098"],"route_path":"/apps/t8t-sc-architecture-public/envs/IDC/clusters/default/namespaces/1.service-route-info/item/password/yunwei","report_path":"/apps/t8t-sc-architecture-public/envs/IDC/clusters/default/namespaces/1.t8t-sc-service-name-adaptive/items","last_version":"0","version":"0","enable":false}],"instance":[{"name":"10.10.11.65:t8t-scm-oos:40925","env":"pro","version":"108","report_ip":"10.10.11.65","status":"UP","register":"eureka","start_time":"2019-09-17 11:31:45","bind_ip":"0.0.0.0","pid":35047,"port":40925,"type":1,"proxyed":"false","merge":""},{"name":"10.10.11.50:t8t-scm-oos:40211","env":"pro","version":"108","report_ip":"10.10.11.50","status":"UP","register":"eureka","start_time":"2019-09-17 11:27:46","bind_ip":"0.0.0.0","pid":92929,"port":40211,"type":1,"proxyed":"false","merge":""},{"name":"proxy_e6763","env":"pro","version":"proxy","report_ip":"10.10.10.99","status":"UP","register":"zk","start_time":"2019-09-16 12:02:47","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_a933c","env":"pro","version":"proxy","report_ip":"10.10.11.60","status":"UP","register":"zk","start_time":"2019-09-16 16:49:40","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_8d172","env":"pro","version":"proxy","report_ip":"10.10.10.114","status":"UP","register":"zk","start_time":"2019-09-09 17:43:44","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_1693d","env":"pro","version":"proxy","report_ip":"10.10.11.61","status":"UP","register":"zk","start_time":"2019-09-16 21:53:41","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_0872e","env":"pro","version":"proxy","report_ip":"10.10.11.46","status":"UP","register":"zk","start_time":"2019-09-16 12:29:32","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_94f33","env":"pro","version":"proxy","report_ip":"10.10.10.51","status":"UP","register":"zk","start_time":"2019-09-16 15:25:41","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_0d11e","env":"pro","version":"proxy","report_ip":"10.10.10.30","status":"UP","register":"zk","start_time":"2019-09-16 21:23:55","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""},{"name":"proxy_b3052","env":"pro","version":"proxy","report_ip":"10.10.10.82","status":"UP","register":"zk","start_time":"2019-09-16 21:37:46","bind_ip":"0.0.0.0","pid":0,"port":40001,"type":1,"proxyed":"true","merge":""}],"version":[{"value":"108","label":"sc_108","appName":"t8t-scm-oos","versionType":"sc","env":"pro","merge":""},{"value":"proxy","label":"rpc_proxy","appName":"t8t-scm-oos","versionType":"proxy","env":"pro","merge":""}]},"msg":""}'
    str_list = a_str.split("}{")
    if len(str_list) > 1:
        refresh = json.loads(str_list[0] + "}")
        print refresh
        data = json.loads("{" + str_list[1])
    else:
        data = json.loads(str_list[0])
    print data


def get_format_datetime(date_format='%Y%m%d%H%M'):
    return time.strftime(date_format, time.localtime(time.time()))


def execute_command(cmd):
    # print cmd
    import os
    a_pipe = os.popen(cmd, 'r')
    a_text = a_pipe.read()
    a_sts = a_pipe.close()
    if a_sts is None: a_sts = 0
    if a_text[-1:] == '\n': a_text = a_text[:-1]
    # print a_sts
    # print a_text
    if a_sts:
        print cmd
        print a_sts
        print a_text
        raise Exception(a_text)
    return a_sts, a_text


class Project(object):
    def __init__(self, proj_path, test_branch):
        if not proj_path:
            print "project directory can not be null"
            exit(0)
        self.project_dir = proj_path
        self.test_branch = test_branch

    def pull_origin(self, branch):
        execute_command("git pull origin %s" % branch)

    def checkout(self, branch):
        execute_command("git checkout %s" % branch)

    def get_version(self, version_str):
        version_list = version_str.split(".")
        version_num = "".join(version_list)
        version_num = str(int(version_num) + 1)
        num_list = list(version_num)
        return ".".join(num_list)

    def get_last_tag(self):
        execute_command("git fetch --tag")
        # 有时需要先grep
        return execute_command("git tag | tail -1")

    def push_origin(self, branch):
        execute_command("git push origin %s" % branch)

    def this_branch(self):
        os.chdir(self.project_dir)
        status, branch = execute_command("git symbolic-ref --short -q HEAD")
        return branch

    def is_clean(self):
        os.chdir(self.project_dir)
        status, output = execute_command("git status")
        if output.find("nothing added to commit") >= 0 or output.find("working tree clean") >= 0 or output.find(
                "nothing to commit") >= 0:
            return True
        return False

    def merge_code(self, now_branch, branch):
        self.checkout(branch)
        self.pull_origin(branch)
        self.check()
        execute_command("git merge %s" % now_branch)

    def add_tag(self, description):
        status, last_tag = self.get_last_tag()
        new_tag = self.generate_new_tag(last_tag)
        execute_command("git tag -a %s -m %s" % (new_tag, description))

    def check(self):
        if not self.is_clean():
            print "分支不干净，请检查"
            exit(0)

    def generate_new_tag(self, last_tag):
        if not last_tag:
            print "最新tag为空，请手动打tag"
            exit(0)
        author = self.get_author()
        if not author:
            print "请设置提交人"
            exit(0)
        # shejiben-7.3.4.4-201908281659-watson
        # utils-1.2.1-201908050927-watson
        tag_list = last_tag.split("-")
        tag_list[1] = self.get_version(tag_list[1])
        tag_list[2] = get_format_datetime()
        tag_list[3] = author

        new_tag = "-".join(tag_list)
        return new_tag

    def get_author(self):
        os.chdir(self.project_dir)
        status, author = execute_command("git config --global user.name")
        return author

    def push_to_test(self):
        now_branch = self.this_branch()
        self.check()
        self.checkout(self.test_branch)
        self.merge_code(now_branch, self.test_branch)
        self.check()
        print "merge finish..."
        self.push_origin(self.test_branch)
        print "push finish..."
        self.checkout(now_branch)


def version_sort(a_map):
    # a_map = {'sc': ['98', '106', '105', '101'], 'task': ['114', '125'], 'server': ['130', '', '129']}
    for module in a_map:
        version_list = []
        for version in a_map[module]:
            if version:
                version_list.append(int(version))

        version_list.sort(reverse=True)
        a_map[module] = [str(version) for version in version_list]
    return a_map


def mbps2mb(mbps):
    mb = mbps * 1000 / 8 / 1024
    return mb


def show_mbps2mb(mbps):
    return str(mbps2mb(mbps)) + 'MB/s'


def split_java_cmd():
    cmd = "/usr/local/jdk-1.8.0_11/bin/java -server -Xms512m -Xmx1024m -Djava.apps.version=14 -XX:+UseG1GC -XX:+HeapDumpOnOutOfMemoryError -XX:G1HeapRegionSize=4m -Djava.run.dir=/data/logs/java/run -Djava.logs.dir=/data/logs/java/logs -Djava.apps.prog=t8t-wkf-ctl -Dinstance.sequence=39e58 -jar /usr/local/release/t8t-wkf-ctl/sc-14/t8t-wkf-ctl-server-14-sc.jar"
    print cmd.split(" ")


def service_map():
    raw_data = {
        "adaptive_t8t-sys-dpt": "dsp-ps-gdm",
        "adaptive_com.canal": "t8t-dta-canal",
        "adaptive_com.integrated-package": "plt-teg-package",
        "adaptive_com.design": "t8t-plt-design",
        "adaptive_app.tit-configure": "t8t-sys-cfg",
        "adaptive_com.caller-dsgw": "t8t-plt-dsgw",
        "spring.platform.alias.crm.biddb": "com.crm",
        "adaptive_com.indent": "t8t-ind-order",
        "adaptive_t8t-dcp-scs": "t8t-dcp-ecs",
        "adaptive_com.call-inbound": "t8t-cal-inbound",
        "spring.platform.alias.crm.itemdb": "com.crm",
        "adaptive_t8t-scm-pom": "dsp-ps-gdm",
        "adaptive_t8t-scm-sup": "t8t-scm-sup",
        "adaptive_crm.msg": "crm-msg-center",
        "adaptive_com.data-pack": "t8t-dta-pack",
        "adaptive_com.codec": "t8t-plt-codec",
        "adaptive_com.shejiben": "t8t-cnt-shejiben",
        "spring.platform.alias.crm.svdb": "com.crm",
        "spring.platform.alias.crm.tuXin": "com.crm",
        "adaptive_dsp-ps-gdm": "dsp-ps-gdm",
        "adaptive_t8t-sys-icp": "t8t-sys-opl",
        "adaptive_com.payment": "t8t-plt-payment",
        "adaptive_com.financial-fund": "plt-fi-fund",
        "adaptive_com.image": "t8t-old-image",
        "adaptive_com.dc-item": "t8t-dc-item",
        "adaptive_t8t-wkf-bpm": "t8t-wkf-ctl",
        "adaptive_com.filter": "t8t-plt-filter",
        "adaptive_com.storage": "t8t-plt-storage",
        "adaptive_com.dw-foreman": "t8t-dw-foreman",
        "adaptive_com.weixin": "t8t-plt-weixin",
        "adaptive_dsp-prs-ctm": "t8t-sys-esm",
        "adaptive_com.finance": "t8t-plt-finance",
        "adaptive_com.dw-designer": "t8t-dw-designer",
        "adaptive_com.settlement": "t8t-plt-settlement",
        "adaptive_t8t-fi-fcm": "t8t-fi-fmd",
        "adaptive_com.dw-amat": "t8t-dw-amat",
        "adaptive_t8t-fi-fcs": "t8t-ps-smg",
        "adaptive_t8t-ps-odm": "t8t-scm-sup",
        "adaptive_com.ask": "t8t-plt-ask",
        "adaptive_dsp-ps-pmd": "dsp-ps-psm",
        "adaptive_com.comment": "t8t-met-owner",
        "adaptive_t8t-crm-qms": "t8t-crm-qms",
        "adaptive_com.diary": "t8t-plt-diary",
        "adaptive_com.dw-supervisor": "t8t-dw-supervisor",
        "adaptive_com.yz": "t8t-yz-background",
        "adaptive_com.logger": "t8t-plt-logger",
        "adaptive_app.bpmnserver": "t8t-bpm-workflow",
        "adaptive_com.estate": "t8t-plt-estate",
        "adaptive_com.autotask": "t8t-plt-autotask",
        "adaptive_com.complaints": "t8t-plt-complaints",
        "adaptive_t8t-scm-mrp": "t8t-scm-sup",
        "adaptive_app.welkin": "t8t-smt-welkin",
        "spring.platform.alias.crm.mainpage": "com.crm",
        "adaptive_caller.data": "t8t-dta-caller",
        "adaptive_app.dw-delivering": "app-dw-delivering",
        "adaptive_app.avalon": "t8t-smt-avalon",
        "spring.platform.alias.crm.configNode": "com.crm",
        "adaptive_t8t-fi-acp": "t8t-fi-acr",
        "adaptive_basic.monitor": "t8t-mon-zedis",
        "adaptive_crm.huodong": "t8t-crm-huodong",
        "adaptive_com.basicdata": "t8t-plt-basicdata",
        "adaptive_com.financial-pay": "plt-fi-pay",
        "spring.platform.alias.crm.bid": "com.crm",
        "spring.platform.alias.crm.sv": "com.crm",
        "adaptive_t8t-fi-tim": "t8t-fi-fip",
        "adaptive_com.passport": "t8t-plt-passport",
        "adaptive_t8t-dcp-dbm": "t8t-dcp-ppm",
        "adaptive_com.usercenter": "t8t-usr-center",
        "adaptive_app.supply-server": "t8t-sup-chain",
        "adaptive_com.dw-item": "t8t-dw-item",
        "spring.platform.alias.crm.utils": "com.crm",
        "adaptive_com.dw-foreman-m": "t8t-dwm-foreman",
        "adaptive_t8t-scm-rem": "t8t-scm-sup",
        "spring.platform.alias.crm.tools": "com.crm",
        "adaptive_t8t-ps-scg": "t8t-fi-fmd",
        "adaptive_com.caller-stat": "t8t-sta-caller",
        "adaptive_t8t-sys-exp": "t8t-scm-cfg",
        "adaptive_shejiben.ipic": "t8t-ipc-shejiben",
        "adaptive_com.oa": "t8t-plt-oa",
        "adaptive_com.crm": "t8t-crm-background",
        "adaptive_t8t-sys-sti": "t8t-sys-pms",
        "adaptive_com.to8to.thrift.is.imageservice": "plt-thr-image",
        "adaptive_com.dw-loan": "t8t-dw-loan",
        "adaptive_com.decocom": "t8t-plt-decocom",
        "adaptive_com.financial-remit": "plt-fi-remit",
        "adaptive_t8t-app-pam": "t8t-sys-faq",
        "adaptive_com.oper-config": "t8t-ope-config",
        "adaptive_com.crm-supervisor": "t8t-crm-supervisor",
        "adaptive_com.pmat": "t8t-crm-pmat",
        "adaptive_com.crm-quality": "t8t-crm-quality",
        "adaptive_com.to8to.thrift.is.ImageService": "plt-thr-image",
        "adaptive_com.supply": "t8t-plt-supply",
        "adaptive_com.redis": "t8t-plt-redis",
        "adaptive_com.clickstream": "t8t-plt-clickstream",
        "spring.platform.alias.crm.query": "com.crm",
        "adaptive_com.tumall": "t8t-shp-tumall",
        "adaptive_com.permission": "t8t-plt-permission",
        "adaptive_com.yugong": "t8t-plt-yugong",
        "adaptive_t8t-fi-ina": "t8t-fi-acr",
        "adaptive_com.cache-cleaner": "t8t-plt-cleaner",
        "adaptive_com.search": "t8t-plt-search",
        "adaptive_com.financial-account": "plt-fi-account",
        "adaptive_t8t-dcp-ecs": "t8t-dcp-ecs",
        "spring.platform.alias.crm.item": "com.crm",
        "adaptive_t8t-fi-rvm": "t8t-fi-pvm",
        "adaptive_t8t-scm-fhc": "dsp-ps-gdm",
        "adaptive_com.dw-advisor": "t8t-dw-advisor",
        "adaptive_com.crm.data": "t8t-crm-data",
        "adaptive_t8t-crm-qsm": "t8t-crm-qms",
        "spring.platform.alias.crm.sms": "com.crm",
        "adaptive_dsp-prs-pqm": "dsp-prs-fdm",
        "adaptive_t8t-wkf-dat": "t8t-wkf-ctl",
        "adaptive_shejiben.imall": "t8t-ima-shejiben",
        "adaptive_com-bpmn": "t8t-plt-bpmn",
        "adaptive_t8t-sys-cfg": "t8t-scm-cfg",
        "adaptive_t8t-scm-ldm": "t8t-scm-sup",
        "adaptive_dsp-prs-ass": "dsp-prs-hmm"
    }

    a_map = {}
    for value in raw_data:
        key = raw_data[value]
        service = value.replace("adaptive_", "")
        if key in a_map:
            a_map[key].append(service)
        else:
            a_map[key] = [key, service]
    print a_map



if __name__ == '__main__':
    service_map()
    # split_java_cmd()
    # a_map = {'sc': ['98', '106', '105', '101'], 'task': ['114', '125'], 'server': ['130', '', '129']}
    # print version_sort(a_map)
    # split_str()
    # test_input()

    # 3.5MB/s
    # print 98 / mbps2mb(29.13)
