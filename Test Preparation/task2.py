import pandas as pd

sal = pd.read_csv('Salaries.csv')


print(sal.head())


print(sal.info())


sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors='coerce')
average_basepay = sal['BasePay'].mean()
print(f"Average BasePay: {average_basepay}")


sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors='coerce')
print(f"Highest OvertimePay: {max(sal['OvertimePay'])}")


joseph_driscoll_info = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
joseph_driscoll_title = joseph_driscoll_info['JobTitle'].values[0]
print(f"Job Title of JOSEPH DRISCOLL: {joseph_driscoll_title}")


joseph_driscoll_salary = joseph_driscoll_info['TotalPayBenefits'].values[0]
print(f"Salary of JOSEPH DRISCOLL (including benefits): {joseph_driscoll_salary}")


highest_paid_person = sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']
print(f"Name of the highest paid person (including benefits): {highest_paid_person}")


lowest_paid_person = sal.loc[sal['TotalPayBenefits'].idxmin()]['EmployeeName']
print(f"Name of the lowest paid person (including benefits): {lowest_paid_person}")


average_basepay_per_year = sal.groupby('Year')['BasePay'].mean()
print(f"Average BasePay per Year: {average_basepay_per_year}")


unique_job_titles = sal['JobTitle'].nunique()
print(f"Number of unique job titles: {unique_job_titles}")


top_5_jobs = sal['JobTitle'].value_counts().head(5)
print(f"Top 5 most common jobs: {top_5_jobs}")


job_titles_2013_one_person = (
    sal[sal['Year'] == 2013]
    .groupby('JobTitle')
    .filter(lambda group: len(group) == 1)
    .nunique()
)
print(f"Number of Job Titles represented by only one person in 2013: {job_titles_2013_one_person}")


chief_count = sal['JobTitle'].str.lower().str.contains('chief').sum()
print(f"Number of people with the word Chief in their job title: {chief_count}")


correlation = sal.apply(lambda row: len(str(row['JobTitle'])), axis=1).corr(sal['TotalPayBenefits'])
print(f"Correlation between Job Title length and Salary: {correlation:.2f}")
