import operator
from functools import reduce

from databuilder.codes import ICD10Code
from databuilder.ehrql import case, when
from databuilder.tables.beta import tpp as schema
from databuilder.codes import Codelist


def first_matching_event(events, codelist, where=True):
    return (
        events.take(where)
        .take(events.snomedct_code.is_in(codelist))
        .sort_by(events.date)
        .first_for_patient()
    )


def last_matching_event(events, codelist, where=True):
    return (
        events.take(where)
        .take(events.snomedct_code.is_in(codelist))
        .sort_by(events.date)
        .last_for_patient()
    )


def age_as_of(date):
    return (date - schema.patients.date_of_birth).years


# TODO this is not exactly the same as died_from_any_cause().
# Note that this function only checks the patient table
def died_as_of(date):
    return schema.patients.date_of_death.is_not_null() & (
        schema.patients.date_of_death < date
    )


def _registrations_overlapping_period(start_date, end_date):
    regs = schema.practice_registrations
    return regs.take(
        regs.start_date.is_on_or_before(start_date)
        & (regs.end_date.is_after(end_date) | regs.end_date.is_null())
    )


def practice_registration_as_of(date):
    regs = _registrations_overlapping_period(date, date)
    return regs.sort_by(regs.start_date, regs.end_date).first_for_patient()
