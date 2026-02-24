#Find the 1R
#Each row is the index of City, Income, FICO Score, Loan Application
from collections import Counter

city = ['San Jose', 'Fremont', 'San Jose', 'Milpitas', 'San Jose', 'San Jose', 'Milpitas', 'Fremont', 'San Jose', 'Fremont']
income = ['High', 'Low', 'Low', 'Average', 'Low', 'High', 'High', 'Average', 'Average', 'Average']
fico_score = ['Good', 'Bad', 'Bad', 'Good', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Good']
loan_application = ['Accepted', 'Rejected', 'Rejected', 'Accepted', 'Rejected', 'Accepted', 'Rejected', 'Accepted', 'Rejected', 'Accepted']


print(Counter(city), 'Total number of cities is 10')
print(Counter(income), 'Total number of income statuses is 10')
print(Counter(fico_score), 'Total number of FICO scores is 10')
print(Counter(loan_application), 'Total number of loan applications is 10')

for index in range(len(city)):
    if loan_application[index] == 'Accepted':
        print("City: ", city[index] +",", "Income: ", income[index]+",", "FICO Score: ", fico_score[index]+",", "Loan: ", loan_application[index])

"""
Cities that were San Jose 5, loan applications accepted from SJ are 2; Error is (2/5)
Cities that were Fremont 3, loan applications accepted from Fremont are 2; Error is (1/3)
Cities that were Milpitas 2, loan applications accepted from Milpitas are 1; Error is (1/2)
4 / 10

Average income count was 4, loan applications accepted with average income count was 3; Error is (1/4)
High income count was 3, loan applications accepted with high income count was 2; Error is (1/3)
Low income count was 3, loan applications accepted with low income count was 0; Error is (0/3)
2/10

Bad FICO Score count was 4, loan applications accepted with a Bad score was 0 (0/4)
Good FICO Score count was 6, loan applications accepted with a Good score was 5 (1/6)

1 / 10
"""
#Looking at the FICO score only, will give us a 10% error rate which is the lowest
#1R - If fico score is good, loan application approved