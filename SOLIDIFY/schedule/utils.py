def recurrences_conflict(new_rule, existing_rule, new_date, existing_date):
    # Handle cases where one is non-repeating, the other is recurring
    if new_rule == 'none' and existing_rule != 'none':
        # One-time event vs recurring routine — test if the one-time event date matches recurrence
        return matches_recurrence(existing_rule, existing_date, new_date)

    if existing_rule == 'none' and new_rule != 'none':
        # Recurring new routine vs one-time existing routine
        return matches_recurrence(new_rule, new_date, existing_date)

    # Both are recurring
    if new_rule == 'daily' or existing_rule == 'daily':
        return True  # daily collides with anything if time overlaps

    if new_rule == existing_rule == 'weekly':
        return new_date.weekday() == existing_date.weekday()

    if new_rule == existing_rule == 'monthly':
        return new_date.day == existing_date.day

    if (new_rule == 'monthly' and existing_rule == 'weekly') or (
        new_rule == 'weekly' and existing_rule == 'monthly'):
        return new_date.weekday() == existing_date.weekday()

    return False



def matches_recurrence(rule, reference_date, test_date):
    """Returns True if test_date would match the recurrence pattern starting from reference_date."""
    if rule == 'daily':
        return True
    elif rule == 'weekly':
        return reference_date.weekday() == test_date.weekday()
    elif rule == 'monthly':
        return reference_date.day == test_date.day
    return False