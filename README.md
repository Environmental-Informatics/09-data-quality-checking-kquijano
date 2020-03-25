# Environmental Informatics

## Assignment 09 - Automated Data Quality Checking with Python

### Lab Objectives

On completion of this lab, students will be able to:

1. Check datasets for gross errors, check for inconsistencies in variables, and check for range problems;
2. Encapsulate each check in a function, that also returns information on how many data points failed checks; and
3. Summarize the results of the data quality check.

### Reading Assignment

Two journal articles related to data quality checking:

- Reek, T., S.R. Doty, and T.W. Owen, 1992: A Deterministic Approach to the Validation of Historical Daily Temperature and Precipitation Data from the Cooperative Network. Bull. Amer. Meteor. Soc., 73, 753–765, [https://doi.org/10.1175/1520-0477(1992)073<0753:ADATTV>2.0.CO;2](https://doi.org/10.1175/1520-0477(1992)073<0753:ADATTV>2.0.CO;2)

- Hu, Q. and S. Feng, 2003: A Daily Soil Temperature Dataset and Soil Temperature Climatology of the Contiguous United States. J. Appl. Meteor., 42, 1139–1156, [https://doi.org/10.1175/1520-0450(2003)042<1139:ADSTDA>2.0.CO;2](https://doi.org/10.1175/1520-0450(2003)042<1139:ADSTDA>2.0.CO;2)

### The Lab Assignment

This week’s assignment is to conduct basic data quality checking on a meteorological data with some known problems.

1. Use the file **DataQualityChecking.txt** provided with this repository.

   - This file contains daily climate data for a single site.
   - Data file is white space delimited.
   - Columns are in order:
     - date,
     - precipitation (mm),
     - maximum air temperature (°C)
     - minimum air temperature (°C), and
     - wind speed (m/s)
     
2. Modify the Python script template called **program_09_template.py** to complete this assignment.  The template contains code defining function names and input/output parameters, as well as comment text describing what each function should accept as parameters, return as variables, and functionally what each function should do.  
   - **DO** rename the python script template to **program_09.py**, and **DO NOT** change the name or order of the parameters being sent to or from each function.  
   - The template defines functions that the autograder program is going to import and evaluate.  
   - Any variation in the submission program name (**program_09.py**) or the function definitions (input parameters and returned parameters), will cause the autograder to fail even if your code "works" for you.  

2. Modify the Python script template called program_09.py so that it does the following:

   - Imports the entire file in as a DataFrame, using date as the index.
   - Completes the following data quality checks:
     - **Check 1:** Removes `No Data` values.
       - Replace all values of -999 in this file with the NumPy NaN values (e.g., numpy.NaN or np.NaN).
       - Record the number of values replaced for each data type in the dataframe ReplacedValuesDF with the index "1. No Data"
     - **Check 2:** Check for gross errors
       - Apply the following error thresholds: 0 ≤ P ≤ 25; -25≤ T ≤ 35, 0 ≤ WS ≤ 10.
       - Replace values outside this range with NaN.
       - Record the number of values replaced for each data type in the dataframe ReplacedValuesDF with the index "2. Gross Error"
     - **Check 3:** Swap `Max Temp` and `Min Temp` when `Max Temp` is less than `Min Temp`.
       - Check that all values of `Max Temp` are greater then for `Min Temp` for the current day's observations.
       - Where they are not, swap the values.
       - Record the number of values replaced for each data type in the dataframe ReplacedValuesDF with the index "3. Swapped"
     - **Check 4:** Check for daily temperature range exceedence.
        - Identify days with temperature range (`Max Temp` minus `Min Temp`) greater than 25°C.
        - When range is exceeded replace both Tmax and Tmin with NaN.
        - Record the number of values replaced for each data type in the dataframe ReplacedValuesDF with the index "4. Range Fail"
   - Plot each dataset before and after correction has been made.
     - Use a single set of axis for each variable, and
     - provide a legend that indicates which variable is the original and which is after quality checking.
   - Write data that has passed the quality check into a new file with the same format as the input data file.
   - Output information on failed checks to a separate Tab delimited file that can be imported into your Metadata file.

3. Be sure that the script has a complete header comment block, appropriate in-line comments, and runs without intervention relative to where the datafile is stored in the repository.

4. Create a metadata file called **METADATA.pdf** using Word, OpenOfiice or another document editor.  The metadata file shold contain the following information:

   - Name of the program, name of the program creator and a short decription of what the program does.
   - Description of the data quality checks performed and how they influenced the contents of the file.
   - Table with the number of corrections made for all three checks (should be properly referenced when discussing how data quality checks influenced the contents of the file \[see previous bullet\]). 
   - Plots for each variable before and after quality checking (these should include descriptive captions, and be properly referenced from the text). 

#### What to turn in...

The following should be included in your GitHub repository:

1. A working program called **program_09.py**, which conforms to the template provided with the original repository.

2. The original data file, **DataQualityChecking.txt**, provided with the repository.

3. The output table file from the program.

4. A metadata file called **METADATA.pdf**.

5. Put your input file, output files, and processing script in the assignment repository and push to GitHub. 

6. The instructor will follow-up with an invivtation to submit the assignment through GradeScope.  Follow the provided instructions to submit the assignment using GitHub.  The AutoGrader will return a report on whether the submitted code met the performance checks.  If errors are found, fix the code, and resubmit.

#### Grading Rubric (50 pts Total)

| Question | Description | Score |
| -------- | ----------- | ----- |
| 1. | Write a Python script to complete the following analysis | (33.0 pts) |
| 1.1. | Import the entire file in as a DataFrame, using date as the index | 3.0 pts |
| 1.2. | Check 1: Remove No Data values (set to -999) | 2.5 pts |
| 1.3. | Check 2: Check for gross errors: 0 ≤ P ≤ 25; -25≤ T ≤ 35, 0 ≤ WS ≤ 10 | 5.0 pts |
| 1.4. | Check 3: Swap `Max Temp` and `Min Temp` when `Max Temp` is less than `Min Temp` | 5.0 pts |
| 1.5. | Check 4: Check for temperature range greater than 25°C | 5.0 pts |
| 1.6. | Where a check is failed, fix it or replace value with NaN and record the number of data points replaced for each check. | 2.5 pts |
| 1.7. | Plot each dataset before and after correction has been made.  Use a single set of axis for each variable, and provide a legend that indicates which is the original and which is after quality checking.  | 5.0 pts |
| 1.8. | Output data that has passed the quality check into a new file with the same format as the input data file. | 2.5 pts |
| 1.9. | Output information on failed checks to a separate Tab delimited file that can be imported into your Metadata file. | 2.5 pts |
| 2. | Working program | 5.0 pts |
| 3. | Program should have clear and concise header and in-line comments | 2.5 pts |
| 4. | Metadata file (PDF) that contains: | (7.5 pts) |
| 4.1. | Description of the data quality checks performed and how they influenced the contents of the file. | 2.5 pts |
| 4.2. | Table with the number of corrections made for all three checks. | 2.5 pts |
| 4.3. | Plots for each variable before and after quality checking. | 2.5 pts |
| 5. | Tried GradeScope submission. | 2.0 pts |

### Check that your code is working

Output from the final statement in the template, `print("\nFinal changed values counts.....\n", ReplacedValuesDF)` should be as follows:

```
Final changed values counts.....
                 Precip  Max Temp  Min Temp  Wind Speed
1. No Data         2.0       2.0       2.0         0.0
2. Gross Error    15.0      14.0       2.0         2.0
3. Swapped         0.0       4.0       4.0         0.0
4. Range Fail      0.0       5.0       5.0         0.0
```
