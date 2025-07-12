from django import forms

class CoreModelFormMixin:
    unique_field_name = None            # e.g. 'category_type', 'habit_name', etc.
    unique_error_msg = None             # e.g. 'You already have a habit with this name.'
    user_field_name = 'user'            # Defaults to 'user'
    user_queryset_fields = []           # Fields to filter by user for dropdowns (e.g. ['category'])
    empty_labels = {}                   # e.g. {'category': "Select an existing category"}

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Set queryset and empty label for user-owned dropdowns
        for field in self.user_queryset_fields:
            if field in self.fields and self._user is not None:
                form_field = self.fields[field]
                # If ForeignKey, filter queryset by user
                if hasattr(form_field, "queryset"):
                    Model = form_field.queryset.model
                    form_field.queryset = Model.objects.filter(**{self.user_field_name: self._user})
                # If ChoiceField, set empty_label if needed
                elif field in self.empty_labels and hasattr(form_field, "empty_label"):
                    form_field.empty_label = self.empty_labels[field]
            # Always set empty_label, in case you want default text
            if field in self.empty_labels and field in self.fields and hasattr(self.fields[field], "empty_label"):
                self.fields[field].empty_label = self.empty_labels[field]

    def clean(self):
        cleaned_data = super().clean()
        user = self._user
        unique_value = cleaned_data.get(self.unique_field_name)
        if user and unique_value:
            Model = self._meta.model
            filter_kwargs = {
                self.user_field_name: user,
                self.unique_field_name: unique_value,
            }
            qs = Model.objects.filter(**filter_kwargs)
            # Exclude current instance on update
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error(self.unique_field_name, self.unique_error_msg)
        return cleaned_data
