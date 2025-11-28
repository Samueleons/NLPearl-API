# __init__.py
from .account import Account
from .call import Call
from .inbound import Inbound
from .outbound import Outbound
from .pearl import Pearl

# Global API key variable
api_key = None

# Global API version variable (default is v2)
api_version = "v2"