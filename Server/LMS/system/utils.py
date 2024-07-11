from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from system.models.Certificate import Certificate
def generate_pdf(path,context):
    template = get_template(path)
    html = template.render(context)
    res = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),res)
    return res 