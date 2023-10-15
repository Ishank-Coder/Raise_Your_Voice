def getlist(request,db):
    
    ref = db.reference('ConvenerRelatedGrievance/Exam')
    data = ref.get()
  
    news = []
    pend=[]
    close = []
    for key, value in data.items():
        if 'status' in value.get('StudentGrievance', {}):
            if value['StudentGrievance']['status'] == 'new':
                news.append(value['StudentGrievance']['name'])
            elif value['StudentGrievance']['status'] == 'pending':
                pend.append(value['StudentGrievance']['name'])
            else:
                close.append(value['StudentGrievance']['name'])

    return(news,pend,close)
    # def search_value(node, target_value, parent_key=None):
    #     if isinstance(node, dict):
    #         for key, value in node.items():
    #             if value == target_value:
    #                 return (key, parent_key)
    #             elif isinstance(value, dict):
    #                 result = search_value(value, target_value, key)
    #                 if result:
    #                     return result
    # res = search_value(data, "new")
    
    # if res:
    #     node_key, parent_key = res
    #     print("Node key:", node_key)
    #     print("Parent key:", parent_key)
    # else:
    #     print("Node not found.")
 