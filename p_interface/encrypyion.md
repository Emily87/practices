
#对字典按键排序，用元组列表的形式返回
d={"ok":1,"no":2}
d1 = sorted(d.items(), key=lambda d:d[0],reverse = False) #[('no', 2), ('ok', 1)] 
#对字典按值排序，用元组列表的形式返回
# d2 = sorted(d.items(), key=lambda d:d[1],reverse = True) #[('ok', 1), ('no', 2)]

#sorted(dict.items(), key=lambda x:x[0], reverse=True)
# key= lambda x:x[0],x[0]表示按键，x[1]表示按值。
# reverse#默认是False，升序排列。当值为True时是降序排列。
# 返回的是一个列表，列表中是排列后的元组