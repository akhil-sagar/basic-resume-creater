from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import tkinter as tk
from tkinter import filedialog

def create_template(name, title, address, email, phone, summary, experiences, education, skills, header_image_path):
    # Create a PDF buffer
    buffer = BytesIO()

    # Create a SimpleDocTemplate object
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create a list to hold the flowables (elements) of the PDF
    elements = []

    # header image
    header_image = Image(header_image_path, width=letter[0], height=120)
    elements.append(header_image)

    # Personal Information Section
    elements.append(Spacer(1, 24))
    elements.append(Paragraph(f"<b>{name}</b>", getSampleStyleSheet()['Heading1']))
    elements.append(Paragraph(title, getSampleStyleSheet()['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(address, getSampleStyleSheet()['Normal']))
    elements.append(Paragraph(f"Email: {email} | Phone: {phone}", getSampleStyleSheet()['Normal']))

    # Summary Section
    elements.append(Spacer(1, 24))
    elements.append(Paragraph("<u>Summary</u>", getSampleStyleSheet()['Heading1']))
    elements.append(Paragraph(summary, getSampleStyleSheet()['Normal']))

    # Experience Section
    elements.append(Spacer(1, 24))
    elements.append(Paragraph("<u>Experience</u>", getSampleStyleSheet()['Heading1']))
    elements.append(Paragraph(experiences, getSampleStyleSheet()['Normal']))
    elements.append(Spacer(1, 6))

    # Education Section
    elements.append(Spacer(1, 24))
    elements.append(Paragraph("<u>Education</u>", getSampleStyleSheet()['Heading1']))
    elements.append(Paragraph(education, getSampleStyleSheet()['Normal']))
    elements.append(Spacer(1, 6))

    # Skills Section
    elements.append(Spacer(1, 24))
    elements.append(Paragraph("<u>Skills</u>", getSampleStyleSheet()['Heading1']))
    skills_text = ", ".join(skills)
    elements.append(Paragraph(skills_text, getSampleStyleSheet()['Normal']))

    # Build the PDF document
    doc.build(elements)

    # Move the buffer cursor to the beginning
    buffer.seek(0)
    return buffer

def generate_resume():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Resume Generator")

    # Function to get user input and generate the resume
    def generate():
        # Get user input
        name = name_entry.get()
        title = title_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        summary = summary_text.get("1.0", tk.END).strip()
        experiences = experiences_text.get("1.0", tk.END).strip()
        education = education_text.get("1.0", tk.END).strip()
        skills = skills_entry.get().split(", ")
        header_image_path = filedialog.askopenfilename(title="Select Header Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        # Generate the resume
        pdf_buffer = create_template(name, title, address, email, phone, summary, experiences, education, skills, header_image_path)

        # Save the resume to a PDF file
        pdf_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        with open(pdf_file_path, "wb") as pdf_file:
            pdf_file.write(pdf_buffer.read())

        print(f"Resume exported to {pdf_file_path}")

    # GUI elements
    tk.Label(root, text="Name:").pack(anchor="w")
    name_entry = tk.Entry(root)
    name_entry.pack(fill=tk.X)

    tk.Label(root, text="Title:").pack(anchor="w")
    title_entry = tk.Entry(root)
    title_entry.pack(fill=tk.X)

    tk.Label(root, text="Address:").pack(anchor="w")
    address_entry = tk.Entry(root)
    address_entry.pack(fill=tk.X)

    tk.Label(root, text="Email:").pack(anchor="w")
    email_entry = tk.Entry(root)
    email_entry.pack(fill=tk.X)

    tk.Label(root, text="Phone:").pack(anchor="w")
    phone_entry = tk.Entry(root)
    phone_entry.pack(fill=tk.X)

    tk.Label(root, text="Summary:").pack(anchor="w")
    summary_text = tk.Text(root, height=5, width=50)
    summary_text.pack(fill=tk.X)

    tk.Label(root, text="Experiences:").pack(anchor="w")
    experiences_text = tk.Text(root, height=5, width=50)
    experiences_text.pack(fill=tk.X)

    tk.Label(root, text="Education:").pack(anchor="w")
    education_text = tk.Text(root, height=5, width=50)
    education_text.pack(fill=tk.X)

    tk.Label(root, text="Skills (comma-separated):").pack(anchor="w")
    skills_entry = tk.Entry(root)
    skills_entry.pack(fill=tk.X)

    # Button to generate the resume
    tk.Button(root, text="Generate Resume", command=generate).pack()

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    # Run the script to generate the resume with user input and GUI
    generate_resume()
#PROJECT DONE BY AMULA AKHIL SAGAR
#NOTE:before running this program make sure that you have downloaded the necessary modules