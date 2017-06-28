#encoding=utf-8
import json

def dealAllProds(allProds,pid,minNum):
    if allProds == None: return
    prodArr = []
    for res in allProds:
        id,prods = res
        print "id:",id
        print "prods:",prods
        prodsJson = json.loads(prods)
        print "prodsJson:",prodsJson
        num = 0
        if prodsJson.has_key(pid):
            num = prodsJson[pid]
            print "num",num
        else:
            print pid,"不存在"
        if num>=minNum:
            ujson = {"id":id,"pid":pid,"num":num}
            prodArr.append(ujson)

    return prodArr


if __name__ == "__main__":
    print "main"
