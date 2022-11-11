
import streamlit as st
from numpy import dsplit
import pickle

st.title("Employee Attrition Within a year Prediction")
pickle_in = open('classifier1.pkl',"rb")
classifier = pickle.load(pickle_in)


def prediction(Age, DailyRate, DistanceFromHome,Education,
       EnvironmentSatisfaction,HourlyRate, JobInvolvement, JobLevel,
       JobSatisfaction, MonthlyIncome, NumCompaniesWorked,
       PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
       StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
       WorkLifeBalance, YearsAtCompany, YearsSinceLastPromotion,
       BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,
       OverTime): 

    if  BusinessTravel == 'Travel_Frequently':
        BusinessTravel_Travel_Frequently = 1
        BusinessTravel_Travel_Rarely = 0
    elif  BusinessTravel == 'Travel_Rarely':
        BusinessTravel_Travel_Frequently = 0
        BusinessTravel_Travel_Rarely = 1
    else:
        BusinessTravel_Travel_Frequently = 0
        BusinessTravel_Travel_Rarely = 0


    if Department == "Hardware":
        dhr = 0
        d_res_dev = 0
        d_sales =0
        d_soft = 0
        d_support =0
    elif Department == "Research & Development":
        dhr = 1
        d_res_dev = 0
        d_sales =0
        d_soft = 0
        d_support =0
    elif Department == "Sales":
        d_sales = 1
        dhr = 0
        d_soft = 0
        d_res_dev = 0
        d_support =0
    elif Department == "Software":
        d_sales = 0
        dhr = 0
        d_soft = 1
        d_res_dev = 0
        d_support =0
    else:
        d_sales = 0
        dhr = 0
        d_soft = 0
        d_res_dev = 0
        d_support =1

    

    if EducationField == 'Medical':
        Medical =1         
        Life_Sciences =0     
        Technical_Degree =0      
        Other =0            
        Marketing =0   

    elif EducationField == 'Life Sciences':
        Medical =0         
        Life_Sciences =1     
        Technical_Degree =0      
        Other =0            
        Marketing =0

    elif EducationField == 'Technical Degree':
        Medical =1         
        Life_Sciences =0     
        Technical_Degree =1      
        Other =0            
        Marketing =0  

    elif EducationField == 'Other':
        Medical =1         
        Life_Sciences =0     
        Technical_Degree =1      
        Other =0            
        Marketing =0 

    else:
        Medical =0        
        Life_Sciences =0     
        Technical_Degree =1      
        Other =0            
        Marketing =1

    

    if Gender =='Male':
        male = 1
    else :
        male=0


    if JobRole == "Sales Executive":
        se =1
        rs=0
        jhr=0
        manager=0
        hcr=0
        rd=0
        sr=0
        lt=0
        md=0
    elif JobRole == "Research Scientist":
        se =0
        rs=1
        jhr=0
        manager=0
        hcr=0
        rd=0
        sr=0
        lt=0
        md=0
    elif JobRole == "Human Resources":
        se =0
        rs=0
        jhr=1
        manager=0
        hcr=0
        rd=0
        sr=0
        lt=0
        md=0
    elif JobRole == "Manager":
        se =0
        rs=0
        jhr=0
        manager=1
        hcr=0
        rd=0
        sr=0
        lt=0
        md=0
    elif JobRole == "Healthcare Representative":
        se =0
        rs=0
        jhr=0
        manager=0
        hcr=1
        rd=0
        sr=0
        lt=0
        md=0
    elif JobRole == "Research Director":
        se =0
        rs=0
        jhr=0
        manager=0
        hcr=0
        rd=1
        sr=0
        lt=0
        md=0
    elif JobRole == "Laboratory Technician":
        se =0
        rs=0
        jhr=0
        manager=0
        hcr=0
        rd=0
        sr=0
        lt=1
        md=0
    elif JobRole == "Manufacturing Director":
        se =0
        rs=0
        jhr=0
        manager=0
        hcr=0
        rd=0
        sr=0
        lt=0
        md=1
    elif JobRole == "Sales Representative":
        se=0
        rs=0
        jhr=0
        manager=0
        hcr=0
        rd=0
        sr=1
        lt=0
        md=1
    else:
        se =0
        rs=0
        jhr=0
        manager=0
        hcr=0
        rd=0
        sr=0
        lt=0
        md=0
    
    if MaritalStatus=='Married':
        marr = 1
        sing = 0

    elif MaritalStatus=='Single':
        marr = 0
        sing = 1
    else:
        marr = 0
        sing = 0


    if OverTime =='Yes':
        yes = 1
    else:
        yes = 0

    

    prediction = classifier.predict([[Age, DailyRate, DistanceFromHome, Education,
        EnvironmentSatisfaction,HourlyRate, JobInvolvement, JobLevel,
        JobSatisfaction, MonthlyIncome, NumCompaniesWorked,
        PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
        StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
        WorkLifeBalance, YearsAtCompany, YearsSinceLastPromotion,
        BusinessTravel_Travel_Frequently, BusinessTravel_Travel_Rarely,
        dhr, d_res_dev,d_sales,d_soft,d_support,
        Life_Sciences,Marketing,Medical,Other,Technical_Degree,
        male,hcr,jhr,lt,manager,md,rd,rs,se,sr,marr,sing,
        yes]])
     
    
    return prediction 
def main(): 
    col1,col2,col3 = st.columns(3)
    with col1:       
        age = st.text_input('Enter Age') 
        DailyRate = st.text_input('Enter DailyRate')
        HourlyRate = st.text_input('Enter HourlyRate')
        DistanceFromHome = st.text_input('Enter Distance From Home')
        EnvironmentSatisfaction = st.text_input('Enter Environment Satisfaction')
        JobInvolvement = st.text_input('Enter Job Involvement')
        JobLevel = st.text_input('Enter Job Level')
        JobSatisfaction = st.text_input('Enter Job Satisfaction')
        MonthlyIncome = st.text_input('Enter Monthly Income')
    with col2:
        NumCompaniesWorked = st.text_input('Enter Number of Companies Worked')
        PercentSalaryHike = st.text_input('Enter Percent Salary Hike')
        RelationshipSatisfaction = st.text_input('Enter Relationship Satisfaction')
        StockOptionLevel = st.text_input('Enter Stock Option Level')
        TotalWorkingYears = st.text_input('Enter Total Working Years')
        TrainingTimesLastYear = st.text_input('Enter Training Times LastYear')
        WorkLifeBalance = st.text_input('Enter Worklife Balance')
        YearsAtCompany = st.text_input('Enter YearsAt Company')
        YearsSinceLastPromotion = st.text_input('Enter Years Since Last Promotion')
    with col3:
        PerformanceRating = st.text_input('Enter Performance Rating ')
        Education = st.text_input('Enter Education')
        BusinessTravel= st.selectbox("Select type of business travel", ('Travel_Frequently','Travel_Rarely',"Non-Travel")) 
        Department=st.selectbox("Select type of department", ('Life Sciences','Sales', 'Support','Software','Research & Development','Human Resources','Hardware')) 
        EducationField=st.selectbox("Select type of education field", ('Other','Marketing','Medical','Technical Degree','Human Resources','Life Sciences')) 
        Gender=st.selectbox("Select  Gender ", ('Male','Female'))
        JobRole=st.selectbox("Select type of Jobrole ", ('Sales Executive', "Research Scientist", "Human Resources",
                                              "Manager","Healthcare Representative","Research Director",'Laboratory Technician','Manufacturing Director','Developer'))
        MaritalStatus=st.selectbox("Select MaritalStatus", ('Single', 'Married',"Divorce"))
        OverTime=st.selectbox("Select OverTime", ('Yes','No'))

    result = ""

    if st.button("Predict"): 
        result = prediction(age, DailyRate, DistanceFromHome,Education,
       EnvironmentSatisfaction,HourlyRate,JobInvolvement, JobLevel,
       JobSatisfaction, MonthlyIncome, NumCompaniesWorked,
       PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
       StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
       WorkLifeBalance, YearsAtCompany, YearsSinceLastPromotion,
       BusinessTravel,Department,EducationField,Gender,JobRole,MaritalStatus,
       OverTime) 
       
        if result==0:
            st.success('The Employee will not get attritioned'.format(result))
            
        else:
            st.success('The Employee will get attritioned'.format(result))


if __name__ == "__main__":
    main()
