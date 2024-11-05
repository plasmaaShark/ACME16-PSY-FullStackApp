from fpdf import FPDF
import datetime
WIDTH = 210
HEIGHT = 297


def print_textboxes(pdf, value, descriptions, size):
    pdf.set_font("Arial", "", 10)
    pdf.ln(11)
    
    # Merge all text content
    combined_text = ""
    for x in range(size):
        combined_text += "{} {}:\n{}\n\n".format(value, x+1, descriptions[x])
    
    # Use a single multi_cell call to generate a large box containing all the content
    pdf.multi_cell(w=75, h=5, txt=combined_text, border=1, align="L")

def print_feedback_box(pdf, feedback, x=10, y=None, w=75, main_font_size=10, detail_font_size=8):
    # Print a feedback text box with a border in the PDF
    if y is not None:
        pdf.set_y(y)  # Set the y coordinate

    start_x = pdf.get_x()  # Get the starting x coordinate
    start_y = pdf.get_y()  # Get the starting y coordinate

    feedback_lines = feedback.split('\n')
    for line in feedback_lines:
        if line.startswith("Your"):  # Check for detailed explanatory text
            pdf.set_font("Arial", "", detail_font_size)
        else:
            pdf.set_font("Arial", "", main_font_size)
        pdf.multi_cell(w=w, h=5, txt=line, border=0, align="L")
    
    # Calculate the height of the text box
    end_y = pdf.get_y()
    box_height = end_y - start_y

    # Draw a border
    pdf.rect(x, start_y, w, box_height)

def print_feedback_box_horizontal(pdf, feedback, x=10, y=None, w=180, main_font_size=10, detail_font_size=8):
    #Print horizontally aligned feedback text boxes in PDF
    if y is not None:
        pdf.set_y(y)  # Set the y coordinate

    pdf.set_x(x)  # Set the x coordinate
    feedback_lines = feedback.split('\n')
    
    # Print feedback text, use multi_cell to achieve automatic line wrapping, no border
    for line in feedback_lines:
        if line.strip().startswith("Your"):  # Check if it is detailed explanation text
            pdf.set_font("Arial", "", detail_font_size)
        else:
            pdf.set_font("Arial", "", main_font_size)
        pdf.multi_cell(w=w, h=6, txt=line, border=0, align="L")

def add_name(pdf, name):
    pdf.set_font('Arial', 'B', 30)
    pdf.ln(50)
    pdf.cell(0, 10, "Person in Context Assessment:", 0, 0, 'C')
    pdf.ln(15)
    pdf.cell(0, 10, "A Personality Assessment of", 0, 0, 'C')
    pdf.ln(15)
    pdf.cell(0, 10, "Temperament, Self-Concept,", 0, 0, 'C')
    pdf.ln(15)
    pdf.cell(0, 10, "Personal Goals and Standards", 0, 0, 'C')
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
    pdf.image(path + "/images/Comparison.png", x=0, y=0, w=WIDTH+5, h=180) #(HEIGHT/2)+30
    pdf.image(path + "/images/Comparison.png", x=0, y=(HEIGHT/2), w=WIDTH+5, h=170) #(HEIGHT/2)+30
    pdf.image(path + "/images/Arrow.png", x=(WIDTH/2)-47, y=(HEIGHT/2)-42, w=100, h=100)
    pdf.image(path + "/images/Single_Arrow.png", x=0, y=(HEIGHT/2)+18, w=75, h=110)

    # Change font and add titles
    pdf.set_font('Arial', '', 16)
    pdf.text(x=48, y=14, txt="Most Important Goals and Ranking of Values:")
    pdf.text(x=57, y=20, txt="Do Your Goals Reflect Your Values?")
    pdf.text(x=70, y=30, txt="Your 4 Most Important Goals:")
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
    pdf.set_xy(x=30, y=45)
    pdf.multi_cell(w=150, h=5, txt="Goal 1: {}\nGoal 2: {}\nGoal 3: {}\nGoal 4: {}".format(goals[0], goals[1], goals[2], goals[3]), border=0)
    pdf.set_font('Arial', '', 11)
    pdf.set_xy(x=70, y=200)
    pdf.multi_cell(w=100, h=8, txt="{}".format(output[0:-1]), border=0)

def add_sort(pdf, order):
    pdf.add_page()
    count = 0

    pdf.set_font('Arial', 'B', 20)
    pdf.text(x=25, y=15, txt="Treatment Recommendations: Facet Specific")
    facet = [order[0], order[1], order[6]]
    xIdx = 15
    for i, f in enumerate(facet):
        z = f.split("\n")
        pdf.set_font('Arial', 'B', 15)
        pdf.text(x=xIdx, y=30, txt=z[0])
        z.pop(0)
        pdf.set_font('Arial', '', 10)
        pdf.text(x=xIdx, y=35, txt=z[0])
        z.pop(0)
        pdf.text(x=xIdx, y=40, txt=z[0])
        z.pop(0)

        if len(z) > 1:
            pdf.set_font('Arial', 'B', 12)
            pdf.text(x=xIdx, y=50, txt=z[0])
            z.pop(0)
            pdf.text(x=xIdx, y=55, txt=z[0])
            z.pop(0)
            yIdx = 60
            pdf.set_font('Arial', '', 10)
            for z1 in z:
                pdf.text(x=xIdx, y=yIdx, txt=z1)
                yIdx += 5

        if i == 0:
            xIdx += 55
        else:
            xIdx += 75

    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.text(x=25, y=15, txt="Treatment Recommendations: Situation Specific")
    facet = [order[2], order[3], order[4], order[5]]
    xIdx = 20
    yIdx = 30
    for i, f in enumerate(facet):
        z = f.split("\n")
        pdf.set_font('Arial', 'B', 15)
        pdf.text(x=xIdx, y=yIdx+5, txt=z[0])
        z.pop(0)
        pdf.set_font('Arial', '', 10)
        pdf.text(x=xIdx, y=yIdx+10, txt=z[0])
        z.pop(0)
        pdf.text(x=xIdx, y=yIdx+15, txt=z[0])
        z.pop(0)

        if len(z) > 1:
            pdf.set_font('Arial', 'B', 12)
            pdf.text(x=xIdx, y=yIdx+25, txt=z[0])
            z.pop(0)
            pdf.text(x=xIdx, y=yIdx+30, txt=z[0])
            z.pop(0)
            yIdx += 35
            pdf.set_font('Arial', '', 10)
            for z1 in z:
                pdf.text(x=xIdx, y=yIdx, txt=z1)
                yIdx += 5

        if i == 0 or i == 2:
            xIdx = 115
        if i == 1:
            xIdx = 20
        if i == 1 or i == 2:
            yIdx = 150
        if i == 0:
            yIdx = 30



    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.text(x=25, y=15, txt="Treatment Recommendations: Situation Specific")
    facet = [order[7], order[8], order[9], order[10]]
    xIdx = 20
    yIdx = 30
    for i, f in enumerate(facet):
        z = f.split("\n")
        pdf.set_font('Arial', 'B', 15)
        pdf.text(x=xIdx, y=yIdx+5, txt=z[0])
        z.pop(0)
        pdf.set_font('Arial', '', 10)
        pdf.text(x=xIdx, y=yIdx+10, txt=z[0])
        z.pop(0)
        pdf.text(x=xIdx, y=yIdx+15, txt=z[0])
        z.pop(0)

        if len(z) > 1:
            pdf.set_font('Arial', 'B', 12)
            pdf.text(x=xIdx, y=yIdx+25, txt=z[0])
            z.pop(0)
            pdf.text(x=xIdx, y=yIdx+30, txt=z[0])
            z.pop(0)
            yIdx += 35
            pdf.set_font('Arial', '', 10)
            for z1 in z:
                pdf.text(x=xIdx, y=yIdx, txt=z1)
                yIdx += 5

        if i == 0 or i == 2:
            xIdx = 115
        if i == 1:
            xIdx = 20
        if i == 1 or i == 2:
            yIdx = 150
        if i == 0:
            yIdx = 30