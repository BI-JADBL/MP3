# MP3
Project Summary – Employee Attrition Prediction
1. Machine learning methods used and why
We used both classification and clustering algorithms:

Logistic Regression for predicting salary.

KMeans and MeanShift for unsupervised clustering to explore natural groupings of employees.

These methods were chosen because we used them i school.

2. Accuracy and quality measures
Accuracy scoreindicates the percentage of correctly predicted cases.

Confusion matrix shows true/false positives and negatives.

F1-score balances precision and recall — useful for imbalanced classes like attrition (where most employees stay).

Silhouette score was used in clustering to measure how well-defined the clusters are.

3. Decisive factors for quitting a job

   We focused more on salary than attrition but key predictors would typically include: JobSatisfaction, WorkLifeBalance, EnvironmentSatisfaction, OverTime, and MonthlyIncome.


4. Ways to improve accuracy
Use feature engineering.

Try advanced models like XGBoost or Neural Networks.

Perform hyperparameter tuning.

Address class imbalance using oversampling (SMOTE) or balanced class weights.

The only thing we really tried was removing outliers, but the result of our model turned out worse  

5. Departments and positions at higher risk
once again we misunderstood and focused on salary instead

6. Equal pay across gender?
same as above

7. Does family status or distance affect work-life balance?
same as above

8. Does education improve satisfaction?


9. Main challenges in development
In our development it would be sickness. Half the group was out for multiple days. Other than that obviuosly focusing too much on code and not so much on the questions. In regards to the questions above then in the future we would argue that our model works and with a little more time we would implement the right columns and such, so that we would get the right answers
