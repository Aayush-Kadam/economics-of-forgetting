import re
from pathlib import Path

from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]


def test_manuscript_citations_are_defined():
    manuscript=(ROOT/"paper"/"manuscript.tex").read_text(encoding="utf-8")
    bibliography=(ROOT/"paper"/"references.bib").read_text(encoding="utf-8")
    cited={key for group in re.findall(r"\\cite[tp]\{([^}]+)\}",manuscript) for key in group.split(",")}
    defined=set(re.findall(r"@\w+\{([^,]+),",bibliography))
    assert cited <= defined


def test_release_pdf_has_expected_metadata_and_text():
    reader=PdfReader(ROOT/"paper"/"manuscript.pdf")
    assert len(reader.pages) >= 8
    assert reader.metadata.title == "Persistent Records and Rehabilitation Incentives"
    text="\n".join(page.extract_text() or "" for page in reader.pages)
    assert "Lifecycle asymmetry" in text
    assert "Adversarial robustness and limitations" in text
    assert "Aayush Kadam" in text
