from __future__ import unicode_literals

import logging

from moto.core.models import HttprettyMockAWS

# Disable extra logging for tests
logging.getLogger('boto').setLevel(logging.CRITICAL)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('nose').setLevel(logging.CRITICAL)

orig_decorate_callable = HttprettyMockAWS.decorate_callable


def decorate_callable_with_attrib(*args, **kwargs):
    wrapper = orig_decorate_callable(*args, **kwargs)
    # Setting the attribute on wrapped functions (most are test cases) so
    # that boto2 tests can be skipped by adding `nosetests -a '!boto2_test'`
    # See: https://nose.readthedocs.io/en/latest/plugins/attrib.html
    wrapper.boto2_test = True
    return wrapper


HttprettyMockAWS.decorate_callable = decorate_callable_with_attrib
