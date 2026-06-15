import pypdf
r = pypdf.PdfReader('draf028.pdf')
print('Pages:', len(r.pages))
parts = []
for i in range(len(r.pages)):
    parts.append('=== PAGE ' + str(i+1) + ' ===')
    parts.append(r.pages[i].extract_text())
text = '\n'.join(parts)
with open('extract_all.txt', 'w', encoding='utf-8') as f:
    f.write(text)
import os
print('written, size:', os.path.getsize('extract_all.txt'))
