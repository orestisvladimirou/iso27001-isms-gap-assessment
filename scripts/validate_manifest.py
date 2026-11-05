#!/usr/bin/env python3
"""Validate that the portable source manifest matches the committed project files."""
import hashlib
import json
from pathlib import Path
from validate_project import ROOT

SKIP={'.git','__pycache__','.pytest_cache'}

def inventory():
    result={}
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(x in SKIP for x in p.relative_to(ROOT).parts):
            continue
        if p.name=='PROJECT_MANIFEST.json' or p.suffix in ('.pyc','.pyo'):
            continue
        rel=p.relative_to(ROOT).as_posix()
        b=p.read_bytes()
        result[rel]={'sha256':hashlib.sha256(b).hexdigest(),'size':len(b)}
    return result

def validate_manifest():
    manifest=json.loads((ROOT/'PROJECT_MANIFEST.json').read_text(encoding='utf-8'))
    assert manifest['version']=='0.3'
    actual=inventory()
    listed={x['path']:{'sha256':x['sha256'],'size':x['size']} for x in manifest['files']}
    assert actual==listed, 'Manifest differs from current source; regenerate after controlled changes'
    print(f'PASS manifest: {len(actual)} source and workbook files match v0.3 checksums.')

if __name__=='__main__':validate_manifest()
