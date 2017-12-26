from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import os
from ansible.plugins.lookup import LookupBase
from ansible.module_utils._text import to_text

class LookupModule(LookupBase):

   def run(self, terms=None, variables=None, **kwargs):
        out = []
        for term in terms:
            temp = os.uname()
            out.append("OS: "+temp[0])
            out.append(" Hostname: "+temp[1])
            out.append(" Kernel version: "+temp[2])


        return out

