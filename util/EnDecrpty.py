# 加密
def encrypt(srcStr, password='6249350187'):
    # 将字符串转换成字节数组
    data = bytearray(srcStr.encode('utf-8'))
    # 把每个字节转换成数字字符串
    strList = [str(byte) for byte in data]
    # 给每个数字字符串前面加一个长度位
    strList = [str(len(s)) + s for s in strList]
    # 进行数字替换
    for index0 in range(len(strList)):
        tempStr = ""
        for index in range(len(strList[index0])):
            tempStr += password[int(strList[index0][index])]
        strList[index0] = tempStr
    return "".join(strList)


# 解密
def decrypt(srcStr, password='6249350187'):
    # 数字替换还原
    tempStr = ""
    for index in range(len(srcStr)):
        tempStr += str(password.find(srcStr[index]))
    # 去掉长度位，还原成字典
    index = 0
    strList = []
    while True:
        # 取长度位
        length = int(tempStr[index])
        # 取数字字符串
        s = tempStr[index + 1:index + 1 + length]
        # 加入到列表中
        strList.append(s)
        # 增加偏移量
        index += 1 + length
        # 退出条件
        if index >= len(tempStr):
            break
    data = bytearray(len(strList))
    for i in range(len(data)):
        data[i] = int(strList[i])
    return data.decode('utf-8')


if __name__ == '__main__':
    # ret = encrypt('id:123,time:7200,key:123456789987654321', '6249350187')
    # print('密文:', ret)

    ret = "924949392249223922292469242493458494493924947449392259262922392289262922347449345849447449347792669226435477922643092269262926192224779268922292219266430477922647449343347449392249222922392204744934584944744934374514384544384744934334744939221922192659266474493458494474493455453477478459438471454435451926492664504354524594569262435451451926445443547145547847845945145945147843845547847449343347449347192689220926292234199266474493458494474493438474493433474493477926592249263926292234744934584944744934719221922092224744934334744939226926292209227922292239261474493458494474493922792254744934334744939227922543592244719220926347449345849447449343192664719263926092279221926347449343347449392249223922292209222477922292684744934584944744939228926792629225922547449392454934334944939263922092209224922549345849492644719268922592624334944939264471926592684754779222922192269220493458494438433494493922392629269926592229226493458494493493433494493471922692229226924292679222922192254934584944934934334944939225922292219223477926249345849449349343349449347792639262477926147547792229221922692204934584944384334944939268471922592204759225922047192209221922549345849449349343349449392684719225922047592209265926792624934584944934939245"

    ret = decrypt(ret, '6249350187')
    print('原文:', ret)