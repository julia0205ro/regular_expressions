import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def full_names(my_list):
    new_employee_list = []
    for entry in my_list[1:]:
        employee_full_name = ' '.join(entry[:3])
        employee_full_name_list = employee_full_name.split()
        hepl_list = ['', '', '']
        for i, j in enumerate(employee_full_name_list):
            hepl_list[i] = employee_full_name_list[i]
        new_employee = hepl_list + entry[3:]
        new_employee_list.append(new_employee)
    new_contacts_list = my_list[:1] + new_employee_list
    return new_contacts_list


def new_phones(my_list):
    pattern = (r'(8|\+7)\s*\(*(\d{3})\)*[-\s*]*(\d{3})[-\s*]*'
               r'(\d{2})[-\s*]*(\d{2})\s*\(*(доб\.)*\s*(\d{4})*\)*')
    btf_number = r'+7(\2)\3-\4-\5 \6\7'
    for employee in my_list[1:]:
        new_phone = re.sub(pattern, btf_number, employee[-2])
        employee[-2] = new_phone
    return my_list


def delete_dupls(my_list):
    new_employees_dict = {}
    for employee in my_list[1:]:
        new_employee = ' '.join(employee[0:2])
        if new_employee not in list(new_employees_dict.keys()):
            new_employees_dict[new_employee] = employee
        else:
            for ind, value in enumerate(new_employees_dict[new_employee]):
                if value == '':
                    new_employees_dict[new_employee][ind] = employee[ind]
    new_contacts_list = my_list[:1] + list(new_employees_dict.values())
    return new_contacts_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  my_contact_list = delete_dupls(new_phones(full_names(contacts_list)))
  datawriter.writerows(my_contact_list)