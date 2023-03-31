# Html_report_making

How to Run this code::
1) Download this project.

2) Open it in Pycharm Community Edition(Which is free and open source)

3) Click Settings --> click project: Html_report_making --> then Python Interpeter
   to install required packages.
   
4) Don't forget to install pytest-html

5) Open Terminal to run code

6) Concept is to store Reports in reports folder so use the below code to get html report and excel report and store them on report folder,
 
       1) First select the directory of TestCase eg : /Desktop/automation/Html_report_making/test_cases/full_crud_module

       2) **To run this code, please copy below code and paste it on terminal and press enter** 

          pytest --html=../../reports/All_crud_report.html --excelreport=../../reports/All_crud_report.xlsx 
          
   
       3) Uses of above code:
          --html=../../reports/All_crud_report.html ---> it generate html report and store it on report dir,
          --excelreport=../../reports/All_crud_report.xlsx ---> it generate excel report and store it on report dir
         
          Description: 
          ./../reports ---> report directory is selected
          All_crud_report.html ---> name of the html file   
          All_crud_report.xlsx ---> name of the excel file 

       4) After execution of automation  report is stored on report folder then --> open with it on browser
       

    
