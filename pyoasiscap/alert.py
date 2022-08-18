"""
CAP v1.2
========

..  codeauthor:: Charles Blais
"""
from dataclasses import dataclass, field, asdict

from typing import Optional, List, Dict

from enum import Enum

from .info import Info


class Status(Enum):
    actual = 'Actual'
    exercise = 'Exercise'
    system = 'System'
    test = 'Test'
    draft = 'Draft'


class MsgType(Enum):
    alert = 'Alert'
    update = 'Update'
    cancel = 'Cancel'
    ack = 'Ack'
    error = 'Error'


class Scope(Enum):
    public = 'Public'
    restricted = 'Restricted'
    private = 'Private'


@dataclass
class Alert:
    class Meta:
        name = "alert"
        nillable = True
        namespace = "urn:oasis:names:tc:emergency:cap:1.2"

    identifier: str

    sender: str

    # important to note that format must be YYYY-mm-ddTHH:MM:SS+HH:MM
    # we have to use string since python datetime timezone offset doesn't
    # support HH:MM format
    sent: str

    status: Status

    msgType: MsgType

    source: Optional[str] = field(default=None)

    scope: Scope = field(default=Scope.private)

    restriction: Optional[str] = field(default=None)

    addresses: Optional[str] = field(default=None)

    code: Optional[List[str]] = field(default=None)

    note: Optional[str] = field(default=None)

    references: Optional[str] = field(default=None)

    incidents: Optional[str] = field(default=None)

    info: List[Info] = field(default_factory=list)

    def asdict(self) -> Dict:
        '''
        asdict is not able to convert enum there this routine will make sure
        this happens
        '''
        obj = asdict(self)
        obj['status'] = self.status.value
        obj['msgType'] = self.msgType.value
        obj['scope'] = self.scope.value
        for idx, info in enumerate(self.info):
            obj['info'][idx] = info.asdict()
        return obj

    def __post_init__(self):
        if isinstance(self.status, str):
            self.status = Status(self.status)
        if isinstance(self.msgType, str):
            self.msgType = MsgType(self.msgType)
        if isinstance(self.scope, str):
            self.scope = Scope(self.scope)
        if isinstance(self.info, list):
            self.info = [
                Info(**c) if isinstance(c, dict) else c
                for c in self.info
            ]
