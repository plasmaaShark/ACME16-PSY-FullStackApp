from fpdf import FPDF
import datetime
WIDTH = 210
HEIGHT = 297


def print_textboxes(pdf, value, descriptions, size):
    pdf.set_font("Arial", "B", 10)
    pdf.ln(11)
    
    # Merge all text content
    combined_text = ""
    for x in range(size):
        combined_text += "{} {}:\n{}\n\n".format(value, x+1, descriptions[x])
    
    # Use a single multi_cell call to generate a large box containing all the content
    pdf.set_fill_color(211, 221, 235) # color in the box
    pdf.multi_cell(w=75, h=5, txt=combined_text, border=1, align="L", fill=1)

    pdf.set_font("Arial", "", 10) # reset font to not bold

# def print_feedback_box(pdf, feedback, x=10, y=None, w=75, main_font_size=10, detail_font_size=8):
#     # Print a feedback text box with a border in the PDF
#     if y is not None:
#         pdf.set_y(y)  # Set the y coordinate

#     start_x = pdf.get_x()  # Get the starting x coordinate
#     start_y = pdf.get_y()  # Get the starting y coordinate

#     feedback_lines = feedback.split('\n')
#     for line in feedback_lines:
#         pdf.multi_cell(w=w, h=6, txt=line, border=0, align="L")
#     # Calculate the height of the text box
#     end_y = pdf.get_y()
#     box_height = end_y - start_y

#     # Draw a border
#     pdf.rect(x, start_y, w, box_height)

# def print_feedback_box(pdf, feedback, x=10, y=None, w=75, main_font_size=10, detail_font_size=8):
#     # 打印无边框的反馈文本框
#     if y is not None:
#         pdf.set_y(y)  # 设置y坐标

#     start_x = pdf.get_x()  # 获取起始x坐标
#     start_y = pdf.get_y()  # 获取起始y坐标

#     feedback_lines = feedback.split('\n')
#     for line in feedback_lines:
#         if line.startswith("Your"):  # 检查是否为详细说明文本
#             pdf.set_font("Arial", "", detail_font_size)
#         else:
#             pdf.set_font("Arial", "", main_font_size)
        
#         # 取消边框并左对齐
#         pdf.multi_cell(w=w, h=5, txt=line, align="L") 
# def print_feedback_box(pdf, feedback, x=10, y=None, w=75, main_font_size=10, detail_font_size=8):
#     # 在PDF中打印无边框的反馈文本框
#     if y is not None:
#         pdf.set_y(y)  # 设置y坐标

#     start_x = pdf.get_x()  # 获取起始x坐标
#     start_y = pdf.get_y()  # 获取起始y坐标

#     feedback_lines = feedback.split('\n')
#     for line in feedback_lines:
#         if line.startswith("Your"):  # 检查详细解释文本
#             pdf.set_font("Arial", "", detail_font_size)
#         else:
#             pdf.set_font("Arial", "", main_font_size)
#         pdf.multi_cell(w=w, h=5, txt=line, border=0, align="L")  # 设置border=0去除边框
    
#     # 移除边框（已经设置border=0，完成此步骤）

def print_feedback_box(pdf, feedback, x=10, y=None, w=75, font_size=10):
    # 在PDF中打印无边框的反馈文本框
    if y is not None:
        pdf.set_y(y)  # 设置y坐标

    start_x = pdf.get_x()  # 获取起始x坐标
    start_y = pdf.get_y()  # 获取起始y坐标

    # 设置统一的字体和大小
    pdf.set_font("Arial", "", font_size)

    feedback_lines = feedback.split('\n')
    for line in feedback_lines:
        pdf.multi_cell(w=w, h=5, txt=line, border=0, align="L")  # 设置border=0去除边框




def print_feedback_box_horizontal(pdf, feedback, x=10, y=None, w=180, font_size=10):
    # Print horizontally aligned feedback text boxes in PDF
    if y is not None:
        pdf.set_y(y)  # Set the y coordinate

    pdf.set_x(x)  # Set the x coordinate
    pdf.set_font("Arial", "", font_size)  # Set font once, with the specified size

    feedback_lines = feedback.split('\n')
    
    # Print feedback text using multi_cell for automatic line wrapping, no border
    for line in feedback_lines:
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

def temperament_scaling(pdf, y_position):
    pdf.set_font('Arial', "", 10)
    base_y = y_position - 45  # Adjust as needed to position labels correctly
    pdf.text(x=5, y=base_y, txt="Very High")
    pdf.text(x=5, y=base_y + 22, txt="High Average")
    pdf.text(x=5, y=base_y + 44, txt="Low Average")
    pdf.text(x=5, y=base_y + 66, txt="Very Low")

# Comparison figure
def comparison_figure(pdf, path, ranks, goals):
    pdf.add_page()

    # Change font and add titles
    pdf.set_font('Arial', '', 16)
    pdf.text(x=48, y=14, txt="Most Important Goals and Ranking of Values:")
    pdf.text(x=57, y=20, txt="Do Your Goals Reflect Your Values?")

    # Add PERSONAL VALUES title in bold
    pdf.set_font("Arial", "B", 11)
    pdf.set_xy(10, 25) # changed to 25 from 35
    pdf.cell(0, 5, "Personal Values", ln=True, align="C")

    ps_text = ("The last personality component we assessed was your values. Your values refer to your beliefs about what you believe is important to living a good life. To measure your values, you ranked them in order of their importance to you in living a good life.")
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0,5, ps_text, border=0, align="L")
    pdf.ln(1)

    ps_text2 = ("Research suggests that is important to have personal goals that match your values. Think about whether the goals you are striving for reflect what you believe is most important to living well. If you have a number of values that you list as important for which you do not list any goals, this may indicate poor goal-value fit. If it is the case that you do not have goals for your most important values, you might consider developing a new goal for those values. Research has shown that having goals that match our values increases psychological well-being and motivation.")
    pdf.multi_cell(0, 5, ps_text2, border=0, align="L")
    pdf.ln(1)

    pdf.image(path + "/images/Comparison.png", x=0, y= + 40, w=WIDTH+5, h=180) #(HEIGHT/2)+30
    pdf.image(path + "/images/Comparison.png", x=0, y=(HEIGHT/2) + 15, w=WIDTH+5, h=170) #(HEIGHT/2)+30
    pdf.image(path + "/images/Arrow.png", x=(WIDTH/2)-40, y=(HEIGHT/2)+14, w=80, h=50)
    pdf.image(path + "/images/Single_Arrow.png", x=0, y=(HEIGHT/2)+32, w=75, h=110)

    pdf.text(x=75, y=75, txt="Your 4 Most Important Goals:")
    pdf.text(x=76, y=(HEIGHT/2)+54, txt="Your Ranking of Values:")
    pdf.set_font('Arial', '', 14)
    pdf.text(x=36, y=(HEIGHT/2)+43+13, txt="Most")
    pdf.text(x=31, y=(HEIGHT/2)+47+13, txt="Important")
    pdf.text(x=36, y=(HEIGHT/2)+121+13, txt="Least")
    pdf.text(x=31, y=(HEIGHT/2)+125+13, txt="Important")


    # Format Rankings
    output = ""
    for item in ranks:
        output += f"{item}\n"

    # Adding text to the boxes
    pdf.set_font('Arial', '', 10)
    pdf.set_xy(x=30, y=87)
    pdf.multi_cell(w=150, h=5, txt="Goal 1: {}\nGoal 2: {}\nGoal 3: {}\nGoal 4: {}".format(goals[0], goals[1], goals[2], goals[3]), border=0)
    pdf.set_font('Arial', '', 11)
    pdf.set_xy(x=70, y=203)
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