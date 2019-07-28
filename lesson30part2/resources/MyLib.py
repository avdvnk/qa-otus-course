from AdminLogin import AdminLogin
from CustomerLogin import CustomerLogin


class MyLib(AdminLogin, CustomerLogin):
    def __init__(self):
        AdminLogin.__init__(self)
        CustomerLogin.__init__(self)
