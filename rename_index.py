# -*- coding: utf-8 -*-
import os

"""
"t8t_sjb_category",
"t8t_sjb_category_image",
"t8t_sjb_collection",
"t8t_sjb_collection_comment",
"t8t_sjb_collection_image",
"t8t_sjb_comment",
"t8t_sjb_designer",
"t8t_sjb_question",
"t8t_sjb_question_answer_tag",
"t8t_sjb_tag",

"""
if __name__ == '__main__':
    index_map = {
        "t8t_sjb_categories": "t8t_sjb_category",
        "t8t_sjb_collcomment": "t8t_sjb_collection_comment",
        "t8t_sjb_collections": "t8t_sjb_collection",
        "t8t_sjb_collimages": "t8t_sjb_collection_image",
        "t8t_sjb_comquest": "t8t_sjb_comment_question",
        "t8t_sjb_designinfo": "t8t_sjb_designer",
        "t8t_sjb_imagesinfocat": "t8t_sjb_category_image",
        "t8t_sjb_tags": "t8t_sjb_tag",
        "t8t_sjb_wendatags": "t8t_sjb_question_answer_tag",
    }
    # index_map = {
    #     "t8t_sjb_collimages": "t8t_sjb_collection_image",
    #     "t8t_sjb_comquest": "t8t_sjb_comment_question",
    #     "t8t_sjb_imagesinfocat": "t8t_sjb_category_image",
    #     "t8t_sjb_tags": "t8t_sjb_tag",
    #     "t8t_sjb_wendatags": "t8t_sjb_question_answer_tag",
    # }

    for index in index_map:
        dest = index_map[index]
        # cmd = "curl -XPOST 'http://192.168.1.118:9200/_reindex?pretty' -H 'Content-Type: application/json' -d'{\"source\":{\"index\":\"%s\"},\"dest\":{\"index\":\"%s\"}}'" % (
        #     index, dest)
        cmd = "curl -XDELETE 'http://192.168.1.118:9200/%s?pretty'" % index
        print cmd
        os.system(cmd)

    pass
