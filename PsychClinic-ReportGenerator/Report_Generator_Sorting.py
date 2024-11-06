import os
from datetime import time

from fpdf import FPDF
import matplotlib.pyplot as plt


import Graph_Generator
import PDF_Generator
import Data_Pruner
import automated_responses
import time
import requests
import Results_Sorted


# email stuff
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Hello,
Your Person in Context Assessment (PICA) results are attached below.
Thank You
'''
# end email stuff

WIDTH = 210
HEIGHT = 297

# need to start the python anywhere console
# username = 'WSUPsych'
# token = 'b19849a8c15e16119580e813c9a1bdc2b9985e5b'
# host = 'www.pythonanywhere.com'


# API endpoint for starting the console
# CONSOLE_START_URL = f'https://{host}/api/v0/user/{username}/consoles/33319540/start/'

def create_report():

    # headers = {
    #     'Authorization': f'Token {token}',
    #     'Content-Type': 'application/json'
    # }
    # response = requests.post(CONSOLE_START_URL, headers=headers)
    # if response.status_code == 200:
    #     print("Console started successfully.")
    # else:
    #     print(f"Error starting console: {response.status_code} - {response.text}")

    # time.sleep(10)
    print('----------------------------------------')

    #number+1 to get total      currently at:tc
    for i in range (13, 14):
        #automated_responses.get_survey(save_survey = "", survey_id = 'SV_3wvBtxhaQcsl06G')
        pdf = FPDF()
        # setting my path as everything leading up to current directory
        my_path = os.path.abspath("")

        # saving the most recent survey result from csv data into pandas df
        df = Graph_Generator.pd.read_csv('Capstone Working Survey.csv')
        idxS = 0-i
        currentSurvey = df.iloc[idxS]
        #print("current survey: ", currentSurvey)
        print('----------------------------------------')
        print('Data Retrieved')
        data = Data_Pruner.get_data('Capstone Working Survey1.csv', idxS)
        #print(data['Personal'])

        # Code for accessing column value by name: value = currentSurvey.loc[:, 'IPAddress'].values[0]
        # IPAddress is the column name in the example above

        # Add title page
        print('----------------------------------------')
        print('Added Title Page')
        title_page(my_path, pdf, data['Personal'])

        #Temperament
        print('----------------------------------------')
        print('Added Temperament Graph')
        stuff = [list(data['Temperament'].values()), list(data['Temperament'].keys())]
        temperament_graph(my_path, pdf, stuff, "Temperament")

        #Self-Concept: Psychological Needs
        print('----------------------------------------')
        print('Added RSSM Graphs')
        rssmTitles = ["Relatedness Satisfaction", "Control Satisfaction", "Self-Esteem Frustration", "Autonomy Frustration"]
        barTitles = [f'Self-with-{v}' if v != 'Overall' else v for k,v in data['RSSMNames'].items()]
        rssm_bar_graphs(my_path, pdf, data['RSSM'], barTitles, rssmTitles)

        #Self-Concept: Rejection Sensitivity
        print('----------------------------------------')
        print('Added Rejection Sensitivity')
        rs_page(pdf, data['RejectionSensitivity'])

        #Self-Concept: Problematic Interpersonal Styles
        print('----------------------------------------')
        print('Added CSIP Graph')
        csipTitles = ["Domineering", "Self-Centered", "Distant/Cold", "Socially Inhibited", "Nonassertive", "Exploitable", "Self-Sacrificing", "Intrusive"]
        csip_bar_graphs(my_path, pdf, data['RadarRSSM'], barTitles, csipTitles)


        #Personal Goals and Standards
        goalTitles = ["Goal Thinking", "Goal Satisfaction", "Goal Self-Efficacy", "Goal Intrinsic Motivation", "Goal Approach Orientation", "Goal Growth Mindset", "Goal Level of Conflict"]

        standardTitles = ["Moral Standard Thinking", "Moral Standard Satisfaction", "Moral Standard Self-Efficacy", "Moral Standard Intrinsic Motivation", "Moral Standard Approach Orientation",
                        "Moral Standard Growth Mindset", "Moral Standard Level of Conflict"]
        #Personal Goals and Standards
        print('----------------------------------------')
        print('Added Goal Graphs')
        # begin adding goals section of the pdf
        goals_bar_graphs(my_path, pdf, data['Goals'], data['GoalDescription'], goalTitles)

        # Comparison figure----Personal Values
        print('----------------------------------------')
        print('Added Comparison Figure')
        PDF_Generator.comparison_figure(pdf, my_path, data['Comparison'], data['GoalDescription'])

       
        #Self-Concept: Psychological Needs
        #print('----------------------------------------')
        #print('Added RSSM Graphs')
        #rssmTitles = ["Relatedness Satisfaction", "Control Satisfaction", "Self-Esteem Frustration", "Autonomy Frustration"]
        #barTitles = [f'Self-with-{v}' if v != 'Overall' else v for k,v in data['RSSMNames'].items()]
        #rssm_bar_graphs(my_path, pdf, data['RSSM'], barTitles, rssmTitles)

        ''' #TODO: fix issues with fig.savefig(path + "/images/radar.png", transparent=False)
        print('----------------------------------------')
        print('Added Radar Plot')
        # add page and begin adding the radar plot
        pdf.add_page()
        PDF_Generator.section_headers(pdf, 'Relational Schema Interpersonal Behavior Scale')
        Graph_Generator.create_radar(pdf, my_path, data['RadarRSSM'], data['RadarRSSMName']) # TODO: last 2 parameters need to be the vector values from pandas df
        '''
        #Temperament
        #print('----------------------------------------')
        #print('Added Temperament Graph')
        #stuff = [list(data['Temperament'].values()), list(data['Temperament'].keys())]
        #temperament_graph(my_path, pdf, stuff, "Temperament")

        #Self-Concept: Problematic Interpersonal Styles
        #print('----------------------------------------')
        #print('Added CSIP Graph')
        #csipTitles = ["Domineering", "Self-Centered", "Distant/Cold", "Socially Inhibited", "Nonassertive", "Exploitable", "Self-Sacrificing", "Intrusive"]
        #csip_bar_graphs(my_path, pdf, data['RadarRSSM'], barTitles, csipTitles)

        #Self-Concept: Rejection Sensitivity
        #print('----------------------------------------')
        #print('Added Rejection Sensitivity')
        #rs_page(pdf, data['RejectionSensitivity'])

        print('----------------------------------------')
        print('Added sorting of results')
        order = ""
        order = Results_Sorted.get_sort(data)
        PDF_Generator.add_sort(pdf, order)

        print('----------------------------------------')
        print('PDF Saved')
        pdf.output('Personalized_report.pdf', 'F')


        print('----------------------------------------')
        user_email = data['Personal']['Email']
        print(user_email)
        #send_mail(user_email)
        print('----------------------------------------')

        #send_mail('walter.scott@wsu.edu')
        send_mail('aquamarinefox.365@gmail.com')
        #send_mail('belinda.lin@wsu.edu')
        plt.close('all')


def title_page(my_path, pdf, info):
    pdf.add_page()
    pdf.image(my_path + "/images/wsu_banner.png", 0, 0, WIDTH)
    #pdf.image(my_path + "/images/Washington-State-University-logo.png", 0, HEIGHT/2 - 100, WIDTH)
    pdf.image(my_path + "/images/buffer.png", 0, HEIGHT/2 + 1, WIDTH)
    PDF_Generator.add_name(pdf, 'For: {}'.format(info['First']))
    # pdf.image(my_path + "/images/cover_page.png", 0, 50, WIDTH)


def rs_page(pdf, rs):
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    total = "Self-Concept: Rejection Sensitivity: " + str(round(rs, 2))

    if rs <= 1.39:
        total += " (Very Low)"
    elif rs <= 5:
        total += " (Low)"
    elif rs <= 6.805:
        total += " (Moderately Low)"
    elif rs <= 10.415:
        total += " (Average)"
    elif rs <= 12.22:
        total += " (Moderately High)"
    elif rs <= 15.85:
        total += " (High)"
    else:
        total += " (Very High)"

    pdf.text(x=20, y=20, txt=total)



def generate_goal_feedback(scores, labels, current_title, is_overall=False):
    # Define explanation feedback for different titles
    feedback_templates = {
        "Goal Thinking": {
        "high": "Your level of thinking about your goals is high, indicating their importance to you and your commitment to achieving them.",
        "average": "Your thinking about your goals is average, suggesting it might be beneficial to focus more on them to enhance motivation.",
        "low": "Your thinking about your goals is low, which may reduce motivation and commitment. Consider strategies to increase your awareness and focus."
        },
        "Goal Satisfaction": {
        "high": "Your satisfaction with your goals is high, showing that you are pleased with your progress and motivated to continue.",
        "average": "Your goal satisfaction is average, suggesting you may benefit from taking small steps to boost your sense of progress.",
        "low": "Your satisfaction with your goals is low, indicating potential frustration. Taking small, actionable steps may help increase satisfaction and motivation."
        },
        "Goal Self-Efficacy": {
        "high": "Your confidence in achieving your goals is high, reflecting strong self-belief in your abilities.",
        "average": "Your confidence in your ability to achieve your goals is moderate. Building more confidence could enhance motivation.",
        "low": "Your confidence is low, potentially impacting your motivation and persistence. Developing strategies to build self-efficacy may help you overcome challenges."
        },
        "Goal Intrinsic Motivation": {
        "high": "Your goals are intrinsically motivated, driven by personal values and interests.",
        "average": "Your motivation is balanced between intrinsic and extrinsic factors, or unclear. Clarifying your motivations could enhance focus.",
        "low": "Your goals are mainly extrinsically motivated, driven by external reasons. Reconnecting with personal interests may help make goal pursuit more rewarding."
        },
        "Goal Approach Orientation": {
        "high": "Your approach to your goals is proactive and positive, focusing on what you want to achieve.",
        "average": "Your approach orientation is moderate, indicating room to reframe goals more positively as approach goals.",
        "low": "Your approach to goals is avoidance-based, which may not be optimal. Reframing goals as approach-oriented can enhance motivation."
        },
        "Goal Growth Mindset": {
        "high": "Your goals reflect a strong growth mindset, valuing learning and improvement.",
        "average": "Your mindset is neutral, suggesting that emphasizing growth and adaptability could enhance progress.",
        "low": "Your mindset leans toward performance, focusing on proving ability. Shifting to a growth perspective could foster learning and resilience."
        },
        "Goal Level of Conflict": {
        "high": "Your goals are conflicted, suggesting that progress on one may hinder others.",
        "average": "Your goals show moderate conflict, where progress on one neither significantly helps nor hinders others.",
        "low": "Your goals are aligned, indicating that progress on one goal supports progress on others."
    }
    }
    # Choose the right feedback template
    feedback = f"{current_title}:\n"
    template = feedback_templates.get(current_title, None)

    if not template:
        return feedback  # If no suitable template is found, an empty response is returned.

    # If it is the Overall score, generate explanatory feedback
    if is_overall:
        score = float(scores[0])  # Assume the first one is the Overall score
        score = round(score, 2) # round to two places
        if score >= 6.0:
            feedback += f"Overall score is {score} (very high):\n{template['high']}\n"
        elif score >= 5.0:
            feedback += f"Overall score is {score} (high):\n{template['high']}\n"
        elif score >= 3.0:
            feedback += f"Overall score is {score} (average):\n{template['average']}\n"
        elif score >= 2.0:
            feedback += f"Overall score is {score} (low):\n{template['low']}\n"
        else:
            feedback += f"Overall score is {score} (very low):\n{template['low']}\n"

    # List Individual scores without explanation
    for i, score in enumerate(scores[1:], start=1):  # Skip the first one (Overall)
        label = labels[i]
        feedback += f"{label} score is {float(score)}\n"

    return feedback


# function to complete the goals section of bar graphs and text boxes
def goals_bar_graphs(my_path, pdf, data, descriptions, titles):
    pdf.add_page()
    PDF_Generator.section_headers(pdf, 'Personal Goals and Standards')
    PDF_Generator.print_textboxes(pdf, "Goal", descriptions, 4)

    counter = 0
    # Create a dictionary mapping keys to titles
    title_map = {
        "GoalThink": "Goal Thinking",
        "GoalSatis": "Goal Satisfaction",
        "GoalEfficacy": "Goal Self-Efficacy",
        "GoalIntrinsic": "Goal Intrinsic Motivation",
        "GoalApproach": "Goal Approach Orientation",
        "GoalGrowth": "Goal Growth Mindset",
        "GoalConflict": "Goal Level of Conflict"
    }

    # loop through all the items in the dictionary
    for key, value in data.items():

        if len(value) == 4:
            labels = ["Goal 1", "Goal 2", "Goal 3", "Goal 4"]
        else:
            labels = ["Overall", "Goal 1", "Goal 2", "Goal 3", "Goal 4"]

        # Setting the is_overall variable
        is_overall = labels[0] == "Overall"

        if key[4:] == 'Conflict' or key[4:] == 'Growth':
            holder = 'Goal_{}'.format(key[4:])
        else:
            holder = key[4:]

        # Get the current title according to key
        current_title = title_map.get(key, "Goal")  # If no match is found, the default title is used.

        # Create and print graphs and explanatory feedback
        if counter != 0:
            Graph_Generator.create_bargraph(pdf, my_path, counter*96, value, labels, key, titles.pop(0))
            
            # Add explanatory feedback
            feedback = generate_goal_feedback(value, labels, current_title, is_overall)
            # pdf.set_font("Arial", "", 10)
            # pdf.ln(5)
            # pdf.multi_cell(0, 5, feedback, border=0, align="L")
            PDF_Generator.print_feedback_box(pdf, feedback, x=10, w=75, main_font_size=10, detail_font_size=8)   # Print feedback box, set font size separately

            pdf.image(my_path + "/images/{}_Scaling.png".format(holder), 100, counter*96+86, WIDTH/2)
            counter += 1
        else:
            Graph_Generator.create_bargraph(pdf, my_path, 8, value, labels, key, titles.pop(0))
            
            # Add explanatory feedback
            feedback = generate_goal_feedback(value, labels, current_title, is_overall)
            # Print feedback box and set font size separately
            PDF_Generator.print_feedback_box(pdf, feedback, x=10, w=75, main_font_size=10, detail_font_size=8)   
            pdf.image(my_path + "/images/{}_Scaling.png".format(holder), 100, 94, WIDTH/2)
            counter += 1

        # When the counter is 2, add a new page
        if counter == 2:
            pdf.add_page()
            PDF_Generator.section_headers(pdf, 'Personal Goals and Standards')
            PDF_Generator.print_textboxes(pdf, "Goal", descriptions, 4)
            counter = 0


# Create and add the text boxes and graphs for the standard graphs
def standard_bar_graphs(my_path, pdf, data, descriptions, titles):
    pdf.add_page()
    PDF_Generator.section_headers(pdf, 'Personal Moral Standards')
    counter = 0
    # loop through all the items in the dictionary
    for key, value in data.items():
        if len(value) == 4:
            labels = ["Moral\nStandard 1", "Moral\nStandard 2", "Moral\nStandard 3", "Moral\nStandard 4"]
        else:
            labels = ["Overall","Moral\nStandard 1", "Moral\nStandard 2", "Moral\nStandard 3", "Moral\nStandard 4"]

        if key[8:] == 'Conflict' or key[8:] == 'Growth':
            holder = 'Moral_{}'.format(key[8:])
        else:
            holder = key[8:]

        # If counter == 2 we need to create a new page
        if counter == 2:
            Graph_Generator.create_bargraph(pdf, my_path, counter*96, value, labels, key, titles.pop(0))
            PDF_Generator.print_textboxes(pdf, "Moral Standard", descriptions, 4)
            pdf.image(my_path + "/images/{}_Scaling.png".format(holder), 100, counter*96+86, WIDTH/2)
            pdf.add_page()
            PDF_Generator.section_headers(pdf, 'Personal Moral Standards')
            counter = 0
        else:
            if counter != 0:
                Graph_Generator.create_bargraph(pdf, my_path, counter*96, value, labels, key, titles.pop(0))
                pdf.image(my_path + "/images/{}_Scaling.png".format(holder), 100, counter*96+86, WIDTH/2)
                counter += 1
            else:
                Graph_Generator.create_bargraph(pdf, my_path, 8, value, labels, key, titles.pop(0))
                pdf.image(my_path + "/images/{}_Scaling.png".format(holder), 100, 94, WIDTH/2)
                counter += 1

    # if counter != 0 then we add new text boxes
    if counter != 0:
        PDF_Generator.print_textboxes(pdf, "Moral Standard", descriptions, 4)


def generate_rssm_feedback(scores, labels, current_title, is_overall=False):
    #Defining an explanatory feedback template
    feedback_templates = {
        "Relatedness Satisfaction": {
            "high": "Your relatedness satisfaction is high, This suggests that you experience some features of a positive self-concept.  More specifically, this suggests that in general you experience high levels of being connected to, close to, and accepted by the people you most interact with or think about. ",
            "average": "Your relatedness satisfaction is average, This suggests that although you do not necessarily experience disconnection or rejection from the people you most interact with or think about, you also do not experience an optimal level of connectedness, relatedness, or acceptance. ",
            "low": "Your relatedness satisfaction is low, This suggests that you experience some features of a negative self-concept.  Specifically, you experience a self that is disconnected from, not close to, and/or rejected by the people you most interact with and/or think about. "
        },
        "Control Satisfaction": {
            "high": "Your control satisfaction is high, This suggests that you experience some features of a positive self-concept.  More specifically, this suggests that in general you experience a self that is in control, engaged, and capable and skilled.  Some research suggests that feeling in control, engaged, and capable is a basic psychological need. Your score indicates that this need is being met. The self tends to experience flow, an optimal state of control, when it is engaged in challenging activities for which there are learned and developed skills and abilities.  It appears you have developed skills and abilities that empower your sense of self.",
            "average": "Your control satisfaction is average, This suggests that although you do not necessarily experience low control, engagement, or capability with others, you also do not experience an optimal level of control and engagement.",
            "low": "Your control satisfaction is low, This suggests that you experience some features of a negative self-concept when interacting or thinking about this person.  More specifically, this suggests that in general you do not experience a self that is in control, engaged, and capable and skilled."
        },
        "Self-Esteem Frustration": {
            "high": "Your frustration with self-esteem is high, This suggests that you possess some features of a negative self-concept.  More specifically, this suggests that in general you experience a self that is low in self-esteem. Our self-esteem reflects both our levels of feeling accepted by others and feeling competent. The two go hand-in-hand in contributing to our self-esteem. This is likely because the experience of acceptance leads us to validate our own personal competence, qualities, and abilities.Some research suggests that feeling a high sense of self-esteem is a basic psychological need. Your score indicates that this need is not being met.",
            "average": "Your self-esteem frustration is average, This suggests that in general you experience average levels of self-esteem.  Our self-esteem reflects both our levels of feeling accepted by others and feeling competent. The two go hand-in-hand in contributing to our self-esteem. This is likely because the experience of acceptance leads us to validate our own personal competence, qualities, and abilities.",
            "low": "Your self-esteem frustration is low, This suggests that in general your needs for self-esteem are being adequately met and you do not experience self-esteem frustration."
        },
        "Autonomy Frustration": {
            "high": "Your autonomy frustration is high, This suggests that you possess some features of a negative self-concept.  More specifically, your score suggests that you often feel as if your actions are externally controlled, coerced or pressured by others, and that you are doing things out of a sense of obligation. ",
            "average": "This suggests that although you do not experience a high level of autonomy frustration, you also do not experience an optimal level of autonomy.  More specifically, your score suggests that you sometimes feel as if your actions are externally controlled, coerced or pressured by others, and that you are doing things out of a sense of obligation. ",
            "low": "Your score suggests that in general you do not experience high autonomy frustration, or that your actions are being controlled, coerced or pressured by others, that you are doing things out of a sense of obligation. "
        }
    }

    # Choose the right feedback template
    feedback = f"{current_title}:\n"
    template = feedback_templates.get(current_title, None)

    if not template:
        return feedback  # If no suitable template is found, an empty response is returned.

    # If it is the Overall score, generate explanatory feedback
    if is_overall:
        score = float(scores[0])  # Assume the first one is the Overall score
        score = round(score, 2) # round the score to two decimal places
        if score >= 4.5:
            feedback += f"Overall score is {score} (very high):\n{template['high']}\n"
        elif score >= 4.0:
            feedback += f"Overall score is {score} (high):\n{template['high']}\n"
        elif score >= 3.5:
            feedback += f"Overall score is {score} (high average):\n{template['high']}\n"
        elif score >= 2.5:
            feedback += f"Overall score is {score} (average):\n{template['average']}\n"
        elif score >= 1.5:
            feedback += f"Overall score is {score} (low average):\n{template['low']}\n"
        elif score >= 1.0:
            feedback += f"Overall score is {score} (low):\n{template['low']}\n"
        else:
            feedback += f"Overall score is {score} (very low):\n{template['low']}\n"

    # List Individual scores without explanation
    for i, score in enumerate(scores[1:], start=1):  # Skip the first one (Overall)
        label = labels[i]
        feedback += f"{label} score is {float(score)}\n"

    return feedback



# Create and add rssm bar graphs
def rssm_bar_graphs(my_path, pdf, data, names, titles):
    initial_y_position = 30  # Sets the initial Y position of the box, used to standardize the start position of each page
    pdf.add_page()
    PDF_Generator.section_headers(pdf, 'Relational Schema Psychological Need Scale')
    
    counter = 0

    y_position = initial_y_position  # Boxes on each page start at the same Y position

    #Create a dictionary mapping keys to titles
    title_map = {
    "RssmRelateSatis": "Relatedness Satisfaction",
    "RssmControlSatis": "Control Satisfaction",
    "RssmEsteemFrus": "Self-Esteem Frustration",
    "RssmAutoFrus": "Autonomy Frustration"
}

    for key, value in data.items():
        current_title = title_map.get(key, "RSSM Scale")  # The default title is "RSSM Scale"
        
        labels = names
        
        #Add explanatory feedback
        feedback = generate_rssm_feedback(value, labels, current_title, is_overall=True)
        
        # Print feedback box and set position dynamically
        PDF_Generator.print_feedback_box(pdf, feedback, x=10, y=y_position, w=75, main_font_size=10, detail_font_size=8)
        y_position = pdf.get_y() + 15  # Update the Y position to make room for the next box


        # Create and print a chart
        if counter != 0:
            Graph_Generator.create_rssm_bargraph(pdf, my_path, (counter * 96), value, names, key, titles.pop(0))
            pdf.image(my_path + "/images/RSSM_Scaling.png", 118, counter * 96 + 86, WIDTH / 2 - 20)
            counter += 1
        else:
            Graph_Generator.create_rssm_bargraph(pdf, my_path, 8, value, names, key, titles.pop(0))
            pdf.image(my_path + "/images/RSSM_Scaling.png", 118, 94, WIDTH / 2 - 20)
            counter += 1

        
        if counter == 2:
            counter = 0  
            if key != list(data.keys())[-1]:  # Check if it is the last element
                pdf.add_page()
                PDF_Generator.section_headers(pdf, 'Relational Schema Psychological Need Scale')
                y_position = initial_y_position  # Reset Y position to keep the new page consistent



def generate_csip_feedback(scores, labels, current_title, is_overall=False):
    # Define explanatory feedback templates with different titles
    feedback_templates = {
        "Domineering": {
            "description": "An interpersonal style in which one is too controlling, manipulating, bossy, argumentative, and/or is acting too superior/condescending when relating to others.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Self-Centered": {
            "description": "An interpersonal style in which one is too insensitive to others needs, thoughts, feelings, has difficulty providing emotional support, liking others and getting along.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Distant/Cold": {
            "description": "An interpersonal style in which one is uncomfortable with being close or intimate, has difficulty fully connecting and enjoying others company.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Socially Inhibited": {
            "description": "A problematic interpersonal style in which one is anxious and shy around others, unable to be themselves and has difficulty fitting in.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Nonassertive": {
            "description": "A problematic interpersonal style in which one tends to be too compromising, and is too easily taken advantage of, acting overly submissive, letting others boss them around too much.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Exploitable": {
            "description": "A problematic interpersonal style in which one has trouble being assertive and taking the lead, tends to feel weak and insecure and easily embarrassed around others.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Self-Sacrificing": {
            "description": "A problematic interpersonal style in which one is too giving, tending to put others' needs before their own, being easily affected by others' pain and suffering, and being too trusting.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        },
        "Intrusive": {
            "description": "A problematic interpersonal style in which one has trouble respecting others' privacy, talks too much, is overly affectionate, and/or needs to be the center of attention.",
            "problem_levels": [
                (0.49, "not a problem for you"),
                (1.49, "a minor problem for you"),
                (2.49, "a moderate problem for you"),
                (3.00, "a serious problem for you")
            ]
        }
    }

    feedback = f"{current_title}:\n"
    template = feedback_templates.get(current_title, None)

    if not template:
        return feedback  # If no suitable template is found, return empty feedback

    # If it is the Overall score, generate explanatory feedback
    if is_overall:
        score = float(scores[0])  # Assume the first one is the Overall score
        score = round(score, 2) # round the decimal to two places
        problem_level_text = "not a problem"
        for threshold, text in template['problem_levels']:
            if score <= threshold:
                problem_level_text = text
                break
        feedback += f"Overall score is {score} ({problem_level_text}):\n{template['description']}\n"

    # List Individual scores without explanation
    for i, score in enumerate(scores[1:], start=1):
        label = labels[i]
        score = round(float(score), 2) # round to two decimal places
        feedback += f"{label} score is {score}\n"

    return feedback


# Create and add rssm bar graphs
def csip_bar_graphs(my_path, pdf, data, names, titles):
    pdf.add_page()
    PDF_Generator.section_headers(pdf, 'Self Concept: Problematic Interpersonal Styles')
    
    counter = 0
    initial_y_position = 30  # Sets the initial Y position of the box, used to standardize the start position of each page
    y_position = initial_y_position  # Boxes on each page start at the same Y position
    # Delete irrelevant data
    dataCopy = data.copy()
    dataCopy.pop('RadarRSSMName', None)
    dataCopy.pop('RSSM_YVector', None)
    dataCopy.pop('RSSM_XVector', None)
    
    # Iterate over each item in the data dictionary
    for key, value in dataCopy.items():
        current_title = titles.pop(0)  # Get the current title
        
        labels = names
        
        # Generate and print feedback
        feedback = generate_csip_feedback(value, labels, current_title, is_overall=True)
        PDF_Generator.print_feedback_box(pdf, feedback, x=10, y=y_position, w=75, main_font_size=10, detail_font_size=8)
        y_position = pdf.get_y() + 15  # Update the Y position to make space for the next box

        # Create and print a chart
        if counter != 0:
            Graph_Generator.create_csip_bargraph(pdf, my_path, (counter * 96), value, names, key, current_title)
            pdf.image(my_path + "/images/RSSM_Scaling.png", 118, counter * 96 + 86, WIDTH / 2 - 20)
            counter += 1
        else:
            Graph_Generator.create_csip_bargraph(pdf, my_path, 8, value, names, key, current_title)
            pdf.image(my_path + "/images/RSSM_Scaling.png", 118, 94, WIDTH / 2 - 20)
            counter += 1

        # If the count reaches 2, add a new page and reset the counter
        if counter == 2:
            counter = 0  
            if key != list(dataCopy.keys())[-1]:  # Check if it is the last element
                pdf.add_page()
                PDF_Generator.section_headers(pdf, 'Self Concept: Problematic Interpersonal Styles')
                y_position = initial_y_position  # Reset Y position to keep the new page consistent

# Function to generate temperament feedback
def generate_temperament_feedback(scores, labels):
    feedback_templates = {
        "BIS": {
            "very_high": "Your score suggests that you may be someone who is more sensitive to situations that are unfamiliar, threatening, or challenging. In these situations, you may have more reactivity in emotional parts of the brain, particularly the amygdala, and may experience greater physiological reactivity. Research has found that infants with high behavioral inhibition temperaments are more likely to develop into 'shy' children. Not all infants with high behavioral inhibition stay 'shy' as your experiences and environment can influence how temperament develops. Importantly, people with high behavioral inhibition temperaments do not experience anxiety unless they experience unfamiliar, challenging or threatening situations. In situations that are familiar, non-challenging, or non-threatening, people with high behavioral inhibition are no more anxious than other people.",
            "average": "Your score suggests that when exposed to situations that are novel, unfamiliar, or threatening, you are generally no more and no less sensitive to these types of situations as is the typical person. If you also scored approximately in the average range on behavioral activation system temperament, this would suggest that you possess an even-keeled, emotionally stable temperament.",
            "low": "Your score suggests that you may be less sensitive to situations that are unfamiliar, threatening, or challenging. In these situations, you may have less reactivity in emotional parts of the brain, particularly the amygdala, and may experience less anxiety and less physiological reactivity. Research has found that infants with high behavioral inhibition temperaments are more likely to develop into 'shy' children. Your score suggests that it is unlikely that you were shy as a child, although factors other than temperament can influence shyness."
        },
        "BAS": {
            "very_high": "Your score in the (very high, high) range. This suggests that you may be more sensitive to situations where there are rewards, things that are attractive, things you want. In these situations, you may have more reactivity in reward systems of the brain that involve the orbitofrontal cortex, the nucleus accumbens, and amygdala, leading you to experience more excitement, more enthusiasm, to approach and get these things that you want. Research has found that people with high behavioral approach temperaments experience positive affect more easily and also learn faster in learning conditioning studies where there are rewards.",
            "average": "Your score in the average range. This suggests that you are fairly typical in your sensitivity to situations where there are rewards, things that are attractive, things you want. In these situations, your reactivity in reward systems of the brain that involve the orbitofrontal cortex, the nucleus accumbens, and amygdala is no more, and no less, reactive than the average person. Similarly, you are likely to experience the amount of excitement and enthusiasm to approach and get these things that you want as the typical person. On the plus side, you are likely to be someone who is even-keeled, emotionally stable, and unlikely to be too impulsive.",
            "low": "Your score in the (very low, low) range. This suggests that you may be less sensitive to situations where there are rewards, things that are attractive, things you want. In these situations, you may have less reactivity in reward systems of the brain that involve the orbitofrontal cortex, the nucleus accumbens, and amygdala, and you may experience less excitement, less enthusiasm, to approach and get these things that you want."
        },
        "BAS-D": {
            "very_high": "Your score in the (very high, high) range. This suggests that you tend to be very motivated to pursue the goals you have, and are quick to act on and move towards your goals, as well as being persistent in achieving them.",
            "average": "Your score in the average range. This suggests that you are fairly typical in your tendency to be motivated to pursue goals you have, neither quick or slow to act on and move towards your goals, or persistent or non-persistent in achieving them.",
            "low": "Your score in the (very low, low) range. This suggests that you may not be very motivated to pursue goals you have, nor quick to act on and move towards your goals, or persistent in achieving them."
        },
        "BAS-FS": {
            "very_high": "Your score in the (very high, high) range. This suggests that you tend to crave excitement, and are very motivated and quick to pursue new rewards or things you think might be fun or exciting on the spur of the moment.",
            "average": "Your score in the average range. This suggests that you are fairly typical in your tendency to be motivated to pursue excitement, fun, new rewards on the spur of the moment.",
            "low": "Your score in the (very low, low) range. This suggests that you are not very motivated to pursue excitement, fun, new rewards on the spur of the moment."
        },
        "BAS-R": {
            "very_high": "Your score in the (very high, high) range. This suggests that you experience a high degree of enthusiasm, excitement, and positive emotions when a positive outcome/reward has occurred or when you anticipate a positive outcome/reward to occur.",
            "average": "Your score in the average range. This suggests that you experience a typical amount of enthusiasm, excitement, and positive emotions when a positive outcome/reward has occurred or when you anticipate a positive outcome/reward to occur.",
            "low": "Your score in the (very low, low) range. This suggests that you not experience a typical level of enthusiasm, excitement, and positive emotions when a positive outcome/reward has occurred or when you anticipate a positive outcome/reward to occur."
        }
    }

    feedback = ""
    for i, score in enumerate(scores):
        label = labels[i]
        template = feedback_templates.get(label)
        
        if not template:
            continue  

        if score >= 3.5:
            level = "very_high"
        elif score >= 2.75:
            level = "very_high" 
        elif score >= 2.25:
            level = "average"
        elif score >= 1.5:
            level = "low"
        else:
            level = "low"
        
        feedback += f"{label}: {round(score, 2)} ({level.replace('_', ' ')})\n{template[level]}\n\n"

    return feedback


# Create and add temperament bar graph
def temperament_graph(my_path, pdf, data, title):
    pdf.add_page()
    
    # Create a chart
    Graph_Generator.temperament_bargraph(my_path, pdf, data[0], data[1], title)
    PDF_Generator.temperament_scaling(pdf)
    
    #Get the current Y position to ensure feedback is printed below the graph
    current_y = pdf.get_y()
    
    # Set the feedback box position below the chart, leaving enough space
    feedback_y_position = current_y + 130  # Change the spacing size
    pdf.set_y(feedback_y_position)
    
    # Generate and print feedback
    labels = ["BIS", "BAS", "BAS-D", "BAS-FS", "BAS-R"]
    scores = [float(score) for score in data[0]]  # Assume data[0] is a list of scores
    feedback = generate_temperament_feedback(scores, labels)
    
    # Print feedback to PDF
    PDF_Generator.print_feedback_box_horizontal(pdf, feedback, x=10, w=180, main_font_size=10, detail_font_size=8)
   

def send_mail(receiver_address):
    sender_address = 'teambluebirds2023@gmail.com'
    sender_pass = 'zgfuoltymavvcskq'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Your personal assessment feedback report'
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'Personalized_report.pdf'
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream', Name=attach_file_name)
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

main = create_report()