import array as arr

server_license = input("Enter the 10 digit licence: ");
local_license = ['','','','','','','','','',''];
num = int(len(server_license))
print (len)

for x in range(0,10):
    if (x % 2) == 0:
        local_license[x] = chr((ord(server_license[int(x)])-1));
    else:
        local_license[x] = chr((ord(server_license[int(x)])+1));

res = "";
for val in range(0,10): 
    res = res + local_license[val];
    
print ((res));
