# Install fpdf if not already installed
# !pip install fpdf

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set a red-colored bold header
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)  # red
        self.cell(0, 10, 'Proposal for Funding Approval: Rangotsav – Holi Celebration 2025', ln=True, align='C')
        self.ln(5)

    def chapter_title(self, title):
        # Blue colored chapter title
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 102, 204)  # blue
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        # Black body text
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of PDF class
pdf = PDF()
pdf.add_page()

# 1. Introduction
pdf.chapter_title("1. Introduction")
intro_text = (
    "This proposal outlines a grand-scale Holi celebration at MCBU University designed "
    "to foster cultural unity, excitement, and community spirit. Rangotsav – Holi Celebration 2025 "
    "will engage all students from MCBU and its affiliated colleges, featuring live music, eco-friendly "
    "color zones, traditional foods, and engaging activities."
)
pdf.chapter_body(intro_text)

# 2. Event Details
pdf.chapter_title("2. Event Details")
event_details_text = (
    "Event Name: Rangotsav – Holi Celebration 2025\n"
    "Date & Time: [Insert Date & Time]\n"
    "Venue: MCBU University Grounds\n"
    "Expected Attendance: Full participation from all MCBU students (including affiliated colleges)\n"
    "Theme: Eco-friendly and Musical Holi"
)
pdf.chapter_body(event_details_text)

# 3. Proposed Activities
pdf.chapter_title("3. Proposed Activities")
activities_text = (
    "• Color Play Zone: Setup with organic, eco-friendly colors and water balloons for an authentic experience.\n"
    "• Live Entertainment: Performances by local bands and a professional DJ.\n"
    "• Food Court: A variety of traditional Holi snacks managed via coordinated vendor stalls.\n"
    "• Interactive Games & Competitions: Engaging contests such as tug-of-war and best-dressed competitions.\n"
    "• Photo Booths: Themed installations to capture memorable moments."
)
pdf.chapter_body(activities_text)

# 4. Integrated Budget Breakdown
pdf.chapter_title("4. Integrated Budget Breakdown")
budget_text = (
    "Total Budget: ₹27,00,000\n\n"
    "Expense Items:\n"
    " - Organic Colors & Materials: ₹3,50,000\n"
    " - Sound, DJ & Entertainment Setup: ₹5,50,000\n"
    " - Stage, Decoration & Logistics: ₹7,00,000\n"
    " - Food & Beverages: ₹3,00,000\n"
    " - Security, Safety & Risk Management: ₹2,50,000\n"
    " - Photography, Videography & Reporting: ₹1,50,000\n"
    " - Miscellaneous & Operational Oversight: ₹4,00,000"
)
pdf.chapter_body(budget_text)

# 5. Value Proposition
pdf.chapter_title("5. Value Proposition")
value_text = (
    "• Unified planning ensures every element—from logistics to safety—is executed with precision.\n"
    "• Enhanced community engagement by including students from all affiliated colleges.\n"
    "• Transparent financials demonstrate a clear and comprehensive investment in delivering a high-quality event."
)
pdf.chapter_body(value_text)

# 6. Conclusion
pdf.chapter_title("6. Conclusion")
conclusion_text = (
    "Rangotsav – Holi Celebration 2025 is set to be a landmark event at MCBU University, "
    "boosting campus spirit and fostering cultural unity. This proposal seeks funding approval to "
    "bring this vibrant celebration to life. Thank you for your time and consideration."
)
pdf.chapter_body(conclusion_text)

# Output the PDF to a file
pdf.output("proposal_colorful.pdf")
print("Colorful PDF proposal has been generated as 'proposal_colorful.pdf'.")
