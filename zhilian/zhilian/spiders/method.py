def getJobGrade(value):
    jobGrade=''
    if value=='无经验' or value=='1年以下':
        jobGrade='入门'
    elif value== '1-3年':
        jobGrade='初级'
    elif value=='3-5年':
        jobGrade='中级'
    elif value== '5-10年':
        jobGrade='高级'
    elif value== '10年以上':
        jobGrade='专家'
    elif value=='不限':
        jobGrade='不限'
        # fail()
    # print('getJobGrade')
    return jobGrade

def getJobSalary(value):
    print(value,'iouoiu')
    if '不限' in value:
        avgSalary = 8
        return 
    else:
        salArr = value.split('元')
        if '-' in salArr[0]:
            Salary = (int(salArr[0].split('-')[0][:-3])+int(salArr[0].split('-')[1][:-3]))/2
            avgSalary = float('%.2f' % Salary)
        else:
            avgSalary = int(salArr[0][:-3])
    return avgSalary

def getIndustry(value):
    # print('getIndustry')
    if value:
        if ',' in value:
            NewIndustry=value.split(',')
            return NewIndustry[0]
        elif '、'  in value:
            NewIndustry=value.split('、')
            return NewIndustry[0]
        elif '/'  in value:
            NewIndustry=value.split('/')
            return NewIndustry[0]
        else:
            return value
    else:
        # fail()
        return 'none'

