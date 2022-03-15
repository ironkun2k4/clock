"""
Enumerations for HTTP response codes and data fields
"""
# pylint: disable=R0903


class Http:
    """
    HTTP response codes
    """
    OK = 200
    CREATED = 201
    BAD = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404


class Attendance:
    """
    Attendance data fields
    """
    MEMBERSHIP_ID = 1003777
    FIRST_NAME = 1003903
    LAST_NAME = 1003904
    EID = 1003807
    OPPORTUNITY = 1003809
    TIMECLOCK_STATUS = 1010008
