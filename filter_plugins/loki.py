# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import re
from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'loki_checksum': self.checksum,
            'loki_tls_certificates': self.tls_certificates,
            'loki_value': self.value,
        }

    def checksum(self, data, program, os, arch):
        """
        """
        checksum = None

        if isinstance(data, list):
            # filter OS
            # linux = [x for x in data if re.search(r"{}-{}.*.zip".format(program, os), x)]
            # filter OS and ARCH
            checksum = [x for x in data if re.search(r"{}-{}-{}.zip".format(program, os, arch), x)][0]

        if isinstance(checksum, str):
            checksum = checksum.split(" ")[0]

        display.v("= checksum: {}".format(checksum))

        return checksum

    def tls_certificates(self, data):
        """
        """
        if isinstance(data, dict):
            cert_file = data.get("cert_file", None)
            key_file = data.get("key_file", None)

            if cert_file and key_file:
                return True

        return False

    def value(self, data):
        """
        """
        result = None
        # display.v(f"value({data} {type(data)})")

        if isinstance(data, bool):
            result = 'true' if data else 'false'
        elif isinstance(data, str):
            if len(data) > 0:
                result = data
        elif isinstance(data, int):
            result = data

        # display.v(f"= result: {result} {type(result)}")

        return result
