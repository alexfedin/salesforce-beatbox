
from _beatbox import _tPartnerNS, _tSObjectNS, _tSoapNS, SoapFaultError, SessionTimeoutError
from _beatbox import Client as XMLClient
from python_client import Client as PythonClient

__all__ = ('XMLClient', '_tPartnerNS', '_tSObjectNS', '_tSoapNS', 'tests',
        'SoapFaultError', 'SessionTimeoutError', 'PythonClient')
