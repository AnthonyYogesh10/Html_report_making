# Html_report_making

How to Run this code::
1) Download this project.

2) Open it in Pycharm Community Edition(Which is free and open source)

3) Click Settings --> click project: Html_report_making --> then Python Interpreter,
   click '+' symbol to install required packages.
   
4) Don't forget to install important Packages pytest-html, pytest-csv, pytest-excel

5) Open Terminal to run code

6) Concept is to store Reports in reports folder so use the below code to get html report and excel report and store them on report folder,
 
       1) First select the directory of TestCase

          i) use cd to change directory 
          ii) eg : /Desktop/automation/Html_report_making/test_cases/full_crud_module

       2) **To run this code, please copy below code and paste it on terminal and press enter** 

           pytest --html=../../reports/html_reports/full_crud_test.html --csv=../../reports/csv_reports/full_crud_test.csv
          
   
       3) Uses of above code:
          pytest --> is used to run the test 
          --html=../../reports/html_reports/full_crud_test.html ---> it generate html report and store it on report dir,
          --csv=../../reports/csv_reports/full_crud_test.csv ---> it generate csv report and store it on report dir
         
          Description: 
          ./../reports ---> report directory is selected
          All_crud_report.html ---> name of the html file   
          All_crud_report.csv ---> name of the csv file 

       4) After execution of automation  report is stored on report folder then --> open with it on browser
       

    
