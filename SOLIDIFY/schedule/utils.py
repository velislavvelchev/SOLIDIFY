def recurrences_conflict(new_rule, existing_rule, new_date, existing_date):
    if new_rule == 'none' or existing_rule == 'none':
        return False  # already caught by datetime overlap, skip here

    if new_rule == 'daily' or existing_rule == 'daily':
        return True  # daily conflicts with anything if time overlaps

    if new_rule == existing_rule == 'weekly':
        return new_date.weekday() == existing_date.weekday()

    if new_rule == existing_rule == 'monthly':
        return new_date.day == existing_date.day

    if (new_rule == 'monthly' and existing_rule == 'weekly') or (
            new_rule == 'weekly' and existing_rule == 'monthly'):
        return new_date.weekday() == existing_date.weekday()

    return False