import os
import time
import download
def remove():
    # Inspection Center
    print('检查中心正在检查')
    time.sleep(0.5)
    print('检查.travis.yml是否存在')
    time.sleep(0.5)
    if os.path.exists('.travis.yml'): # 如果文件存在
        # 删除文件，可使用以下两种方法。
        print('检查到.travis.yml')
        time.sleep(0.5)
        print('正在处理')
        time.sleep(0.5)
        os.remove('.travis.yml') # 则删除
        time.sleep(0.5)
        print('处理完成')
        #os.unlink(my_file)
    else:
        print('no such file .travis.yml')
def language():
    languages = 'language.yml'
    open(5,wb)

