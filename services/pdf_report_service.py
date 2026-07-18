from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    filename,
    resume_analysis,
    skill_gap,
    market_analysis,
    roadmap,
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>CareerPilot AI Report</b>", styles["Title"]))

    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    story.append(Paragraph("<b>Resume Analysis</b>", styles["Heading2"]))
    story.append(Paragraph(resume_analysis.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Skill Gap Analysis</b>", styles["Heading2"]))
    story.append(Paragraph(skill_gap.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Market Analysis</b>", styles["Heading2"]))
    story.append(Paragraph(market_analysis.replace("\n", "<br/>"), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Career Roadmap</b>", styles["Heading2"]))
    story.append(Paragraph(roadmap.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)