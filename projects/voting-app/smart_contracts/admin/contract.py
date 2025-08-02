from algopy import Account, ARC4Contract, GlobalState, String, Txn
from algopy.arc4 import abimethod

from .constants import error_messages as ERROR_MESSAGES


class Admin(ARC4Contract):
    def __init__(self) -> None:
        self.global_admin = GlobalState(Account(Txn.sender.bytes))

    @abimethod(allow_actions=["UpdateApplication"])
    def update(self) -> None:
        assert Txn.sender == self.global_admin.get(
            Account()
        ), ERROR_MESSAGES.UNAUTHORIZED

    @abimethod(allow_actions=["DeleteApplication"])
    def delete(self) -> None:
        assert Txn.sender == self.global_admin.get(
            Account()
        ), ERROR_MESSAGES.UNAUTHORIZED

    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello, " + name
