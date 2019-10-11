name = "zzw"
print("我的名字是%s,请关照！" % name)

scale=0.25
print("数据比例%.2f%%" %(scale*100))
print("数据比例{:.2f}%".format(scale * 100))
print("我的名字是{},比例是{:.2f}%".format(name, scale*100))
print(f"我的名字是{name:s},数据比例是{scale*100:.2f}%")
# 最简捷的应该是最后一种方式
id_number=123456
print(f'我的身份证号码是：{id_number}')
print(f'我的身份证号码是：{id_number:07d}')

a_list=['a', 'b', 'c']
print(f'列表如下：{a_list}')
print(f'列表如下：{a_list[0]},{a_list[1]}')

b_str='1 2 3 4 5 6'
b_list=b_str.split(' ')
print(b_list)
for i in range(5):
    print(f'我排在第{i}位')
    print(f'我的前面是第{i-1}位')
    print(f'我的后面是第{i+1}位')
