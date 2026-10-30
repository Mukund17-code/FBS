no = int(input('Enter three digit number :'))

fn = no % 10
no = no // 10

sn = no % 10
no = no // 10

th = no % 10
no = no //10

sum = fn + sn + th
print(f'sum number =',fn,'+',sn,'+',th,'=',sum)
