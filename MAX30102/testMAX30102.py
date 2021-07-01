import max30102
import hrcalc

m = max30102.MAX30102()

hr2 = 0
sp2 = 0

while True:
    red, ir = m.read_sequential()
    
    hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)

    print("hr detected:",hrb)
    print("sp detected:",spb)
    
    if(hrb == True and hr != -999):
        hr2 = int(hr)
        print("Heart Rate : ",hr2)
    if(spb == True and sp != -999):
        sp2 = int(sp)
        print("SPO2       : ",sp2)
