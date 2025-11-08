from enum import Enum


class IncidentSource(str, Enum):
    OPERATOR = "OPERATOR"
    MONITORING = "MONITORING"
    PARTNER = "PARTNER"
