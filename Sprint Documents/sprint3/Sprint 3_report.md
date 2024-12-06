# Sprint 3 Report (11/05/24 - 12/05/24)

## YouTube link of Sprint * Video (Make this video unlisted)
https://youtu.be/wskZBLFgjfU

## What's New (User Facing)
 * Fix existing radar graph code and push fixes
 * Move graphs to span whole page with text underneath them.
 * Move ranked goals and personal goals side by side
 * Fix missing values causing error with sorting

## Work Summary (Developer Facing)
 We have finished implementing the changes to the PDF report for the Person in Context Assesment (PICA). These changes include adding more descriptive text to the graphs, moving the graphs and their text to span the whole page instead of being side by side, and adding 'missing' text to the graph when they have missing values. One challenge we faced this sprint was our main report generator facing an error when the user's goals were missing. We were able to fix the sorting algorithm to handle the null array when sorting the goals and allow the report to run even with missing values.

## Unfinished Work
NONE

## Completed Issues/User Stories
Below are the issues completed during this sprint:

Shaylin Smith:https:
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/44  Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/45 Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/46 Story Points:3 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/49 Story Points:3 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/51 Story Points:5 

Jiaming Chu:
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/44  Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/45 Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/47 Story Points:3 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/50 Story Points:5 

Christian Manangan: 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/44  Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/45 Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/48 Story Points:3 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/51 Story Points:5 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/53 Story Points:5 

 ## Incomplete Issues/User Stories
NONE

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Results_Sorted.py
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Report_Generator_Sorting.py
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/PDF_Generator.py
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Graph_Generator.py
 
## Retrospective Summary
Here's what went well:
  * All PDF modifications requested by the client has been implemented
  * Client Demo went well
  * System now generates and sends the new PDF report with all the modifications automatically whenever a survey is submitted
 
Here's what we'd like to improve:
   * Getting familiar with the phone app's infrastructure. Learning how to do minor changes such as changing UI text and navigating through the MongoDB database.
  
Here are changes we plan to implement in the next sprint:
   * All focus will be on the phone app. Some key changes include improving the clustering algorithm and having a way to input survey results from the qualtrics survey into the phone app


