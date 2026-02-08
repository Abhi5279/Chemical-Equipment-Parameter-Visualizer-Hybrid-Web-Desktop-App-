# # # # # # from reportlab.lib.pagesizes import A4
# # # # # # from reportlab.pdfgen import canvas


# # # # # # def generate_dataset_pdf(dataset, file_path):
# # # # # #     """
# # # # # #     Generates a PDF report for a dataset
# # # # # #     """

# # # # # #     c = canvas.Canvas(file_path, pagesize=A4)
# # # # # #     width, height = A4

# # # # # #     y = height - 50

# # # # # #     c.setFont("Helvetica-Bold", 16)
# # # # # #     c.drawString(50, y, "Chemical Equipment Analysis Report")

# # # # # #     y -= 40
# # # # # #     c.setFont("Helvetica", 11)

# # # # # #     c.drawString(50, y, f"Dataset Name: {dataset.file_name}")
# # # # # #     y -= 20
# # # # # #     c.drawString(50, y, f"Uploaded At: {dataset.uploaded_at}")

# # # # # #     y -= 30
# # # # # #     c.setFont("Helvetica-Bold", 12)
# # # # # #     c.drawString(50, y, "Summary Metrics")

# # # # # #     y -= 20
# # # # # #     c.setFont("Helvetica", 11)
# # # # # #     c.drawString(50, y, f"Total Equipment: {dataset.total_equipment}")
# # # # # #     y -= 15
# # # # # #     c.drawString(50, y, f"Average Flowrate: {dataset.avg_flowrate}")
# # # # # #     y -= 15
# # # # # #     c.drawString(50, y, f"Average Pressure: {dataset.avg_pressure}")
# # # # # #     y -= 15
# # # # # #     c.drawString(50, y, f"Average Temperature: {dataset.avg_temperature}")

# # # # # #     y -= 25
# # # # # #     c.setFont("Helvetica-Bold", 12)
# # # # # #     c.drawString(50, y, "Risk & Health")

# # # # # #     y -= 20
# # # # # #     c.setFont("Helvetica", 11)
# # # # # #     c.drawString(50, y, f"Health Score: {dataset.health_score} / 100")

# # # # # #     y -= 30
# # # # # #     c.setFont("Helvetica-Oblique", 10)
# # # # # #     c.drawString(
# # # # # #         50,
# # # # # #         y,
# # # # # #         "This report is system-generated based on uploaded equipment data."
# # # # # #     )

# # # # # #     c.showPage()
# # # # # #     c.save()

# # # # # from reportlab.lib import colors
# # # # # from reportlab.lib.pagesizes import A4
# # # # # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # # # # from reportlab.platypus import (
# # # # #     SimpleDocTemplate,
# # # # #     Table,
# # # # #     TableStyle,
# # # # #     Paragraph,
# # # # #     Spacer,
# # # # #     HRFlowable,
# # # # # )


# # # # # def generate_dataset_pdf(dataset, file_path):
# # # # #     """
# # # # #     Generates a professional PDF report for a dataset
# # # # #     """

# # # # #     # Document setup
# # # # #     doc = SimpleDocTemplate(
# # # # #         file_path,
# # # # #         pagesize=A4,
# # # # #         rightMargin=50,
# # # # #         leftMargin=50,
# # # # #         topMargin=50,
# # # # #         bottomMargin=50,
# # # # #     )

# # # # #     styles = getSampleStyleSheet()
# # # # #     elements = []

# # # # #     # ===============================
# # # # #     # 1. HEADER SECTION
# # # # #     # ===============================
# # # # #     title_style = ParagraphStyle(
# # # # #         "MainTitle",
# # # # #         parent=styles["Heading1"],
# # # # #         fontSize=22,
# # # # #         textColor=colors.HexColor("#1A3A5F"),
# # # # #         spaceAfter=10,
# # # # #     )

# # # # #     elements.append(
# # # # #         Paragraph("Chemical Equipment Analysis Report", title_style)
# # # # #     )

# # # # #     meta_text = (
# # # # #         f"<b>Dataset:</b> {dataset.file_name}<br/>"
# # # # #         f"<b>Generated:</b> {dataset.uploaded_at.strftime('%d %b %Y, %H:%M')}"
# # # # #     )
# # # # #     elements.append(Paragraph(meta_text, styles["Normal"]))
# # # # #     elements.append(Spacer(1, 20))
# # # # #     elements.append(
# # # # #         HRFlowable(
# # # # #             width="100%",
# # # # #             thickness=1,
# # # # #             color=colors.lightgrey,
# # # # #             spaceBefore=5,
# # # # #             spaceAfter=20,
# # # # #         )
# # # # #     )

# # # # #     # ===============================
# # # # #     # 2. SUMMARY METRICS TABLE
# # # # #     # ===============================
# # # # #     elements.append(
# # # # #         Paragraph("<b>Summary Metrics</b>", styles["Heading3"])
# # # # #     )
# # # # #     elements.append(Spacer(1, 10))

# # # # #     metric_data = [
# # # # #         ["Metric Description", "Value"],
# # # # #         ["Total Equipment Count", str(dataset.total_equipment)],
# # # # #         ["Average Flowrate", str(dataset.avg_flowrate)],
# # # # #         ["Average Pressure", str(dataset.avg_pressure)],
# # # # #         ["Average Temperature", str(dataset.avg_temperature)],
# # # # #     ]

# # # # #     metric_table = Table(metric_data, colWidths=[300, 150])
# # # # #     metric_table.setStyle(
# # # # #         TableStyle(
# # # # #             [
# # # # #                 ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F2F2")),
# # # # #                 ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1A3A5F")),
# # # # #                 ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
# # # # #                 ("ALIGN", (0, 0), (-1, -1), "LEFT"),
# # # # #                 ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
# # # # #                 ("FONTSIZE", (0, 0), (-1, -1), 10),
# # # # #                 ("TOPPADDING", (0, 0), (-1, -1), 8),
# # # # #                 ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
# # # # #             ]
# # # # #         )
# # # # #     )

# # # # #     elements.append(metric_table)
# # # # #     elements.append(Spacer(1, 25))

# # # # #     # ===============================
# # # # #     # 3. SAFETY & HEALTH SECTION
# # # # #     # ===============================
# # # # #     elements.append(
# # # # #         Paragraph("<b>Safety & Integrity Assessment</b>", styles["Heading3"])
# # # # #     )
# # # # #     elements.append(Spacer(1, 10))

# # # # #     health_color = (
# # # # #         colors.darkgreen if dataset.health_score >= 70 else colors.darkred
# # # # #     )

# # # # #     health_data = [
# # # # #         ["Overall Health Score", f"{dataset.health_score} / 100"]
# # # # #     ]

# # # # #     health_table = Table(health_data, colWidths=[300, 150])
# # # # #     health_table.setStyle(
# # # # #         TableStyle(
# # # # #             [
# # # # #                 ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#F8F9FA")),
# # # # #                 ("TEXTCOLOR", (1, 0), (1, 0), health_color),
# # # # #                 ("FONTNAME", (1, 0), (1, 0), "Helvetica-Bold"),
# # # # #                 ("FONTSIZE", (1, 0), (1, 0), 14),
# # # # #                 ("ALIGN", (0, 0), (-1, -1), "CENTER"),
# # # # #                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
# # # # #                 ("BOX", (0, 0), (-1, -1), 1.5, colors.HexColor("#1A3A5F")),
# # # # #                 ("TOPPADDING", (0, 0), (-1, -1), 15),
# # # # #                 ("BOTTOMPADDING", (0, 0), (-1, -1), 15),
# # # # #             ]
# # # # #         )
# # # # #     )

# # # # #     elements.append(health_table)

# # # # #     # ===============================
# # # # #     # 4. FOOTER
# # # # #     # ===============================
# # # # #     elements.append(Spacer(1, 40))

# # # # #     footer_style = ParagraphStyle(
# # # # #         "Footer",
# # # # #         parent=styles["Normal"],
# # # # #         fontSize=8,
# # # # #         textColor=colors.grey,
# # # # #         alignment=1,
# # # # #     )

# # # # #     elements.append(
# # # # #         Paragraph(
# # # # #             "This report is system-generated based on uploaded equipment data.<br/>"
# # # # #             "Confidential – Internal Use Only",
# # # # #             footer_style,
# # # # #         )
# # # # #     )

# # # # #     # Build PDF
# # # # #     doc.build(elements)

# # # # from reportlab.lib import colors
# # # # from reportlab.lib.pagesizes import A4
# # # # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # # # from reportlab.platypus import (
# # # #     SimpleDocTemplate,
# # # #     Table,
# # # #     TableStyle,
# # # #     Paragraph,
# # # #     Spacer,
# # # #     HRFlowable,
# # # # )


# # # # def generate_dataset_pdf(dataset, file_path):
# # # #     """
# # # #     Generates a professional, bordered PDF report for a dataset
# # # #     """

# # # #     summary = dataset.summary

# # # #     doc = SimpleDocTemplate(
# # # #         file_path,
# # # #         pagesize=A4,
# # # #         rightMargin=50,
# # # #         leftMargin=50,
# # # #         topMargin=50,
# # # #         bottomMargin=50,
# # # #     )

# # # #     styles = getSampleStyleSheet()
# # # #     elements = []

# # # #     # ===============================
# # # #     # HEADER
# # # #     # ===============================
# # # #     title_style = ParagraphStyle(
# # # #         "MainTitle",
# # # #         parent=styles["Heading1"],
# # # #         fontSize=22,
# # # #         textColor=colors.HexColor("#1A3A5F"),
# # # #         spaceAfter=10,
# # # #     )

# # # #     elements.append(
# # # #         Paragraph("Chemical Equipment Analysis Report", title_style)
# # # #     )

# # # #     meta_text = (
# # # #         f"<b>Dataset:</b> {dataset.file_name}<br/>"
# # # #         f"<b>Generated:</b> {dataset.uploaded_at.strftime('%d %b %Y, %H:%M')}"
# # # #     )
# # # #     elements.append(Paragraph(meta_text, styles["Normal"]))
# # # #     elements.append(Spacer(1, 15))

# # # #     elements.append(
# # # #         HRFlowable(width="100%", thickness=1, color=colors.grey)
# # # #     )
# # # #     elements.append(Spacer(1, 20))

# # # #     # ===============================
# # # #     # SUMMARY METRICS
# # # #     # ===============================
# # # #     elements.append(
# # # #         Paragraph("<b>Summary Metrics</b>", styles["Heading3"])
# # # #     )
# # # #     elements.append(Spacer(1, 10))

# # # #     metrics = [
# # # #         ["Metric", "Value"],
# # # #         ["Total Equipment", dataset.total_equipment],
# # # #         ["Average Flowrate", dataset.avg_flowrate],
# # # #         ["Average Pressure", dataset.avg_pressure],
# # # #         ["Average Temperature", dataset.avg_temperature],
# # # #     ]

# # # #     metric_table = Table(metrics, colWidths=[280, 170])
# # # #     metric_table.setStyle(_boxed_table_style())
# # # #     elements.append(metric_table)
# # # #     elements.append(Spacer(1, 25))

# # # #     # ===============================
# # # #     # EQUIPMENT TYPE DISTRIBUTION
# # # #     # ===============================
# # # #     elements.append(
# # # #         Paragraph("<b>Equipment Type Distribution</b>", styles["Heading3"])
# # # #     )
# # # #     elements.append(Spacer(1, 10))

# # # #     type_data = [["Equipment Type", "Count"]]
# # # #     for eq_type, count in summary["equipment_type_distribution"].items():
# # # #         type_data.append([eq_type, count])

# # # #     type_table = Table(type_data, colWidths=[280, 170])
# # # #     type_table.setStyle(_boxed_table_style())
# # # #     elements.append(type_table)
# # # #     elements.append(Spacer(1, 25))

# # # #     # ===============================
# # # #     # RISK ANALYSIS
# # # #     # ===============================
# # # #     elements.append(
# # # #         Paragraph("<b>Risk Analysis</b>", styles["Heading3"])
# # # #     )
# # # #     elements.append(Spacer(1, 10))

# # # #     risk = summary["risk_analysis"]
# # # #     risk_data = [
# # # #         ["Risk Category", "Count"],
# # # #         ["High Risk Equipment", risk["high_risk"]],
# # # #         ["Normal Equipment", risk["normal"]],
# # # #     ]

# # # #     risk_table = Table(risk_data, colWidths=[280, 170])
# # # #     risk_table.setStyle(_boxed_table_style())
# # # #     elements.append(risk_table)
# # # #     elements.append(Spacer(1, 25))

# # # #     # ===============================
# # # #     # HEALTH SCORE (HIGHLIGHTED)
# # # #     # ===============================
# # # #     elements.append(
# # # #         Paragraph("<b>Overall Health Assessment</b>", styles["Heading3"])
# # # #     )
# # # #     elements.append(Spacer(1, 10))

# # # #     health_color = (
# # # #         colors.darkgreen
# # # #         if dataset.health_score >= 70
# # # #         else colors.orange
# # # #         if dataset.health_score >= 40
# # # #         else colors.darkred
# # # #     )

# # # #     health_table = Table(
# # # #         [["Health Score", f"{dataset.health_score} / 100"]],
# # # #         colWidths=[280, 170],
# # # #     )

# # # #     health_table.setStyle(
# # # #         TableStyle(
# # # #             [
# # # #                 ("BOX", (0, 0), (-1, -1), 2, colors.HexColor("#1A3A5F")),
# # # #                 ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#F2F2F2")),
# # # #                 ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
# # # #                 ("FONTSIZE", (1, 0), (1, 0), 16),
# # # #                 ("TEXTCOLOR", (1, 0), (1, 0), health_color),
# # # #                 ("ALIGN", (0, 0), (-1, -1), "CENTER"),
# # # #                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
# # # #                 ("TOPPADDING", (0, 0), (-1, -1), 15),
# # # #                 ("BOTTOMPADDING", (0, 0), (-1, -1), 15),
# # # #             ]
# # # #         )
# # # #     )

# # # #     elements.append(health_table)
# # # #     elements.append(Spacer(1, 40))

# # # #     # ===============================
# # # #     # FOOTER
# # # #     # ===============================
# # # #     footer_style = ParagraphStyle(
# # # #         "Footer",
# # # #         parent=styles["Normal"],
# # # #         fontSize=8,
# # # #         textColor=colors.grey,
# # # #         alignment=1,
# # # #     )

# # # #     elements.append(
# # # #         Paragraph(
# # # #             "This report is system-generated based on uploaded equipment data.<br/>"
# # # #             "Confidential – Internal Use Only",
# # # #             footer_style,
# # # #         )
# # # #     )

# # # #     doc.build(elements)


# # # # def _boxed_table_style():
# # # #     """
# # # #     Shared bordered table style
# # # #     """
# # # #     return TableStyle(
# # # #         [
# # # #             ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F2F2")),
# # # #             ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1A3A5F")),
# # # #             ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
# # # #             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
# # # #             ("GRID", (0, 0), (-1, -1), 1, colors.grey),
# # # #             ("FONTSIZE", (0, 0), (-1, -1), 10),
# # # #             ("TOPPADDING", (0, 0), (-1, -1), 8),
# # # #             ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
# # # #         ]
# # # #     )


# # # from reportlab.lib import colors
# # # from reportlab.lib.pagesizes import A4
# # # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # # from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
# # # from reportlab.lib.units import inch

# # # def generate_dataset_pdf(dataset, file_path):
# # #     doc = SimpleDocTemplate(
# # #         file_path,
# # #         pagesize=A4,
# # #         rightMargin=30,
# # #         leftMargin=30,
# # #         topMargin=30,
# # #         bottomMargin=30,
# # #     )
    
# # #     styles = getSampleStyleSheet()
# # #     elements = []
# # #     summary = dataset.summary

# # #     # --- Header ---
# # #     title_style = ParagraphStyle("Title", fontSize=18, textColor=colors.HexColor("#1A3A5F"), fontName="Helvetica-Bold")
# # #     elements.append(Paragraph("Chemical Equipment Analysis Dashboard", title_style))
    
# # #     meta_style = ParagraphStyle("Meta", fontSize=9, textColor=colors.grey)
# # #     meta_text = f"Dataset: {dataset.file_name} | Generated: {dataset.uploaded_at.strftime('%d %b %Y')}"
# # #     elements.append(Paragraph(meta_text, meta_style))
# # #     elements.append(Spacer(1, 10))
# # #     elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1A3A5F")))
# # #     elements.append(Spacer(1, 15))

# # #     # --- TOP ROW: Key Metrics (Horizontal) ---
# # #     metric_data = [
# # #         ["Total Equipment", "Avg Flowrate", "Avg Pressure", "Avg Temp"],
# # #         [dataset.total_equipment, dataset.avg_flowrate, dataset.avg_pressure, dataset.avg_temperature]
# # #     ]
# # #     top_table = Table(metric_data, colWidths=[130]*4)
# # #     top_table.setStyle(TableStyle([
# # #         ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1A3A5F")),
# # #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
# # #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
# # #         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
# # #         ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
# # #         ('FONTSIZE', (0, 0), (-1, -1), 10),
# # #         ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
# # #         ('TOPPADDING', (0, 0), (-1, -1), 10),
# # #     ]))
# # #     elements.append(top_table)
# # #     elements.append(Spacer(1, 20))

# # #     # --- MAIN CONTENT: Two-Column Layout ---
# # #     # Left Side: Tables | Right Side: "Visual" Status Bars
    
# # #     # 1. Equipment Table
# # #     type_data = [["Equipment Category", "Count"]]
# # #     for eq_type, count in summary["equipment_type_distribution"].items():
# # #         type_data.append([eq_type, count])
# # #     left_table = Table(type_data, colWidths=[180, 70])
# # #     left_table.setStyle(_clean_table_style())

# # #     # 2. Risk Visual (Right Side)
# # #     risk = summary["risk_analysis"]
# # #     health_pct = dataset.health_score # Assuming 0-100
    
# # #     # Simple Visual Bar for Health
# # #     health_bar_bg = Table([[""]], colWidths=[200], rowHeights=[20])
# # #     health_bar_bg.setStyle(TableStyle([
# # #         ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
# # #         ('BOX', (0,0), (-1,-1), 1, colors.grey)
# # #     ]))
    
# # #     # Overall layout table (invisible) to hold columns
# # #     main_grid_data = [
# # #         [
# # #             [Paragraph("<b>Distribution Details</b>", styles['Normal']), Spacer(1, 5), left_table],
# # #             [
# # #                 Paragraph("<b>System Health & Risk</b>", styles['Normal']), 
# # #                 Spacer(1, 10),
# # #                 Paragraph(f"Overall Health: {health_pct}%", styles['Normal']),
# # #                 _generate_status_bar(health_pct, 200),
# # #                 Spacer(1, 15),
# # #                 Paragraph("<b>Risk Profile</b>", styles['Normal']),
# # #                 _generate_risk_table(risk)
# # #             ]
# # #         ]
# # #     ]
    
# # #     main_grid = Table(main_grid_data, colWidths=[270, 250])
# # #     main_grid.setStyle(TableStyle([
# # #         ('VALIGN', (0, 0), (-1, -1), 'TOP'),
# # #         ('LEFTPADDING', (1, 0), (1, 0), 20),
# # #     ]))
    
# # #     elements.append(main_grid)
    
# # #     # --- Footer ---
# # #     elements.append(Spacer(1, 40))
# # #     footer = Paragraph("CONFIDENTIAL - SYSTEM GENERATED REPORT", ParagraphStyle("F", fontSize=7, alignment=1, textColor=colors.grey))
# # #     elements.append(footer)

# # #     doc.build(elements)

# # # def _clean_table_style():
# # #     return TableStyle([
# # #         ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F2F4F6")),
# # #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#1A3A5F")),
# # #         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
# # #         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
# # #         ('GRID', (0, 0), (-1, -1), 0.1, colors.grey),
# # #         ('FONTSIZE', (0, 0), (-1, -1), 9),
# # #         ('TOPPADDING', (0, 0), (-1, -1), 6),
# # #         ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
# # #     ])

# # # def _generate_status_bar(pct, width):
# # #     """Creates a visual progress bar using a Table"""
# # #     filled_width = (pct / 100.0) * width
# # #     color = colors.darkgreen if pct > 70 else colors.orange if pct > 40 else colors.red
# # #     bar = Table([[""]], colWidths=[filled_width], rowHeights=[12])
# # #     bar.setStyle(TableStyle([
# # #         ('BACKGROUND', (0, 0), (-1, -1), color),
# # #         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
# # #     ]))
# # #     return bar

# # # def _generate_risk_table(risk):
# # #     data = [
# # #         ["High Risk", risk["high_risk"]],
# # #         ["Normal", risk["normal"]]
# # #     ]
# # #     t = Table(data, colWidths=[120, 50])
# # #     t.setStyle(TableStyle([
# # #         ('TEXTCOLOR', (0,0), (0,0), colors.red),
# # #         ('FONTNAME', (0,0), (-1, -1), 'Helvetica'),
# # #         ('FONTSIZE', (0,0), (-1, -1), 9),
# # #         ('LINEBELOW', (0,0), (-1, -1), 0.5, colors.lightgrey),
# # #     ]))
# # #     return t

# # from reportlab.lib import colors
# # from reportlab.lib.pagesizes import A4
# # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # from reportlab.platypus import (
# #     SimpleDocTemplate,
# #     Table,
# #     TableStyle,
# #     Paragraph,
# #     Spacer,
# #     HRFlowable,
# # )
# # from reportlab.lib.units import inch


# # def generate_dataset_pdf(dataset, file_path):
# #     summary = dataset.summary

# #     doc = SimpleDocTemplate(
# #         file_path,
# #         pagesize=A4,
# #         rightMargin=36,
# #         leftMargin=36,
# #         topMargin=36,
# #         bottomMargin=36,
# #     )

# #     styles = getSampleStyleSheet()
# #     elements = []

# #     # =========================
# #     # HEADER (EXECUTIVE)
# #     # =========================
# #     title = Paragraph(
# #         "Chemical Equipment Analytics Report",
# #         ParagraphStyle(
# #             "title",
# #             fontSize=20,
# #             fontName="Helvetica-Bold",
# #             textColor=colors.HexColor("#0F2A44"),
# #         ),
# #     )

# #     meta = Paragraph(
# #         f"""
# #         <b>Dataset:</b> {dataset.file_name}<br/>
# #         <b>Generated:</b> {dataset.uploaded_at.strftime('%d %b %Y, %H:%M')}
# #         """,
# #         ParagraphStyle("meta", fontSize=9, textColor=colors.grey),
# #     )

# #     elements.extend([title, Spacer(1, 6), meta, Spacer(1, 12)])
# #     elements.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey))
# #     elements.append(Spacer(1, 18))

# #     # =========================
# #     # EXECUTIVE KPI STRIP
# #     # =========================
# #     kpi_data = [
# #         ["TOTAL UNITS", "AVG FLOW", "AVG PRESSURE", "AVG TEMP", "HEALTH"],
# #         [
# #             dataset.total_equipment,
# #             dataset.avg_flowrate,
# #             dataset.avg_pressure,
# #             dataset.avg_temperature,
# #             f"{dataset.health_score}%",
# #         ],
# #     ]

# #     kpi_table = Table(kpi_data, colWidths=[90] * 5)
# #     kpi_table.setStyle(
# #         TableStyle(
# #             [
# #                 ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F2A44")),
# #                 ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
# #                 ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#0F2A44")),
# #                 ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
# #                 ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
# #                 ("ALIGN", (0, 0), (-1, -1), "CENTER"),
# #                 ("FONTSIZE", (0, 0), (-1, -1), 10),
# #                 ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#0F2A44")),
# #                 ("TOPPADDING", (0, 0), (-1, -1), 12),
# #                 ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
# #             ]
# #         )
# #     )

# #     elements.append(kpi_table)
# #     elements.append(Spacer(1, 22))

# #     # =========================
# #     # MAIN ANALYTICS GRID
# #     # =========================

# #     # ---- LEFT: Equipment Distribution
# #     dist_data = [["Equipment Type", "Count"]]
# #     for k, v in summary["equipment_type_distribution"].items():
# #         dist_data.append([k, v])

# #     dist_table = Table(dist_data, colWidths=[180, 60])
# #     dist_table.setStyle(_table_style())

# #     left_block = [
# #         Paragraph(
# #             "Equipment Distribution",
# #             ParagraphStyle("h", fontSize=12, fontName="Helvetica-Bold"),
# #         ),
# #         Spacer(1, 8),
# #         dist_table,
# #     ]

# #     # ---- RIGHT: Health & Risk
# #     health_bar = _progress_bar(dataset.health_score, 180)

# #     risk_table = Table(
# #         [
# #             ["High Risk Units", summary["risk_analysis"]["high_risk"]],
# #             ["Normal Units", summary["risk_analysis"]["normal"]],
# #         ],
# #         colWidths=[140, 40],
# #     )
# #     risk_table.setStyle(_risk_style())

# #     right_block = [
# #         Paragraph(
# #             "System Integrity & Risk",
# #             ParagraphStyle("h", fontSize=12, fontName="Helvetica-Bold"),
# #         ),
# #         Spacer(1, 10),
# #         Paragraph(f"<b>Overall Health:</b> {dataset.health_score}%", styles["Normal"]),
# #         Spacer(1, 6),
# #         health_bar,
# #         Spacer(1, 14),
# #         Paragraph("<b>Risk Breakdown</b>", styles["Normal"]),
# #         Spacer(1, 6),
# #         risk_table,
# #     ]

# #     main_grid = Table(
# #         [[left_block, right_block]],
# #         colWidths=[250, 230],
# #         style=[
# #             ("VALIGN", (0, 0), (-1, -1), "TOP"),
# #             ("LEFTPADDING", (1, 0), (1, 0), 24),
# #         ],
# #     )

# #     elements.append(main_grid)

# #     # =========================
# #     # FOOTER
# #     # =========================
# #     elements.append(Spacer(1, 36))
# #     elements.append(
# #         Paragraph(
# #             "CONFIDENTIAL • SYSTEM GENERATED • INTERNAL USE ONLY",
# #             ParagraphStyle(
# #                 "f",
# #                 fontSize=7,
# #                 textColor=colors.grey,
# #                 alignment=1,
# #             ),
# #         )
# #     )

# #     doc.build(elements)


# # # =========================
# # # STYLES & HELPERS
# # # =========================

# # def _table_style():
# #     return TableStyle(
# #         [
# #             ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F3F6F9")),
# #             ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#0F2A44")),
# #             ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
# #             ("ALIGN", (1, 1), (-1, -1), "CENTER"),
# #             ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
# #             ("FONTSIZE", (0, 0), (-1, -1), 9),
# #             ("TOPPADDING", (0, 0), (-1, -1), 8),
# #             ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
# #         ]
# #     )


# # def _risk_style():
# #     return TableStyle(
# #         [
# #             ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
# #             ("FONTSIZE", (0, 0), (-1, -1), 9),
# #             ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.lightgrey),
# #             ("TEXTCOLOR", (0, 0), (0, 0), colors.red),
# #             ("TEXTCOLOR", (0, 1), (0, 1), colors.darkgreen),
# #         ]
# #     )


# # def _progress_bar(pct, width):
# #     color = (
# #         colors.darkgreen if pct >= 70
# #         else colors.orange if pct >= 40
# #         else colors.red
# #     )

# #     filled = (pct / 100) * width

# #     bar = Table(
# #         [[""]],
# #         colWidths=[filled],
# #         rowHeights=[10],
# #         style=[
# #             ("BACKGROUND", (0, 0), (-1, -1), color),
# #         ],
# #     )

# #     container = Table(
# #         [[bar]],
# #         colWidths=[width],
# #         rowHeights=[10],
# #         style=[
# #             ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
# #             ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
# #         ],
# #     )

# #     return container


# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Table,
#     TableStyle,
#     Paragraph
# )
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# def generate_dataset_pdf(dataset, file_path):
#     summary = dataset.summary
#     styles = getSampleStyleSheet()

#     doc = SimpleDocTemplate(
#         file_path,
#         pagesize=A4,
#         rightMargin=24,
#         leftMargin=24,
#         topMargin=24,
#         bottomMargin=24,
#     )

#     elements = []

#     # ==================================================
#     # HEADER (TIGHT, ALIGNED)
#     # ==================================================
#     header = Table(
#         [[
#             Paragraph(
#                 "<b>Chemical Equipment Analysis Report</b>",
#                 ParagraphStyle(
#                     "t",
#                     fontSize=16,
#                     textColor=colors.HexColor("#0F2A44"),
#                 ),
#             ),
#             Paragraph(
#                 f"""
#                 <font size=8>
#                 Dataset: {dataset.file_name}<br/>
#                 Generated: {dataset.uploaded_at.strftime('%d %b %Y %H:%M')}
#                 </font>
#                 """,
#                 styles["Normal"],
#             ),
#         ]],
#         colWidths=[320, 180],
#     )

#     header.setStyle(TableStyle([
#         ("VALIGN", (0, 0), (-1, -1), "TOP"),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
#         ("LINEBELOW", (0, 0), (-1, -1), 1, colors.grey),
#     ]))

#     elements.append(header)

#     # ==================================================
#     # KPI STRIP (FIXED HEIGHT)
#     # ==================================================
#     kpi = Table(
#         [[
#             "TOTAL",
#             "AVG FLOW",
#             "AVG PRESS",
#             "AVG TEMP",
#             "HEALTH"
#         ],
#         [
#             dataset.total_equipment,
#             dataset.avg_flowrate,
#             dataset.avg_pressure,
#             dataset.avg_temperature,
#             f"{dataset.health_score}%",
#         ]],
#         colWidths=[100] * 5,
#         rowHeights=[22, 26],
#     )

#     kpi.setStyle(TableStyle([
#         ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F2A44")),
#         ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
#         ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#0F2A44")),
#         ("FONTNAME", (0, 0), (-1, 1), "Helvetica-Bold"),
#         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#         ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
#     ]))

#     elements.append(kpi)

#     # ==================================================
#     # MAIN GRID (NO SPACERS, FULL WIDTH)
#     # ==================================================
#     # LEFT: Equipment Distribution
#     dist_data = [["EQUIPMENT TYPE", "COUNT"]]
#     for k, v in summary["equipment_type_distribution"].items():
#         dist_data.append([k, v])

#     dist_table = Table(
#         dist_data,
#         colWidths=[200, 60],
#         rowHeights=18,
#     )

#     dist_table.setStyle(TableStyle([
#         ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9EEF3")),
#         ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#         ("ALIGN", (1, 1), (-1, -1), "CENTER"),
#         ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
#         ("FONTSIZE", (0, 0), (-1, -1), 9),
#     ]))

#     # RIGHT: Health + Risk
#     risk = summary["risk_analysis"]

#     health_bar = _fixed_bar(dataset.health_score, 180)

#     right_block = Table(
#         [
#             ["OVERALL HEALTH", f"{dataset.health_score}%"],
#             [health_bar, ""],
#             ["HIGH RISK", risk["high_risk"]],
#             ["NORMAL", risk["normal"]],
#         ],
#         colWidths=[180, 80],
#         rowHeights=[18, 16, 18, 18],
#     )

#     right_block.setStyle(TableStyle([
#         ("SPAN", (0, 1), (-1, 1)),
#         ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
#         ("TEXTCOLOR", (0, 2), (0, 2), colors.red),
#         ("TEXTCOLOR", (0, 3), (0, 3), colors.darkgreen),
#         ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
#         ("ALIGN", (1, 0), (-1, -1), "CENTER"),
#     ]))

#     main = Table(
#         [[dist_table, right_block]],
#         colWidths=[260, 260],
#         rowHeights=[120],
#     )

#     main.setStyle(TableStyle([
#         ("VALIGN", (0, 0), (-1, -1), "TOP"),
#         ("TOPPADDING", (0, 0), (-1, -1), 6),
#     ]))

#     elements.append(main)

#     # ==================================================
#     # FOOTER (TIGHT)
#     # ==================================================
#     footer = Table(
#         [[
#             Paragraph(
#                 "<font size=7>CONFIDENTIAL • SYSTEM GENERATED • INTERNAL USE ONLY</font>",
#                 styles["Normal"],
#             )
#         ]],
#         colWidths=[520],
#     )

#     footer.setStyle(TableStyle([
#         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#         ("TOPPADDING", (0, 0), (-1, -1), 6),
#         ("LINEABOVE", (0, 0), (-1, -1), 0.5, colors.grey),
#     ]))

#     elements.append(footer)

#     doc.build(elements)


# # ==================================================
# # HELPERS
# # ==================================================

# def _fixed_bar(pct, width):
#     color = (
#         colors.darkgreen if pct >= 70
#         else colors.orange if pct >= 40
#         else colors.red
#     )

#     filled = max(1, int((pct / 100) * width))

#     bar = Table(
#         [[""]],
#         colWidths=[filled],
#         rowHeights=[10],
#         style=[("BACKGROUND", (0, 0), (-1, -1), color)],
#     )

#     container = Table(
#         [[bar]],
#         colWidths=[width],
#         rowHeights=[10],
#         style=[
#             ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
#             ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
#         ],
#     )

#     return container


from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def generate_dataset_pdf(dataset, file_path):
    summary = dataset.summary
    styles = getSampleStyleSheet()
    
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30,
    )
    
    elements = []
    
    # ================================================== 
    # HEADER
    # ==================================================
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=colors.HexColor("#0F2A44"),
        spaceAfter=6,
        alignment=TA_LEFT,
        fontName="Helvetica-Bold"
    )
    
    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["Normal"],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_RIGHT,
    )
    
    header_data = [[
        Paragraph("Chemical Equipment Analysis Report", title_style),
        Paragraph(
            f"<b>Dataset:</b> {dataset.file_name}<br/>"
            f"<b>Generated:</b> {dataset.uploaded_at.strftime('%d %b %Y %H:%M')}",
            meta_style
        ),
    ]]
    
    header = Table(header_data, colWidths=[300, 235])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ]))
    elements.append(header)
    elements.append(Spacer(1, 8))
    
    # Divider line
    divider = Table([[""]], colWidths=[535])
    divider.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 1.5, colors.HexColor("#0F2A44")),
    ]))
    elements.append(divider)
    elements.append(Spacer(1, 12))
    
    # ================================================== 
    # KPI STRIP
    # ==================================================
    kpi_header = ["TOTAL\nEQUIPMENT", "AVG FLOW\nRATE", "AVG\nPRESSURE", "AVG\nTEMP", "HEALTH\nSCORE"]
    kpi_values = [
        str(dataset.total_equipment),
        f"{dataset.avg_flowrate:.1f}",
        f"{dataset.avg_pressure:.1f}",
        f"{dataset.avg_temperature:.1f}",
        f"{dataset.health_score}%"
    ]
    
    kpi = Table(
        [kpi_header, kpi_values],
        colWidths=[107] * 5,
        rowHeights=[32, 28],
    )
    kpi.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F2A44")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 1), (-1, 1), colors.HexColor("#0F2A44")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTSIZE", (0, 1), (-1, 1), 13),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.75, colors.white),
        ("BOX", (0, 0), (-1, -1), 1.5, colors.HexColor("#0F2A44")),
    ]))
    elements.append(kpi)
    elements.append(Spacer(1, 16))
    
    # ================================================== 
    # MAIN GRID
    # ==================================================
    # LEFT: Equipment Distribution
    dist_header_style = ParagraphStyle(
        "DistHeader",
        parent=styles["Normal"],
        fontSize=10,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#0F2A44"),
    )
    
    dist_data = [[
        Paragraph("EQUIPMENT TYPE", dist_header_style),
        Paragraph("COUNT", dist_header_style)
    ]]
    
    for k, v in summary["equipment_type_distribution"].items():
        dist_data.append([
            Paragraph(str(k), styles["Normal"]),
            str(v)
        ])
    
    dist_table = Table(
        dist_data,
        colWidths=[180, 70],
        rowHeights=22,
    )
    dist_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9EEF3")),
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ("ALIGN", (1, 0), (1, 0), "CENTER"),
        ("ALIGN", (1, 1), (1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    
    # RIGHT: Health + Risk
    risk = summary["risk_analysis"]
    health_bar = _fixed_bar(dataset.health_score, 180)
    
    risk_header_style = ParagraphStyle(
        "RiskHeader",
        parent=styles["Normal"],
        fontSize=10,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#0F2A44"),
    )
    
    right_block = Table(
        [
            [
                Paragraph("OVERALL HEALTH SCORE", risk_header_style),
                Paragraph(f"<b>{dataset.health_score}%</b>", styles["Normal"])
            ],
            [health_bar, ""],
            [
                Paragraph("High Risk Equipment", styles["Normal"]),
                Paragraph(f"<b>{risk['high_risk']}</b>", styles["Normal"])
            ],
            [
                Paragraph("Normal Equipment", styles["Normal"]),
                Paragraph(f"<b>{risk['normal']}</b>", styles["Normal"])
            ],
        ],
        colWidths=[185, 80],
        rowHeights=[22, 18, 22, 22],
    )
    right_block.setStyle(TableStyle([
        ("SPAN", (0, 1), (-1, 1)),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E9EEF3")),
        ("TEXTCOLOR", (0, 2), (0, 2), colors.red),
        ("TEXTCOLOR", (0, 3), (0, 3), colors.darkgreen),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ALIGN", (1, 0), (1, 0), "CENTER"),
        ("ALIGN", (1, 2), (1, 3), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    
    main = Table(
        [[dist_table, right_block]],
        colWidths=[250, 265],
    )
    main.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    elements.append(main)
    elements.append(Spacer(1, 20))
    
    # ================================================== 
    # FOOTER
    # ==================================================
    footer_style = ParagraphStyle(
        "Footer",
        parent=styles["Normal"],
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER,
    )
    
    footer = Table(
        [[Paragraph("CONFIDENTIAL • SYSTEM GENERATED • INTERNAL USE ONLY", footer_style)]],
        colWidths=[535],
    )
    footer.setStyle(TableStyle([
        ("LINEABOVE", (0, 0), (-1, -1), 0.5, colors.grey),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
    ]))
    elements.append(footer)
    
    doc.build(elements)

# ================================================== 
# HELPERS
# ==================================================
def _fixed_bar(pct, width):
    """Creates a horizontal progress bar"""
    color = (
        colors.darkgreen if pct >= 70
        else colors.orange if pct >= 40
        else colors.red
    )
    filled = max(1, int((pct / 100) * width))
    
    bar_inner = Table(
        [[""]],
        colWidths=[filled],
        rowHeights=[12],
    )
    bar_inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
    ]))
    
    container = Table(
        [[bar_inner]],
        colWidths=[width],
        rowHeights=[12],
    )
    container.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    
    return container