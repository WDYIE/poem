import requests
import json



access_token = "24.12fb56af434f077bbbfb9d7883aa4088.2592000.1572939273.282335-17330434"
url = "https://aip.baidubce.com/rpc/2.0/creation/v1/poem?access_token="+access_token

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Content-Type":"application/json"}

def getPeom(text,index):
    dict_data = {'text': text, 'index': index}
    bodystr = json.dumps(dict_data)
    response = requests.post(url=url, headers=headers, data=bodystr)
    str = response.content.decode('utf-8')
    return str
def combine(words1,words2):
    res = []
    for s1 in words1:
        for s2 in words2:
            res.append(s1+s2)
    return res

def savedict(data_dict):
    csv_path = "data"+ ".csv"
    print(csv_path)
    with open(csv_path, 'w') as csv_file:
        for temp_list in data_dict:
            line_data = temp_list+','
            line_data += ",".join(str(i) for i in data_dict[temp_list])
            line_data += "\n"
            csv_file.write(line_data)
def readto_dict():
    birth_data = {}
    csv_path = "data" + ".csv"
    with open(csv_path) as csvfile:
        for row in csvfile.readlines():  # 将csv 文件中的数据保存到birth_data中
            strs = row.split(',')
            key = strs[0]
            strs = strs[1:]
            birth_data[key]=strs
    return birth_data


print(getPeom("西湖龙井",index=0))


allPeom={}
allWord=["美丽",'可爱']
allTitle = ['龙井','茉莉']

res = combine(allWord,allTitle)
for text in res:
    for i in range(10):
       content = getPeom(text,i)
       if text in allPeom:
           arr = allPeom[text]
           arr.append(content)
       else:
           allPeom[text]=[]
           arr = allPeom[text]
           arr.append(content)

savedict(allPeom)
resn =readto_dict()
print(resn)

