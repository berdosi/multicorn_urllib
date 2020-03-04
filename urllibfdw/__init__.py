"""Implement Foreign Data Wrapper for PostgreSQL with urllib"""
import urllib.request
from multicorn import ForeignDataWrapper

def data_download(url):
    """Return data downloaded from a URL"""
    with urllib.request.urlopen(url) as response:
        return {'url': url, 'response': response.read().decode('utf-8')}

class UrllibForeignDataWrapper(ForeignDataWrapper):
    """Foreign Data Wrapper class."""
    def __init__(self, options, columns):
        super(UrllibForeignDataWrapper, self).__init__(options, columns)
        self.columns = columns

    def execute(self, quals, columns):
        """This method yields the result records for a SELECT statement"""
        for qual in quals:
            yield data_download(qual.value)
