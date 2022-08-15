total=0
inputfee=0
allfee=[]
while (inputfee!=-1):
    inputfee=int((input('請輸入電費(輸入-1離開):')))
    if inputfee==-1:
        print('輸入結束，共輸入%d個數'%(len(allfee)))
    else:
         allfee.append(inputfee)
         total+=inputfee  
print('電費最大值為%d'%(max(allfee)))         
print('電費最小值為%d'%(min(allfee)))
print('電費總和為%d'%(sum(allfee)))
print('電費由大到小排序為',sorted(allfee,reverse=True))
        
