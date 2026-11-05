#!/usr/bin/env python3
"""Read-only OOXML check of the fictional v0.2 SoA companion workbook."""
import csv
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from validate_project import ROOT

P=ROOT/'phase2'/'SoA_Review_v0.2.xlsx'
NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

def validate_workbook():
    with (ROOT/'phase2/data/soa_applicability_review.csv').open(newline='',encoding='utf-8') as f:
        records=list(csv.DictReader(f))
    assert P.is_file(), 'SoA review workbook missing'
    with zipfile.ZipFile(P) as z:
        book=ET.fromstring(z.read('xl/workbook.xml'))
        sheets=[x.attrib['name'] for x in book.findall('.//'+NS+'sheet')]
        assert sheets==['Review Dashboard','SoA Register','Evidence Workstreams','Proposed Exclusions'],sheets
        shared=ET.fromstring(z.read('xl/sharedStrings.xml'))
        strings=[''.join(t.text or '' for t in item.findall('.//'+NS+'t')) for item in shared.findall(NS+'si')]
        register=ET.fromstring(z.read('xl/worksheets/sheet2.xml'))
        cells={c.attrib['r']:c for c in register.findall('.//'+NS+'c')}
        def read(ref):
            c=cells.get(ref)
            if c is None:return ''
            v=c.find(NS+'v')
            if v is None:return ''.join(x.text or '' for x in c.findall('.//'+NS+'t'))
            return strings[int(v.text)] if c.attrib.get('t')=='s' else v.text or ''
        assert len(records)==93
        for index,r in enumerate(records,2):
            assert read('A'+str(index))==r['control_id'], ('ID mismatch',index)
            assert read('D'+str(index))==r['necessity_decision'], ('Decision mismatch',index)
            assert read('F'+str(index))==r['implementation_status'], ('Status mismatch',index)
            assert read('E'+str(index))==r['inclusion_or_exclusion_reason'], ('Rationale mismatch',index)
        assert read('A94')==records[-1]['control_id']
        # The register's 2nd sheet includes 93 control rows, not baseline placeholders.
        assert not any(read('C'+str(i))=='Annex A control reference — review pending' for i in range(2,95))
        assert len(z.read('xl/worksheets/sheet1.xml'))>1000
    print('PASS workbook: 93 decisions and rationales match CSV, four review sheets, no baseline placeholders.')
    return True

if __name__=='__main__':validate_workbook()
