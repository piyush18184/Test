# 1

import pandas as pd

mat = pd.read_excel (r'C:\Users\Piyush\Downloads\Python_Assignment.xlsx', sheet_name='Maths')
mat = mat.rename(columns = {'Roll No':'Roll No', 'Class':'Class', 'Theory Marks':'Maths_Theory', 'Numerical Marks':'Maths_Numerical', 'Practical Marks':'Maths_Practical'})
phy = pd.read_excel (r'C:\Users\Piyush\Downloads\Python_Assignment.xlsx', sheet_name='Physics')
phy = phy.rename(columns = {'Roll No':'Roll No', 'Class':'Class', 'Theory Marks':'Physics_Theory', 'Numerical Marks':'Physics_Numerical', 'Practical Marks':'Physics_Practical'})
hin = pd.read_excel (r'C:\Users\Piyush\Downloads\Python_Assignment.xlsx', sheet_name='Hindi')
hin = hin.rename(columns = {'Roll No':'Roll No', 'Class':'Class', 'Marks':'Hindi_Marks'})
eco = pd.read_excel (r'C:\Users\Piyush\Downloads\Python_Assignment.xlsx', sheet_name='Economics')
eco = eco.rename(columns = {'Roll No':'Roll No', 'Class':'Class', 'Theory Marks':'Economics_Theory', 'Numerical Marks':'Economics_Numerical'})
mus = pd.read_excel (r'C:\Users\Piyush\Downloads\Python_Assignment.xlsx', sheet_name='Music')
mus = mus.rename(columns = {'Roll No':'Roll No', 'Class':'Class', 'Theory Marks':'Music_Theory', 'Practical Marks':'Music_Practical'})

f3 = mat[["Roll No", "Class", "Maths_Theory", "Maths_Numerical", "Maths_Practical"]].merge(phy[["Roll No", "Class", "Physics_Theory", "Physics_Numerical", "Physics_Practical"]], on = ["Roll No", "Class"], how = "outer").merge(hin[["Roll No", "Class", "Hindi_Marks"]], on = ["Roll No", "Class"], how = "outer").merge(mus[["Roll No", "Class", "Music_Theory", "Music_Practical"]], on = ["Roll No", "Class"], how = "outer").merge(eco[["Roll No", "Class", "Economics_Theory", "Economics_Numerical"]], on = ["Roll No", "Class"], how = "outer")

#f3.rename(columns = {'Roll No':'Roll No', 'Class':'Class', 'Theory Marks_x':'Maths_Theory', 'Numerical Marks_x':'Maths_Numerical', 'Practical Marks_x':'Maths_Practical', 'Theory Marks_y':'Physics_Theory', 'Numerical Marks_y':'Physics_Numerical', 'Practical Marks_y':'Physics Practical', 'Marks':'Hindi_Marks', 'Theory Marks_x':'Music_Theory', 'Practical Marks':'Music_Practical', 'Theory Marks_y':'Economics_Theory', 'Numerical Marks':'Economics Numerical'}, inplace = True)

f3["Maths %"] = (f3["Maths_Theory"]+f3["Maths_Numerical"]+f3["Maths_Practical"])/3
f3["Physics %"] = (f3["Physics_Theory"]+f3["Physics_Numerical"]+f3["Physics_Practical"])/3
f3["Hindi %"] = f3["Hindi_Marks"]
f3["Economics %"] = (f3["Economics_Theory"]+f3["Economics_Numerical"])/2
f3["Music %"] = (f3["Music_Theory"]+f3["Music_Practical"])/2

res = f3[["Roll No", "Class", "Maths %", "Physics %", "Hindi %", "Economics %", "Music %"]]


# 2.a

tot_enroll = len(res.index)

# 2.b

all_sub = len(res[(res["Maths %"]>=0) & (res["Physics %"]>=0) & (res["Hindi %"]>=0) & (res["Economics %"]>=0) & (res["Music %"]>=0)].index)

# 2.c

temp = [len(res[res["Maths %"]>=0].index), len(res[res["Physics %"]>=0].index), len(res[res["Hindi %"]>=0].index), len(res[res["Economics %"]>=0].index), len(res[res["Music %"]>=0].index)]
sub = ['Maths', 'Physics', 'Hindi', 'Economics', 'Music']
max_stu_dict = dict(zip(sub, temp))
max_stu = max(max_stu_dict, key=max_stu_dict.get)


# 2.e

maximum_list = list()
for col in res.columns:
    maximum_list.append(res[col].mean())
sub = ['Maths', 'Physics', 'Hindi', 'Economics', 'Music']

avg_dict = dict(zip(sub, maximum_list[2:]))
high_avg_sub = max(avg_dict, key=avg_dict.get)
