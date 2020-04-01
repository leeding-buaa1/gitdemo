# TempConvert.py
val = input("请输入带温度表示符号的温度值(例如: 32C): ")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("转换后的温度为: %.2fF"%f)