import weasyprint
import jinja2
import os
import pandas as pd
from datetime import datetime
def template_loader(default = './', temp_name = 'index.html'):
    
    

    df = pd.read_excel('payslip.xlsx','Sheet1')
    month = datetime.strftime(datetime.now(), '%B')
    year = datetime.strftime(datetime.now(), "%Y")
    next_year = str(int(year)+1)

    for index, row in df.iterrows():

        name = row['Name']
        employee_id = row['Employee Id']
        designation = row['Designation']
        month = month
        gender = row['Gender']
        doj = row['Date of Joining']
        pfnum = row['PF A/C']
        dob = row['Date of Birth']
        uan = row['UAN']
        location = row['Location']
        pan = row['PAN']
        bank_ac = row['Bank A/C']
        ifsc = row['IFSC Code']
        esi = row['ESI Number']
        calendar = row['Available Calendar Days']
        paid_days = row['Paid Days']
        lop_days = row['LOP Days']
        basic = row['Basic']
        hra = row['House Rent Allowance(HRA)']
        ca = row['Conveyance Allowance']
        spl = row['Special Allowance']
        pf = row['PF']
        tds = row['TDS']
        esi = row['ESI']
        total_earnings = row['(A) Total Earnings']
        total_deductions = row['(B) Total Deductions']
        net_sal = row['Net Salary (A)-(B)']
        in_words = row['In Words']
        context= {
        'name':name,
        'employee_id':employee_id,
        'designation': designation,
        'location': location,
        'pan':pan,
        'gender': gender,
        'doj': doj,
        'dob':dob,
        'pfnum':pfnum,
        'bank_ac':bank_ac,
        'uan':uan,
        'ifsc': ifsc,
        'esi': esi,
        'calendar': calendar,
        'paid_days':paid_days,
        'lop_days':lop_days,
        'basic': basic,
        'rent_allowance':hra,
        'con_allowance': ca,
        'spl':spl,
        'pf':pf,
        'tds':tds,
        'esi':esi,
        'total_earnings':total_earnings,
        'total_deductions':total_deductions,
        'net_sal':net_sal,
        'in_words':in_words,
        'month': month,
        'year': year,
        'next_year': next_year,
        

        }
        # path = str(os.path.join(os.getcwd(), 'template'))
        # image_path = str(os.path.join(os.getcwd(), 'images'))
        locator = jinja2.FileSystemLoader('./')
        environment = jinja2.Environment(loader=locator)
        template = environment.get_template(temp_name)
        output_string = template.render(context)

        data = output_string
        css = weasyprint.CSS(filename='index.css')
        name = context['name']
        file_name = f'{name} payslip-{month}-{year}.pdf'
        pdf = weasyprint.HTML(string=data, base_url='./').write_pdf(stylesheets = [css])
        folder_name = f'{month} {year} Payslips'
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        with open(os.path.join(folder_name,file_name), 'wb') as f:
            f.write(pdf)

            


template_loader()


print(os.path.join(os.getcwd(), 'template'))


