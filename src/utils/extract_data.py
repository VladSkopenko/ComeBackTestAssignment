from io import BytesIO

from docx import Document


def extract_data_from_docx(file_content):
    doc = Document(BytesIO(file_content))

    title = ""
    authors = ""
    affiliations = ""
    abstract = ""
    keywords = ""
    main_text = []
    references = []

    for para in doc.paragraphs:
        if not title and para.text.strip():
            title = para.text.strip()
        elif "Authors:" in para.text:
            authors = para.text.replace("Authors:", "").strip()
        elif "Affiliations:" in para.text:
            affiliations = para.text.replace("Affiliations:", "").strip()
        elif "Abstract:" in para.text:
            abstract = para.text.replace("Abstract:", "").strip()
        elif "Keywords:" in para.text:
            keywords = para.text.replace("Keywords:", "").strip()
        elif para.text.strip():
            main_text.append({
                "title": para.text.strip(),
                "content": para.text.strip(),
                "level": 1
            })
        elif "References:" in para.text:
            references.append(para.text.strip())

    return {
        "title": title,
        "authors": authors,
        "affiliations": affiliations,
        "abstract": abstract,
        "keywords": keywords,
        "main_text": main_text,
        "references": references
    }
