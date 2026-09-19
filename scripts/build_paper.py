"""Build the local review PDF from the frozen manuscript source."""

import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paper" / "manuscript.tex"
PDF = ROOT / "paper" / "manuscript.pdf"
EQUATION_DIR = ROOT / "experiments" / "m8_visual_audit" / "equations"
EQUATIONS = {}


def clean(text):
    text = text.replace(r"\printbibliography", "")
    text = re.sub(r"\\bibliographystyle\{[^}]+\}|\\bibliography\{[^}]+\}", "", text)
    text = re.sub(r"\\(?:begin|end)\{document\}", "", text)
    replacements = {
        r"$\rho$": "rho", r"$\phi$": "phi", r"$\alpha$": "alpha",
        r"$\kappa$": "kappa", r"$\beta$": "beta", r"$R_t$": "R_t",
        r"$x_t$": "x_t", r"$e_t$": "e_t", r"$\rho=0$": "rho = 0",
        r"$\alpha>0$": "alpha > 0", r"$e_R>0$": "e_R > 0", r"$e_R<0$": "e_R < 0",
    }
    for old, new in replacements.items(): text = text.replace(old, new)
    citations={"boardmeyer2013":"Board and Meyer-ter-Vehn, 2013","bohren2024":"Bohren, 2024",
               "bhaskarthomas2019":"Bhaskar and Thomas, 2019","elulgottardi2015":"Elul and Gottardi, 2015",
               "jovanovic2021":"Jovanovic, 2021","liuskrzypacz2014":"Liu and Skrzypacz, 2014",
               "sperisen2018":"Sperisen, 2018","pei2026":"Pei, forthcoming"}
    text = re.sub(r"\\cite[tp]\{([^}]+)\}", lambda m: "("+"; ".join(citations.get(k,k) for k in m.group(1).split(","))+")", text)
    text = re.sub(r"\\(?:emph|textit|textbf)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\label\{[^}]+\}|\\ref\{[^}]+\}", "", text)
    text = text.replace("\\%", "%").replace("--", "-")
    def inline_math(match):
        value = match.group(1)
        commands = {
            r"\ldots": "...", r"\in": " in ", r"\geq": " >= ", r"\leq": " <= ",
            r"\neq": " != ", r"\phi": "phi", r"\rho": "rho", r"\alpha": "alpha",
            r"\beta": "beta", r"\kappa": "kappa", r"\Delta": "Delta ", r"\bar R": "R-bar",
        }
        value = re.sub(r"\\operatorname\{([^{}]+)\}", r"\1", value)
        for old, new in commands.items():
            value = value.replace(old, new)
        value = re.sub(r"\\([A-Za-z]+)", r"\1", value)
        return value
    text = re.sub(r"\$([^$]+)\$", inline_math, text)
    text = re.sub(r"\\[A-Za-z]+", "", text)
    text = text.replace("{", "").replace("}", "").replace("_", "_")
    return re.sub(r"\s+", " ", text).strip()


def register_equation(value, number=None):
    key=f"EQ{len(EQUATIONS)+1:03d}"
    label_match=re.search(r"\\label\{([^}]+)\}",value)
    label=label_match.group(1) if label_match else None
    value=re.sub(r"\\label\{[^}]+\}","",value).strip()
    EQUATIONS[key]={"latex":value,"number":number,"label":label}
    return f"\n\n{key}\n\n"


def normalize_math(value):
    value=re.sub(r"\\textbf\{([^{}]+)\}",r"\\mathrm{\1}",value)
    value=value.replace(r"\textit",r"\mathrm").replace(r"\mathbb E",r"\mathbb{E}")
    value=value.replace(r"\qed","").replace("&","")
    value=re.sub(r"\\ge(?![A-Za-z])",r"\\geq",value); value=re.sub(r"\\le(?![A-Za-z])",r"\\leq",value)
    return re.sub(r"\s+"," ",value).strip().rstrip(";.")


def render_math(latex, key):
    import matplotlib.pyplot as plt
    EQUATION_DIR.mkdir(parents=True,exist_ok=True)
    rows=[x.strip() for x in re.split(r"\\\\",latex) if x.strip()]
    if r"\begin{pmatrix}" in latex:
        body=latex.split(r"\begin{pmatrix}",1)[1].split(r"\end{pmatrix}",1)[0]
        matrix_rows=[r.split("&") for r in body.split(r"\\")]
        prefix=latex.split(r"\begin{pmatrix}",1)[0]
        rows=[prefix+r"\left(\begin{array}{cc}"+" & ".join(r)+r"\end{array}\right)" for r in matrix_rows]
        # MathText lacks array environments; use aligned row notation while preserving every entry.
        rows=[prefix+"( "+" , ".join(matrix_rows[0])+" )", "( "+" , ".join(matrix_rows[1])+" )"]
    images=[]
    for i,row in enumerate(rows):
        row=normalize_math(row)
        path=EQUATION_DIR/f"{key}-{i+1}.png"
        fig=plt.figure(figsize=(7.0,.55)); fig.patch.set_alpha(0)
        fig.text(.5,.5,"$"+row+"$",ha="center",va="center",fontsize=13)
        fig.savefig(path,dpi=240,bbox_inches="tight",pad_inches=.04,transparent=True); plt.close(fig)
        images.append(Image(str(path),width=6.2*inch,height=.38*inch))
    return images


def parse():
    source = TEX.read_text(encoding="utf-8")
    appendix=(ROOT/"paper"/"appendix.tex").read_text(encoding="utf-8")
    source=source.replace(r"\input{appendix.tex}","\n"+appendix+"\n")
    counter={"n":0}
    def numbered(match):
        counter["n"]+=1
        return register_equation(match.group(1),counter["n"])
    source = re.sub(r"\\begin\{equation\}(.*?)\\end\{equation\}", numbered, source, flags=re.S)
    source = re.sub(r"\\begin\{align\}(.*?)\\end\{align\}", numbered, source, flags=re.S)
    source = re.sub(r"\\\[(.*?)\\\]", lambda m:register_equation(m.group(1)), source, flags=re.S)
    labels={v["label"]:v["number"] for v in EQUATIONS.values() if v["label"]}
    source=re.sub(r"\\eqref\{([^}]+)\}",lambda m:f"({labels.get(m.group(1),'?')})",source)
    source = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "", source, flags=re.S)
    source = re.sub(r"\\begin\{proposition\}(?:\[([^]]+)\])?(.*?)\\end\{proposition\}",
                    lambda m: "PROPOSITION" + (": " + m.group(1) if m.group(1) else "") + ". " + m.group(2), source, flags=re.S)
    source = re.sub(r"\\subsection\{([^}]+)\}",r"\n\nSUBSECTION: \1\n\n",source)
    source = source.replace(r"\qed", "End of proof.")
    title = re.search(r"\\title\{([^}]+)\}", source).group(1)
    author = re.search(r"\\author\{([^}]+)\}", source).group(1)
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", source, flags=re.S).group(1)
    body = source.split(r"\end{abstract}", 1)[1]
    sections = []
    matches = list(re.finditer(r"\\section\{([^}]+)\}", body))
    for i, match in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(body)
        chunk = body[match.end():end]
        paragraphs = [clean(x) for x in re.split(r"\n\s*\n", chunk) if clean(x)]
        sections.append((match.group(1), paragraphs))
    return title, author, clean(abstract), sections


def footer(canvas, doc):
    canvas.saveState(); canvas.setFont("Helvetica", 8); canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(.8*inch, .45*inch, "Persistent Records and Rehabilitation Incentives")
    canvas.drawRightString(7.7*inch, .45*inch, str(doc.page)); canvas.restoreState()


def main():
    title, author, abstract, sections = parse()
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="PaperTitle", parent=styles["Title"], fontName="Times-Bold", fontSize=20, leading=24, alignment=TA_CENTER, spaceAfter=18))
    styles.add(ParagraphStyle(name="PaperAuthor", parent=styles["Normal"], fontName="Times-Roman", fontSize=12, alignment=TA_CENTER, spaceAfter=18))
    styles.add(ParagraphStyle(name="PaperBody", parent=styles["BodyText"], fontName="Times-Roman", fontSize=10.2, leading=14.5, alignment=TA_JUSTIFY, spaceAfter=9))
    styles.add(ParagraphStyle(name="PaperH1", parent=styles["Heading1"], fontName="Times-Bold", fontSize=14, leading=17, spaceBefore=15, spaceAfter=8, textColor=colors.HexColor("#183153")))
    styles.add(ParagraphStyle(name="PaperAbstract", parent=styles["BodyText"], fontName="Times-Italic", fontSize=9.7, leading=13.5, alignment=TA_JUSTIFY, leftIndent=.35*inch, rightIndent=.35*inch, spaceAfter=14))
    doc = SimpleDocTemplate(str(PDF), pagesize=letter, rightMargin=.8*inch, leftMargin=.8*inch, topMargin=.72*inch, bottomMargin=.72*inch,
                            title=title, author=author, subject="Theory-first working paper")
    story = [Spacer(1,.25*inch), Paragraph(title,styles["PaperTitle"]), Paragraph(author,styles["PaperAuthor"]),
             Paragraph("September 2026 — Working Paper, External Review Version v0.1.0",styles["PaperAuthor"]),
             Paragraph("Abstract",styles["PaperH1"]), Paragraph(abstract,styles["PaperAbstract"])]
    figures = {"Lifecycle asymmetry":"m1_lifecycle_asymmetry.png", "Self-confirming and self-correcting regions":"m1_5_logistic_sign_map.png"}
    for heading, paragraphs in sections:
        story.append(Paragraph(heading, styles["PaperH1"]))
        for paragraph in paragraphs:
            if paragraph.startswith("PROPOSITION"):
                story.append(Paragraph("<b>"+escape(paragraph)+"</b>",styles["PaperBody"]))
            elif paragraph.startswith("SUBSECTION:"):
                story.append(Paragraph("<b>"+escape(paragraph.replace("SUBSECTION:","").strip())+"</b>",styles["PaperBody"]))
            elif paragraph in EQUATIONS:
                eq=EQUATIONS[paragraph]; imgs=render_math(eq["latex"],paragraph)
                for j,img in enumerate(imgs):
                    number=f"({eq['number']})" if eq["number"] and j==len(imgs)-1 else ""
                    table=Table([[img,number]],colWidths=[6.25*inch,.35*inch])
                    table.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                                               ("FONTNAME",(1,0),(1,0),"Times-Roman"),("FONTSIZE",(1,0),(1,0),9)]))
                    story.append(table)
            elif paragraph and not paragraph.startswith(("documentclass","usepackage","graphicspath","onehalfspacing","newtheorem","maketitle")):
                story.append(Paragraph(escape(paragraph),styles["PaperBody"]))
        if heading in figures:
            path=ROOT/"outputs"/"figures"/figures[heading]
            story.extend([Spacer(1,8),Image(str(path),width=5.7*inch,height=3.55*inch),Spacer(1,8)])
    story.extend([PageBreak(),Paragraph("References",styles["PaperH1"])])
    refs=[
      "Bhaskar, V., and C. Thomas (2019). Community Enforcement of Trust with Bounded Memory. Review of Economic Studies 86(3), 1010-1032.",
      "Board, S., and M. Meyer-ter-Vehn (2013). Reputation for Quality. Econometrica 81(6), 2381-2462.",
      "Bohren, J. A. (2024). Persistence in a Dynamic Moral Hazard Game. Theoretical Economics 19(1), 449-498.",
      "Elul, R., and P. Gottardi (2015). Bankruptcy: Is It Enough to Forgive or Must We Also Forget? AEJ: Microeconomics 7(4), 294-338.",
      "Jovanovic, B. (2021). Product Recalls and Firm Reputation. AEJ: Microeconomics 13(3), 404-442.",
      "Liu, Q., and A. Skrzypacz (2014). Limited Records and Reputation Bubbles. Journal of Economic Theory 151, 2-29.",
      "Pei, H. (forthcoming). Reputation Effects with Endogenous Records. American Economic Journal: Microeconomics.",
      "Sperisen, B. (2018). Bad Reputation under Bounded and Fading Memory. Economic Inquiry 56(1), 138-157.",
    ]
    for ref in refs: story.append(Paragraph(ref,styles["PaperBody"]))
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(PDF)


if __name__ == "__main__": main()
