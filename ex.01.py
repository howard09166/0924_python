t = int(input('秒'))
print(f"{t//3600}:{t%3600//60:02}:{t%60:02}")

all = int(input('全班'))
x = int(input('繳交'))
print(f"{x/all*100:.1f}%",'未繳交=',all-x)

fir = int(input('第一次段考成績'))
sec = int(input('第二次段考成績'))
thi = int(input('第三次段考成績'))
print(f"平均成績: {(fir + sec + thi) / 3:.1f}")
