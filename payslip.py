import weasyprint
import jinja2
import os
import pandas as pd
from datetime import datetime

def convertor(value):
    return str(value)

def template_loader(default = 'template/', temp_name = 'index.html'):
    
    

    df = pd.read_excel('payslip.xlsx','Sheet1', converters={'Bank A/C':convertor})


    for index, row in df.iterrows():

        name = row['Name']
        employee_id = row['Employee Id']
        designation = row['Designation']
        gender = row['Gender']
        doj = row['Date of Joining']
        month = row['Month']
        year = row['Year']
        financial_year_from = row['Financial Year From']
        financial_year_to = row['Financial Year To']
        pfnum = row['PF UAN']
        dob = row['Date of Birth']
        location = row['Location']
        pan = row['PAN']
        bank_ac = row['Bank A/C']
        ifsc = row['IFSC Code']
        esi_number = row['ESI Number']
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
        net_sal =row['Net Salary (A)-(B)']
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
        'month': month,
        'financial_year_from':financial_year_from,
        'financial_year_to':financial_year_to,
        'year':year,
        'pfnum':pfnum,
        'bank_ac':bank_ac,
        'ifsc': ifsc,
        'esi_number': esi_number,
        'calendar': calendar,
        'paid_days':paid_days,
        'lop_days':lop_days,
        'basic': f'{basic:,}',
        'rent_allowance':f'{hra:,}',
        'con_allowance': f'{ca:,}',
        'spl': f'{spl:,}',
        'pf': f'{pf:,}',
        'tds': f'{tds:,}',
        'esi': f'{esi:,}',
        'total_earnings': f'{total_earnings:,.2f}',
        'total_deductions': f'{total_deductions:,.2f}',
        'net_sal': f'{net_sal:,.2f}',
        'in_words':in_words,
  
        

        }
        path = str(os.path.join(os.getcwd(), 'template'))
        image_path = str(os.path.join(os.getcwd(), 'images'))
        locator = jinja2.FileSystemLoader(path)
        environment = jinja2.Environment(loader=locator)
        template = environment.get_template(temp_name)
        output_string = template.render(context)

        data = output_string   
        css = weasyprint.CSS(filename='template/index.css')
        name = context['name']
        file_name = f'{name} payslip-{month}-{year}.pdf'
        pdf = weasyprint.HTML(string=data, base_url=image_path).write_pdf(stylesheets = [css])
        folder_name = f'{month} {year} Payslips'
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        with open(os.path.join(folder_name,file_name), 'wb') as f:
            f.write(pdf)

            


template_loader()


print(os.path.join(os.getcwd(), 'template'))


