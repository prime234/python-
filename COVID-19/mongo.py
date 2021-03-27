import pymongo
class covid:
    def __init__(self,data ,name, imageUrl, categories, today_confirm,today_suspect,today_heal,today_dead,today_storeConfirm,total_confirm,total_suspect,total_heal,total_dead,total_severe):
        self.data= data
        self.name = name
        self.id = id
        self.lastUpdateTime = lastUpdateTime
        self.today_confirm = today_confirm
        self.today_suspect= today_suspect
        self.today_heal = today_heal
        self.today_dead = today_dead
        self.today_storeConfirm = today_storeConfirm
        self.total_confirm = total_confirm
        self.total_suspect = total_suspect
        self.total_heal= total_heal
        self.total_dead = total_dead
        self.total_severe= total_severe

    def __str__(self) -> str:
        return self.data +'^' + self.name +'^' + self.id +'^' + self.lastUpdateTime +'^' + self.today_confirm


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["COVID-19"]
    today_province_2020_12_04 = mydb['today_province_2020_12_04']
    with open('today_province_2020_12_04.csv', 'r',encoding='UTF-8') as f:
        item = f.readline()
        while item:
            attr = item.split('^')
            today_province_2020_12_04 = (int(attr[0]), attr[1].strip(), attr[4].strip(), attr[5].strip(), attr[6].strip())
            today_province_2020_12_04.insert_one(today_province_2020_12_04.__dict__)
            item = f.readline()

