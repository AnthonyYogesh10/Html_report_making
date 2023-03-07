# Html_report_making

How to Run this code::
1) Download this project.

2) Open it in Pycharm Community Edition(Which is free and open source)

3) Click Settings --> click project: Html_report_making --> then Python Interpeter
   to install required packages.
   
4) Don't forget to install pytest-html

5) Open Terminal to run code

6) Concept is to store Reports in reports folder so use the below code to get html report,
 
       1) First select the directory of TestCase eg : /Desktop/automation/Html_report_making/test_cases/full_crud_module
       
       2) After selecting testCase copy this code ---> pytest --html=../../reports/All_crud_report.html --css=../../utilities/style.css 
       
       3) All_crud_report.html ---> name of the report and --css=../../utilities/style.css ---> to use our Style format
       
       4) After execution of automation  report is stored on report folder then --> open with it on browser
       

    
