from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv(r"C:\Users\MNajamuddin\Downloads\topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(20, 298, 20):
        pdf.line(10, y, 200, y)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)
        for y in range(20, 298, 20):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
