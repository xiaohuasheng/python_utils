# -*- coding: utf-8 -*-
import json

import requests


def get_data(index, start=0, size=100):
    headers = {
        'Content-Type': 'application/json',
    }
    data = '''
    {
  "from" : %d,
  "size" : %d,
  "query" : {
    "terms" : {
      "category" : [
        15377426,
        15377425,
        15377424,
        15377423,
        153226,
        153223,
        153220,
        153215,
        153234,
        153233,
        153232,
        153230,
        153763,
        153227,
        153213,
        150733,
        153225,
        153224,
        153218,
        153210
      ],
      "boost" : 1.0
    }
  },
  "sort" : [
    {
      "rank" : {
        "order" : "desc"
      }
    }
  ]
}
    ''' % (start, size)
    # data = '{"from":%d,"size":%d,"query":{"filtered":{"filter":{"bool":{"must":[{"range":{"case_num":{"from":0,"to":null,"include_lower":true,"include_upper":false}}}],"_cache":true}}}}}' % (
    #     start, size)
    response = requests.post('http://192.168.2.57:9200/shejiben_ipic_dev20190905/%s/_search' % index, headers=headers,
                             data=data)
    print response.status_code
    data = response.json()
    return data['hits']['hits']


def set_data(index, data_list):
    headers = {
        'Content-Type': 'application/json',
    }

    params = (
    )

    proxies = {"http": "http://192.168.3.97:3128"}
    for item in data_list:
        data = json.dumps(item['_source'])
        # data = '{"id":260683,"goodlevel":0,"min_price":0,"city":"\u6FEE\u9633","type":"1","yuyue_nums":0,"workyears":0,"cxt_num":0,"apply_status":1,"shen":"\u6CB3\u5357","mainfield":0,"otherfield":"","truename":"ling","cxt_year":0,"max_price":0,"ident":0,"regdate":1293582941,"uid":null,"pic_num":null,"case_num":null,"case_show_num":null,"elite_num":null,"sign_num":null,"appraise_num":null,"user_score":null,"space_tags":"","collect_num":null,"attention_num":null,"extensionnum":null,"is_show":null,"otype":null,"odate":null,"name_rz":null,"spaceStr":"","name_rz_status":0}'
        # response = requests.post('http://192.168.1.118:9200/t8t_sjb_designer/doc/', headers=headers, data=data)
        response = requests.post('http://192.168.1.118:9200/%s/doc/' % index, headers=headers, params=params,
                                 data=data, proxies=proxies)
        # break


if __name__ == '__main__':
    page = 1
    size = 100
    index_type = "categories"
    index_type = "imagesinfocat"
    target_index = "t8t_sjb_category"
    target_index = "t8t_sjb_category_image"
    while True:
        start = (page - 1) * size
        data_list = get_data(index_type, start, size)
        if not data_list:
            break
        set_data(target_index, data_list)
        page = page + 1
    pass
