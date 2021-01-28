import yagmail
for i in range(10):
    yag = yagmail.SMTP(user="an980604@163.com",host="smtp.163.com",password="JQZKROSEURZWCDUX")
    con = ["a.txt"]
    yag.send("1736221450@qq.com","测试","社会我飞哥，人狠话还多！")




