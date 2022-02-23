
# managermenu=Menu(mymenu,tearoff=0)
# managermenu.add_command(label='pakisatan')
# managermenu.add_command(label='pakisatan')
# managermenu.add_command(label='pakisatan')


# # 2nd menu
# # view employes 
# viewEMployee=Menu(mymenu,tearoff=0)
# viewEMployee.add_command(label='attandence', command=submit_Btn1)
# viewEMployee.add_cascade(label='manager', menu=managermenu)
# viewEMployee.add_command(label='employee', command=submit_Btn1)

# # main menu
# # add  cascade
# EmployeeMenu=Menu(mymenu,tearoff=0)
# EmployeeMenu.add_command(label="add employee",command=submit_Btn)
# EmployeeMenu.add_cascade(label="view employee",menu=viewEMployee)
# EmployeeMenu.add_command(label="delete employee",command=submit_Btn)

# # ##########################################################
# mymenu.add_cascade(label='employee',menu=EmployeeMenu)