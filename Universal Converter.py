#!/ProgramData/Anaconda3/envs/ Python
# -*- coding:utf-8 -*-
# Universal Converter.py
# author: cqs

is_add = True
while(is_add):
    print('欢迎使用万能单位转换器'.center(30,'*'))
    #选择转换类型
    menu = {
        'T':'温度转换',
        'L':'长度转换',
        'C':'货币转换'
    }
    for k, v in menu.items():
        print(k, v)
    choose = input('请输入转换类型：')
    
    #摄氏温度与华氏温度互相转换
    if choose == 'T':
        temp = input('请输入温度（示例：1C或1F）：')
        t_type = temp[-1]
        temp = float(temp.strip('C').strip('F'))
        if t_type == 'C':
            Tf = ( 9 / 5 ) * temp +32
            Tf = float(str(Tf)[:5])
            print(f'你输入的摄氏温度为：{temp}C，华氏温度为：{Tf}F')
        else:
            Cf = ( 5 / 9 ) * ( temp - 32 )
            Cf = float(str(Cf)[:5])
            print(f'你输入的华氏温度为：{temp}F，摄氏温度为：{Cf}C')
        
        # 选择是否继续
        is_add = input('继续转换(y/s):').strip() == 'y'
            
    #中国长度单位丈与美国长度单位米互相装换
    elif choose == 'L':
        temp = input('请输入长度（示例：1Z(丈)或1M(米)）：')
        t_type = temp[-1]
        temp = float(temp.strip('Z').strip('M'))
        if t_type == 'Z':
            Mf = ( 10 / 3 ) * temp
            print(f'你输入的长度为：{temp}丈，转换后的长度为：{Mf}米')
        else:
            Zf = ( 3 / 10 ) * temp
            print(f'你输入的长度为：{temp}米，转换后的长度为：{Zf}丈')
        
        # 选择是否继续
        is_add = input('继续转换(y/s):').strip() == 'y'
            
    #人民币与美元互相装换
    elif choose == 'C':
        temp = input('请输入金额（示例：1Y(人民币)或1U(美元)）：')
        t_type = temp[-1]
        temp = float(temp.strip('Y').strip('U'))
        if t_type == 'Y':
            Uf = 6.7854 * temp
            print(f'你输入的人民币金额为：{temp}元，转换后的美元为：{Uf}美元')
        else:
            Yf = 0.1474 * temp
            print(f'你输入的美元为：{temp}美米，转换后的人民币为：{Yf}元')
            
        # 选择是否继续
        is_add = input('继续转换(y/s):').strip() == 'y'
    else:
        print('你输入错误，请重新输入：')
        
        # 选择是否继续
        is_add = input('继续转换(y/s):').strip() == 'y'