2010.05.06 
�ץ� PDF-XChange Viewer �s�ɫ�N

>>
startxref
45123248
%%EOF

�ܦ�

>>
startxref 45123248
%%EOF

�ɭP pdf.py �B�z�W�����~�A�]���ק令
        try:
            startxref = int(line)
            line = self.readNextEndLine(stream)
            if line[:9] != "startxref":
                raise utils.PdfReadError, "startxref not found"
        except ValueError:
            # FIX: startxref 45123248
            a,v = line.split(' ')
            startxref = int(v)


