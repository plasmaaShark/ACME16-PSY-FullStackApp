# Sprint 2 Report (10/06/24 - 11/05/24)

## What's New (User Facing)
 * New system for automatically sending PICA results PDF to user's email
 * Fixed Qualtrics API issues
 * New more understandable results PDF for PICA
 
## Work Summary (Developer Facing)
During this sprint, our first feature the client wanted to implement was making sure that the PICA results PDF was automatically sent to the user once they finished their assesment. Previously, the user would have to go into PythonAnywhere to get their results. We had to first work out the 401 issue that happened when the code tried to make an API call to PythonAnywhere that was not supported anymore. That call was what allowed the code to run after the user finished their assesment. We instead replaced that system with a Flask framework which is more supported and should last longer than the deprecated PythonAnywhere API. We also had to edit the Qualtrics API token that allows the code to get the Qualtrics survey data. We figured out that an old token was being used and we replaced it with the correct one. Once we got those solved, the PDFs were able to send to the correct user easily. After that, we then went to work on editing the layout of the results PDF based upon the client's needs. The main part was adding in more text explaining the different graphs and charts and what the different temperments meant. This allowed for the results to be more understandable to the user.
## Unfinished Work


## Completed Issues/User Stories
Below are the issues completed during this sprint:

Shaylin Smith


Jiaming Chu


Christian Manangan


## Incomplete Issues/User Stories


## Code Files for Review


## Retrospective Summary
### What Went Well:

  
### Areas for Improvement:

  
### Planned Changes for Next Sprint:

