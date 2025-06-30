
from fpdf import FPDF

def generate_pdf(name, treatment, cost):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Dental Treatment Plan", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Treatment Details: {treatment}")
    pdf.cell(200, 10, txt=f"Estimated Cost: ₹{cost}", ln=True)

    file_path = f"treatment_plan_{name.replace(' ', '_')}.pdf"
    pdf.output(file_path)
    return file_path
