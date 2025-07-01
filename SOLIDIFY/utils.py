from django.utils.safestring import mark_safe

def helptext_to_ul(text):
    """
    Converts a multi-line string to a HTML unordered list.
    """
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    if not lines:
        return ""
    html = "<ul>\n" + "\n".join(f"<li>{line}</li>" for line in lines) + "\n</ul>"
    return mark_safe(html)
