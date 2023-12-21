import time 
for index in range(1,100):
    time.sleep(0.5)
    if index % 13 ==0:
        print(f"this divisible number =",{index})