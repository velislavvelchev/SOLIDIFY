import datetime
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def recurrences_conflict(
    new_rule, existing_rule,
    new_date, existing_date,
    new_interval=1, existing_interval=1
):
    if new_rule == 'none' and existing_rule != 'none':
        return matches_recurrence(existing_rule, existing_date, new_date, existing_interval)

    if existing_rule == 'none' and new_rule != 'none':
        return matches_recurrence(new_rule, new_date, existing_date, new_interval)

    # Both are recurring
    if new_rule == 'daily' and existing_rule == 'daily':
        return recurring_overlap_exists(new_date, new_interval, existing_date, existing_interval, unit='days')

    if new_rule == existing_rule == 'weekly':
        if new_date.weekday() != existing_date.weekday():
            return False
        return recurring_overlap_exists(new_date, new_interval, existing_date, existing_interval, unit='weeks')

    if new_rule == existing_rule == 'monthly':
        if new_date.day != existing_date.day:
            return False
        return recurring_overlap_exists(new_date, new_interval, existing_date, existing_interval, unit='months')


    # Different recurrence types — simulate daily alignment
    return recurring_overlap_exists(new_date, new_interval, existing_date, existing_interval, unit='days')


def recurring_overlap_exists(d1, i1, d2, i2, unit='days', max_span=365):
    """
    Simulate recurrence dates up to `max_span` units and check for any shared date.
    """
    get_date = lambda base, step, n: base + datetime.timedelta(days=step * n)

    if unit == 'weeks':
        i1, i2 = i1 * 7, i2 * 7
    elif unit == 'months':
        # Simple approximation — check same day in each month up to `max_span`
        dates_a = set(add_months(d1.date(), i1 * n) for n in range(max_span // i1 + 1))
        dates_b = set(add_months(d2.date(), i2 * n) for n in range(max_span // i2 + 1))
        return bool(dates_a & dates_b)

    # For 'days' and 'weeks' (already converted)
    dates_a = set(get_date(d1.date(), i1, n) for n in range(max_span // i1 + 1))
    dates_b = set(get_date(d2.date(), i2, n) for n in range(max_span // i2 + 1))
    return bool(dates_a & dates_b)


def add_months(date_obj, months):
    year = date_obj.year + (date_obj.month - 1 + months) // 12
    month = (date_obj.month - 1 + months) % 12 + 1
    day = min(date_obj.day, [31,
        29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return datetime.date(year, month, day)


def matches_recurrence(rule, reference_date, test_date, interval=1):
    if rule == 'daily':
        delta_days = (test_date.date() - reference_date.date()).days
        return delta_days % interval == 0 and delta_days >= 0

    elif rule == 'weekly':
        if test_date.weekday() != reference_date.weekday():
            return False
        delta_weeks = (test_date.date() - reference_date.date()).days // 7
        return delta_weeks % interval == 0 and delta_weeks >= 0

    elif rule == 'monthly':
        if test_date.day != reference_date.day:
            return False
        delta_months = (test_date.year - reference_date.year) * 12 + (test_date.month - reference_date.month)
        return delta_months % interval == 0 and delta_months >= 0

    return False
