attendence = []

with open('d:\\attendence.csv') as file:
    for line in file:
        attendence.append(line)




def prepare_report(lst_element):
	#Step:1 -- You will recieve element in splitted form ---> [ABDUL HANNAN,F2018065041,P,P,P,P,P,P,P,P,P,P,P,P,P,P] 
	#Step:2 --  You will take two element through slice and get first two element [ABDUL HANNAN,F2018065041] and also reverse it here
	#Step:3 --  you will convert this Name, and ID into dictionary {ID:Name}
	
	#Step:4 -- Then you will take slice of lst_element such that it will consists of attedence information --- result---> [P,P,P,P,P,P,P,P,P,P,P,P,P,P]
	
	#Step:5 -- The you will pass this above slice to the following function, then this function will return a dictionary with attendence count, for example, for the above slice it will return the dictionary {"Present":14}
	
    dic_2 = present_absent_report( ... )

	#Step: 6 --- You will process the two dictionaries into the following final result as follows,
	#dic_1 --> {'F2016065051': ['Muhammad Adnan Riaz', 'Present : 5/7-->(71.43)%', 'Absent : 2/7-->(28.57)%']}
    
    return dic_1



def present_absent_report(attendance_lst):
   #your code here


for i in attendence:
    i = i.strip('\n\r')
    print(prepare_report(i.split(',')))


