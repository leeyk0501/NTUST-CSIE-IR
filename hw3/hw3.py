while True:
    try:
        query_count = int(input())
        ans_doc_list = []
        rele_doc_list = []
        for i in range(query_count):
            ans_doc_str = input()
            rele_doc_str = input()
            ans_doc_list.append(ans_doc_str.split())
            rele_doc_list.append(rele_doc_str.split())
        map_value_list = []
        for i in range(len(ans_doc_list)):
            precision_list = []
            match = 0
            for j in range(len(ans_doc_list[i])):
                if ans_doc_list[i][j] in rele_doc_list[i]:
                    match += 1
                    precision_list.append(round(match / (j + 1.), 4))
            map_value_list.append(round(sum(precision_list) / len(rele_doc_list[i]), 4))
        map_ans = round(sum(map_value_list) / len(map_value_list), 4)
        print(map_ans)
    except:
        break
