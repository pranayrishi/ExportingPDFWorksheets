from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors


# Function to create PDF from text input
def create_pdf(text_input, filename="worksheet.pdf"):
    # Create a canvas object with A4 page size
    pdf = canvas.Canvas(filename, pagesize=A4)

    # Set font and size
    pdf.setFont("Helvetica", 12)

    # Define margin and starting position
    width, height = A4
    x_margin, y_margin = 40, 800  # Starting x and y positions

    # Split the input text by lines (optional: customize formatting)
    text_lines = text_input.split('\n')

    # Loop through lines and draw them on the PDF
    for line in text_lines:
        if y_margin < 50:  # Check if you need a new page
            pdf.showPage()  # Create a new page
            pdf.setFont("Helvetica", 12)
            y_margin = 800

        # Draw text at the current position
        pdf.drawString(x_margin, y_margin, line)

        # Move the y position down for the next line
        y_margin -= 20

    # Save the PDF
    pdf.save()


# Example input text for a worksheet
text_input = """
Math Worksheet

1. Solve the following equations:
   a) 5x + 7 = 22
   b) 3y - 4 = 11

2. Write a short essay on 'The Importance of AI in Education'.

3. Fill in the blanks:
   a) The capital of France is ________.
   b) The formula for the area of a circle is ________.
"""

# Create the PDF
create_pdf(text_input)
print("PDF created successfully!")
