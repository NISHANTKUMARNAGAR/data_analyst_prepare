data={100:'ravi',101:'vijay',102:'rahul'};
print(data);
names={};  #empty dictionary
names[1]='Ravi';
names[2]='Manoj';
names['nm']='hari';
names[4]='om';
print(names);
print(names[2]);

#functions
data={100:'ravi',101:'vijay',102:'rahul'};
data1={103:'sanjay'};
print(data1[103])
print(len(data));
print(str(data));
print(data.keys());
print(data.values());
print(data.items());
data.update(data1);
print(data);
data1.clear();
print(data1);
data1=data.copy();
print(data1);
print(100 in data);
print(109 in data);
print(data.get(101));

'''dictionary multiple value in a list for a key input example
in pdf of dictionary input in study/python 
below is  code for solving the question'''
'''input way is 
2
naman 2 5 6
seema 4 3 6'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

#dictionary input 1 value for a key
people={}
for i in range(2):
    name,city=input().split()
    people[name]=city
print(people)

#to count characters get() method
s = "hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)