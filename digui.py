import time

class C:
    def fun(self):
        # 获取当前的时间，形成 小时：分钟：秒  的字符串
        print(time.strftime("%X"), end=' ')

    def fileOpen(self):
        t = time.strftime("%X")
        file = open('File_test/Hello.txt', mode='a+', encoding='utf-8')
        file.write(t + '\n')
        file.flush()
        file.close()

c = C()
c.fun()
c.fileOpen()

