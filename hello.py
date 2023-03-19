# class Team:
#     def __init__(self,te,ta,tr):
#         self.te = te
#         self.ta = ta
#         self.tr = tr
# class Tournament(Team):
#     def __init__(self , lt , di):
#         self.lt = lt
#         self.di = di
#     def hart(self):
#        ft={}
#        for i in self.lt:
#            if  not i.ta in ft:
#                ft[i.ta] =1
#            else:
#                ft[i.ta]+=1
#        return(ft)
# def happ(jt,np):
#     dx={}
#     for i in jt:
#         if i.di['Time'] >= np:
#             for kp in i.lt:
#                 dx[kp.tr]=kp.te
#
#     dx=dict(sorted(dx.items(),key=lambda items:items[1]))
#     return(dx.keys())
#
# n=int(input())
# js=[]
# for i in range(n):
#     m = int(input())
#     l=[]
#     for j in range(m):
#         tR = int(input())
#         tC = input()
#         tN = input()
#         l.append(Team(tR , tC , tN))
#     dic = {}
#     dic["Name"] = input()
#     dic["Host"] = input()
#     dic["Edition"] = int(input())
#     dic["year"] = int(input())
#     dic["participants"] = int(input())
#     dic["Time"] = int(input())
#     js.append(Tournament(l , dic))

# diff = cv2.blur(diff, (5, 5))
# p = js[0].hart()
# for i,j in p.items():
#     print(i,j,sep="-")
# for i in happ(js,int(input())):
#     print(i)
def kst(lt,pl):
    count =0
    for i in lt:
        if i%pl == 0:
            count=count+1
    return count



n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(kst (l,  int(input())   ))