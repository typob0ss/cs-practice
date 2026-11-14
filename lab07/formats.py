def csv_to_records(text):
    data = []
    head, *lines = text.split("\n")
    head = head.split(",")
    for line in lines:
        line = line.split(",")
        record = {}
        for i in range(len(line)):
            record[head[i]] = line [i]
        data.append(record)
    return data
    return head, lines    
print(csv_to_records("id,город\n1,Азов\n2,Шахты"))
# [{"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}]

# parse_settings(["# отчёт", "title: Отчёт за март", "decimals: 1", "active: true",
#                 "columns:", "  - город", "  - цена"])
# # {"title": "Отчёт за март", "decimals": 1, "active": True, "columns": ["город", "цена"]}

# merge_by_key([{"id": "1", "город": "Азов"}], {"1": {"регион": "Ростовская"}}, "id")
# # [{"регион": "Ростовская", "id": "1", "город": "Азов"}]
