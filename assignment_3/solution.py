attendence = []

with open('assignment_3/attendence.csv') as file:
    for line in file:
        attendence.append(line)

def prepare_report(lst_element):
    first_two = lst_element[:2][::-1]
    dic_1 = dict([first_two])
    attandance_information = lst_element[2:]
	
    final_list = [first_two[-1]]
    dic_2 = present_absent_report(attandance_information)
    total_attendance_days = sum(dic_2.values())
    if dic_2['Present'] > 0:
        present_string = f"Present: {dic_2['Present']}/{total_attendance_days}-->({round(dic_2['Present']/total_attendance_days*100, 2)})%"
        final_list.append(present_string)
    
    if dic_2['Absent'] > 0:
        absent_string = f"Absent: {dic_2['Absent']}/{total_attendance_days}-->({round(dic_2['Absent']/total_attendance_days*100, 2)})%"
        final_list.append(absent_string)
    
    dic_1[first_two[0]] = final_list

    return dic_1

def present_absent_report(attendance_lst):
    attendance_dict = {
        "Present": attendance_lst.count('P'),
        "Absent": attendance_lst.count('A')
    }
    return attendance_dict

for i in attendence:
    i = i.strip('\n\r')
    print(prepare_report(i.split(',')))