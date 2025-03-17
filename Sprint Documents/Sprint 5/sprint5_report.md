# Sprint 5 Report (2/10/25-3/10/25)

## YouTube link of Sprint * Video (Make this video unlisted)

## What's New (User Facing)
 * Fix graphs' x-axis labeling
 * Allow users to opt in for what parts of the survey they want to take
 * Have the PICA report only print the parts of the survey the user took
 * Add final text fixes to PICA report

## Work Summary (Developer Facing)
During this sprint, our client had us focusing on finalizing the report generator as well as the Qualtrics survey. This entailed adding any final edits to the text on the generated report, fixing the graphs so they were on the proper scale, making sure that the figure were generating correctly on the report generator, and adding in the new option to allow users to opt in for the parts of the survey they wanted to take. To allow users to opt in, we had to add a new question to the Qualtrics survey, and then edit our report generator so it would pull in that new question's data from the Qualtrics API and thus only add the parts of the survey the user opted in for to their report.

## Unfinished Work
If applicable, explain the work you did not finish in this sprint. For issues/user stories in the current sprint that have not been closed, (a) any progress toward completion of the issues has been clearly tracked (by checking the checkboxes of  acceptance criteria), (b) a comment has been added to the issue to explain why the issue could not be completed (e.g., "we ran out of time" or "we did not anticipate it would be so much work"), and (c) the issue is added to a subsequent sprint, so that it can be addressed later.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * URL of issue 1
 * URL of issue 2
 * URL of issue n

 Reminders (Remove this section when you save the file):
  * Each issue should be assigned to a milestone
  * Each completed issue should be assigned to a pull request
  * Each completed pull request should include a link to a "Before and After" video
  * All team members who contributed to the issue should be assigned to it on GitHub
  * Each issue should be assigned story points using a label
  * Story points contribution of each team member should be indicated in a comment
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
 
 * URL of issue 1 <<One sentence explanation of why issue was not completed>>
 * URL of issue 2 <<One sentence explanation of why issue was not completed>>
 * URL of issue n <<One sentence explanation of why issue was not completed>>
 
 Examples of explanations (Remove this section when you save the file):
  * "We ran into a complication we did not anticipate (explain briefly)." 
  * "We decided that the feature did not add sufficient value for us to work on it in this sprint (explain briefly)."
  * "We could not reproduce the bug" (explain briefly).
  * "We did not get to this issue because..." (explain briefly)

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
