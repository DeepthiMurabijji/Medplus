import random 
'''
a=input("enter the string: ")
p=('.',',','!','?',';')
c=0
new=" "

for i in a.split():
	if (len(i)>3):
		if(i.endswith(p)):
			w1=i[1:-2]
			w1=random.sample(w1,len(w1))
			#print(w1)
			w1.insert(0,i[0])
			w1.append(i[-2])
			w1.append(i[-1])
			new=new+''.join(w1)+''

		else:
			w1=i[1:-1]
			#print(w1)
			w1=random.sample(w1,len(w1))
			w1.insert(0,i[0])
			w1.append(i[-1])
			new=new+''.join(w1)+" "
	else: 
		new=new+i+" " 	
			
print(new)			
'''


def main():
    word = '"surprising",...'                      #input("Please enter a word: ")
    print(scramble(word)) 

def scramble(word):
    char1 = random.randint(1, len(word)-2)
    char2 = random.randint(1, len(word)-2)
    while char1 == char2:
        char2 = random.randint(1, len(word)-2)
    newWord = ""

    for i in range(len(word)):
        if i == char1:
            newWord = newWord + word[char2]
        elif i == char2:
            newWord = newWord + word[char1]

        else:

            newWord = newWord + word[i]

    return newWord

main()			
			
			
			
			
			
	

'''
def scramble(word):
	word=list(word)
	shuffle(word)
	return ''.join(word)
	
word=input("enter a word: ")
res=[scramble(word) ]
print(str(res))


string='string'
l=list(string)
shuffle(l)
string=''.join(l)
print(string)
'''
