from fpdf import FPDF
import datetime
WIDTH = 210
HEIGHT = 297


def print_textboxes(pdf, value, descriptions, size):
    pdf.set_font("Arial", "", 10)
    pdf.ln(11)
    lineholder = 11
    d = "I wandered lonely as a phone\nThat floats on high o'er vales and hills,\nWhen all at once I saw a crowd,\nA host, of golden daffodils\nBeside the lake, beneath the trees,\nFluttering and dancing in the breeze."
    for x in range(size):
        pdf.multi_cell(w=75,h=5,txt="{} {}:\n{}".format(value, x+1, descriptions[x]), border = 1, align="L")
        lineholder += 72
        pdf.set_y(lineholder)

def add_name(pdf, name):
    pdf.set_font('Arial', 'B', 30)
    pdf.ln(50)
    pdf.cell(0, 10, "Person-In-Context: A Personality", 0, 0, 'C')
    pdf.ln(15)
    pdf.cell(0, 10, "Assessment of Temperament,", 0, 0, 'C')
    pdf.ln(15)
    pdf.cell(0, 10, "Self-Schemas, Personal Goals,", 0, 0, 'C')
    pdf.ln(15)
    pdf.cell(0, 10, "and Standards", 0, 0, 'C')
    pdf.set_font('Arial', 'B', 24)
    pdf.ln(30)
    pdf.cell(0, 10, name, 0, 0, 'C')
    pdf.ln(15)
    today = datetime.date.today()
    d = today.strftime("%B %d, %Y")
    dr = "Date of Report: %s" % (d)
    pdf.cell(0, 10, dr, 0, 0, 'C')

def section_headers(pdf, text):
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 0, text, 0, 0, 'C')
    #pdf.text(x=WIDTH/2, y=14, txt=text)

def temperament_scaling(pdf):
    pdf.set_font('Arial', "", 10)
    pdf.text(x=5, y=36, txt="Very High")
    pdf.text(x=5, y=61, txt="High Average")
    pdf.text(x=5, y=85, txt="Low Average")
    pdf.text(x=5, y=109, txt="Very Low")

# Comparison figure
def comparison_figure(pdf, path, ranks, goals):
    pdf.add_page()
    pdf.image(path + "/images/Comparison.png", x=0, y=0, w=WIDTH+5, h=170) #(HEIGHT/2)+30
    pdf.image(path + "/images/Comparison.png", x=0, y=(HEIGHT/2), w=WIDTH+5, h=170) #(HEIGHT/2)+30
    pdf.image(path + "/images/Arrow.png", x=(WIDTH/2)-47, y=(HEIGHT/2)-42, w=100, h=100)
    pdf.image(path + "/images/Single_Arrow.png", x=0, y=(HEIGHT/2)+18, w=75, h=110)

    # Change font and add titles
    pdf.set_font('Arial', '', 16)
    pdf.text(x=48, y=14, txt="Most Important Goals and Ranking of Values:")
    pdf.text(x=57, y=20, txt="Do Your Goals Reflect Your Values?")
    pdf.text(x=70, y=43, txt="Your 4 Most Important Goals:")
    pdf.text(x=76, y=(HEIGHT/2)+43, txt="Your Ranking of Values:")
    pdf.set_font('Arial', '', 14)
    pdf.text(x=36, y=(HEIGHT/2)+43, txt="Most")
    pdf.text(x=31, y=(HEIGHT/2)+47, txt="Important")
    pdf.text(x=36, y=(HEIGHT/2)+121, txt="Least")
    pdf.text(x=31, y=(HEIGHT/2)+125, txt="Important")


    # Format Rankings
    output = ""
    for item in ranks:
        output += f"{item}\n"

    # Adding text to the boxes
    pdf.set_font('Arial', '', 10)
    pdf.set_xy(x=30, y=50)
    pdf.multi_cell(w=150, h=18, txt="Goal 1: {}\nGoal 2: {}\nGoal 3: {}\nGoal 4: {}".format(goals[0], goals[1], goals[2], goals[3]), border=0)
    pdf.set_font('Arial', '', 11)
    pdf.set_xy(x=70, y=200)
    pdf.multi_cell(w=100, h=8, txt="{}".format(output[0:-1]), border=0)

def add_sort(pdf, order):
    pdf.add_page()
    count = 0
    lst = order.split("\n")
    yIdx = 25
    xIdx = 15
    pg = 0
    facet = True
    pdf.set_font('Arial', 'B', 20)
    pdf.text(x=25, y=15, txt="Treatment Recommendations: Facet Specific")

    for x in range(len(lst)):
        pg += 1
        if count == 0:
            pdf.set_font('Arial', 'B', 15)
            xIdx = 10
        else:
            pdf.set_font('Arial', '', 10)
            xIdx = 15
        pdf.text(x=xIdx, y=yIdx, txt=lst[x])
        yIdx+= 10
        count += 1
        if count == 4:
            count = 0
        if pg == 12 and facet == True:
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.text(x=25, y=15, txt="Treatment Recommendations: Situation Specific")
            pg = 0
            yIdx = 30
            facet = False
        elif pg == 24:
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.text(x=25, y=15, txt="Treatment Recommendations: Situation Specific")
            pg = 0
            yIdx = 30

