import os

from reportlab.lib.pagesizes import letter, A4, inch, portrait, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import utils
from reportlab.platypus import Image, NextPageTemplate, \
    PageTemplate, BaseDocTemplate, Frame


class MyPrint:
    def __init__(self, buffer, pagesize, results):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.results = results
        self.width, self.height = portrait(self.pagesize)

    def generate_pdf(self):
        buffer = self.buffer
        doc = BaseDocTemplate(buffer,
                              rightMargin=0.3 * inch,
                              leftMargin=0.3 * inch,
                              topMargin=0.3 * inch,
                              bottomMargin=inch / 4,
                              )

        land_frame = Frame(0, 0, self.height, self.width, id='LFrame')
        land_frame._topPadding = 22
        land_frame._leftPadding = 11
        land_frame._bottomPadding = 22

        port_frame = Frame(0, 0, self.width, self.height, id='PFrame')
        port_frame._topPadding = 22
        port_frame._leftPadding = 11
        port_frame._bottomPadding = 22

        landscape_temp = PageTemplate(id='landscape_temp', frames=[land_frame, ], pagesize=landscape(self.pagesize))

        portrait_temp = PageTemplate(id='portrait_temp', frames=[port_frame, ], pagesize=self.pagesize)

        # Our container for 'Flowable' objects
        elements = []
        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        template_list = []
        for result in self.results:
            # image = 'http://127.0.0.1:8000' + result.image.url
            image = self.path_relative_to_file(__file__, '..' + result.image.url)
            # image = result.image.url
            im = self.scale_image(image)
            im.hAlign = 'CENTER'
            im.vAlign = 'MIDDLE'
            img = utils.ImageReader(image)
            width, height = img.getSize()

            if width > height:
                next_page = NextPageTemplate('landscape_temp')
                next_page.hAlign = 'CENTER'
                next_page.vAlign = 'MIDDLE'
                next_page.height = self.width
                next_page.width = self.height
                template_list.append(landscape_temp)
                elements.append(next_page)
            else:
                next_page = NextPageTemplate('portrait_temp')
                next_page.hAlign = 'CENTER'
                next_page.vAlign = 'MIDDLE'
                next_page.height = self.height
                next_page.width = self.width
                template_list.append(portrait_temp)
                elements.append(next_page)

            elements.append(im)
            #elements.append(PageBreak())

        doc.addPageTemplates(template_list)

        doc.build(elements)
        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

    def scale_image(self, fileish) -> Image:
        """ scales image with given width. fileish may be file or path """
        img = utils.ImageReader(fileish)
        orig_width, org_height = img.getSize()
        aspect = orig_width / org_height
        if orig_width > org_height > 529:
            height = 529
            if height * aspect > 792:
                width = 792
            else:
                width = height * aspect
        elif org_height > 792:
            height = 792
            if height * aspect > 529:
                width = 529
            else:
                width = height * aspect
        else:
            height = org_height
            width = height * aspect

        return Image(fileish, width=width, height=height)

    def path_relative_to_file(self, base_file_path, relative_path):
        base_dir = os.path.dirname(os.path.abspath(base_file_path))
        return os.path.normpath(os.path.join(base_dir, relative_path))

