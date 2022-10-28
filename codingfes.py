# 복권
num=list(map(int,input().split(',')));
nnum=sorted(num);
rotto=nnum[0]+nnum[1]+nnum[3]+nnum[2];
print(rotto)
