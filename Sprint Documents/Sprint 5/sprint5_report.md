# Sprint 5 Report (2/10/25-3/10/25)

## YouTube link of Sprint * Video (Make this video unlisted)
https://youtu.be/7JfYkXJAc7g

## What's New (User Facing)
 * Fix graphs' x-axis labeling
 * Allow users to opt in for what parts of the survey they want to take
 * Have the PICA report only print the parts of the survey the user took
 * Add final text fixes to PICA report

## Work Summary (Developer Facing)
During this sprint, our client had us focusing on finalizing the report generator as well as the Qualtrics survey. This entailed adding any final edits to the text on the generated report, fixing the graphs so they were on the proper scale, making sure that the figure were generating correctly on the report generator, and adding in the new option to allow users to opt in for the parts of the survey they wanted to take. To allow users to opt in, we had to add a new question to the Qualtrics survey, and then edit our report generator so it would pull in that new question's data from the Qualtrics API and thus only add the parts of the survey the user opted in for to their report.

## Unfinished Work
The work we did not finish the sprint was creating a clinical copy of the report generator for our client, Belinda Lin. We need to finalize the report generator before we can create the clinical copy and so we have worked on fixing those errors the client asks of us before we create the new copy. The issue was not completed this sprint because we need another round of feedback from the client to make sure that the report looks how the client wants it.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/63
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/61
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/62
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 Christian Manangan: 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/55  Story Points:5 
* Belinda wants a copy (clinical version) of the final version of the system. Once we get Dr. Scotts' approval, making a clone would be easy
  
## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Report_Generator_Sorting.py
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/PDF_Generator.py
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/PDF_Generator.py
 * https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Data_Pruner.py
 
## Retrospective Summary
Here's what went well:
  * Once changes have been implemented on our local version, we updated the PythonAnywhere files right away. Didn't wait till last minute.
 
Here's what we'd like to improve:
   * Distinguishing between system files and local files
  
Here are changes we plan to implement in the next sprint:
   * Creating a clinical version of the system
   * Testing
