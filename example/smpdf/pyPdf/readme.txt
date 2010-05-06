2010.05.06 
修正 PDF-XChange Viewer 存檔後將

>>
startxref
45123248
%%EOF

變成

>>
startxref 45123248
%%EOF

導致 pdf.py 處理上的錯誤，因此修改成
        try:
            startxref = int(line)
            line = self.readNextEndLine(stream)
            if line[:9] != "startxref":
                raise utils.PdfReadError, "startxref not found"
        except ValueError:
            # FIX: startxref 45123248
            a,v = line.split(' ')
            startxref = int(v)


