import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate_workbook import validate_workbook
from validate_manifest import validate_manifest

class WorkbookAndManifestTests(unittest.TestCase):
    def test_workbook_rows_match_csv(self):
        self.assertTrue(validate_workbook())
    def test_manifest_hashes_match_source(self):
        validate_manifest()
