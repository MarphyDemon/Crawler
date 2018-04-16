failcount = 0
falseSalary = 0
count = 0

#  统计总数
def getCount():
    global count
    count = count+1
    # print(getCount,'getCount')
    return count

# 统计无效的数据
def fail():
    global failcount
    failcount = failcount+1
    # print(failcount,'failcount')
    return failcount

def failSalary():
    global falseSalary
    falseSalary = falseSalary+1
    # print(falseSalary,'falseSalary')
    return falseSalary

def getJobGrade(value):
    jobGrade=''
    if value=='应届毕业生' or value=='1年以下':
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
    value=value.replace('K','k')
    if value:
        if '-' in value:
            Salary=value.split('-')
            Salary=(int(Salary[0].split('k')[0])+int(Salary[1].split('k')[0]))/2
            # print('getJobSalary')
            avgSalary = float('%.2f' % Salary)
        else:
            avgSalary = int(Salary[0].split('k')[0])
    else:
        avgSalary = 0
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
        else:
            return value
    else:
        # fail()
        return 'none'

def getMonth(value):
    i={}
    if value:
        datestr = value.split(" ")[0]
        dateArray = datestr.split("-")
        i['year'] = dateArray[0]
        i['month'] = dateArray[1]
        return i
    else:
        return 'none'


#未融资。天使轮，A轮 B轮 C轮 D轮 不需要融资 上市公司
#def getCompanyValue(value):
#   # if value==''    

# def getfail():
    # return failcount