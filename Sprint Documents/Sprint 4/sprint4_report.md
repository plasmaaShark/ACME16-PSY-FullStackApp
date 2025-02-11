
Page
1
of 2
# Sprint 4 Report (01/10/25 - 02/10/25)
## YouTube link of Sprint * Video (Make this video unlisted)
https://youtu.be/uBIiNWOlyYo
## What's New (User Facing)
* Added positive and negative edits to phone app
* Add therapy page to phone app
* Fix minor edits and missing data from PICA report generator
## Work Summary (Developer Facing)
During this sprint, we first focused on familiarizing ourselves with the phone app files and implemented the positive and negative edits to the situations workflow. We then also added a new therapy page to the phone app that the client requested that appears right before the sorting page when creating a new situation. This page would allow the user to reflect on their answers from previous pages and revise some of their answers if they want to. We had to add a new form to our Flask application, create a new HTML page, and then also insert in data from pevious forms completed. We also added the new information from the therapy page into the past situations page so the user could see their previous responses to the new therapy page. Finally, during the last week of the sprint we have worked on fixing minor edits to the report generator from our previous semester. This includes fixing some of the typos and fixing graphs that showed that data was missing when it was not.
## Unfinished Work
The work we did not finish the sprint was creating a clinical copy of the report generator for our client, Belinda Lin. We need to finalize the report generator before we can create the clinical copy and so we have worked on fixing those errors the client asks of us before we create the new copy. The issue was not completed this sprint because we need another round of feedback from the client to make sure that the report looks how the client wants it.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
* URL of issue 1
* URL of issue 2
* URL of issue n
Reminders (Remove this section when you save the file):
* Each issue should be assigned to a milestone
* Each completed issue should be assigned to a pull request
* Each completed pull request should include a link to a "Before and After" video
* All team members who contributed to the issue should be assigned to it on
GitHub
* Each issue should be assigned story points using a label
* Story points contribution of each team member should be indicated in a comment
  
## Incomplete Issues/User Stories
Here are links to issues we worked on but did not complete in this sprint:
Christian Manangan: 
https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/issues/55  Story Points:5 
* Belinda wants a copy (clinical version) of the final version of the system. Once we get Dr. Scotts' approval, making a clone would be easy
  
## Code Files for Review
Please review the following code files, which were actively developed during this
sprint, for quality:
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/psychclinic.py
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/Controller/forms.py
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/Controller/routes.py
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/Model/models.py
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/View/static/css/main.css
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/View/templates/behavior.html
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/View/templates/feelings.html
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/View/templates/feelings_page.html
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/View/templates/sorting.html
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/MongoPsychClinicWeb/app/View/templates/thoughts.html
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Report_Generator_Sorting.py
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/PDF_Generator.py
* https://github.com/plasmaaShark/ACME16-PSY-FullStackApp/blob/main/PsychClinic-ReportGenerator/Data_Pruner.py
  
## Retrospective Summary
Here's what went well:
* Fixed double emailing issue of the PDF
* All web app changes requested by the client has been implemented
* All minor pdf modifications requested by the client has been implemented
  
Here's what we'd like to improve:
* Updating the PythonAnywhere files once we have a working local version with our changes
  
Here are changes we plan to implement in the next sprint:
* Finalizing the report generator
* Changing the workflow of the Qualtrics survey to make certain parts of the PICA optional
* Looking into improving the clustering algorithm with an LLM
