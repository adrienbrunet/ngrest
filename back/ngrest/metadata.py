from __future__ import unicode_literals

from collections import OrderedDict

from django.utils.encoding import force_text

from rest_framework import serializers
from rest_framework.utils.field_mapping import ClassLookupDict
from rest_framework.metadata import SimpleMetadata


class NgMetadata(SimpleMetadata):
    label_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'boolean',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'input',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'regex',
        serializers.SlugField: 'slug',
        serializers.IntegerField: 'integer',
        serializers.FloatField: 'float',
        serializers.DecimalField: 'decimal',
        serializers.DateField: 'date',
        serializers.DateTimeField: 'datetime',
        serializers.TimeField: 'time',
        serializers.ChoiceField: 'choice',
        serializers.MultipleChoiceField: 'multiple choice',
        serializers.FileField: 'file upload',
        serializers.ImageField: 'image upload',
        serializers.ListField: 'list',
        serializers.DictField: 'nested object',
        serializers.Serializer: 'nested object',
    })

    def get_serializer_info(self, serializer):
        """
        Given an instance of a serializer, return a dictionary of metadata
        about its fields.
        """
        if hasattr(serializer, 'child'):
            # If this is a `ListSerializer` then we want to examine the
            # underlying child serializer instance instead.
            serializer = serializer.child
        return [
            self.get_field_info(field, field_name)
            for field_name, field in serializer.fields.items()
        ]

    def get_field_info(self, field, field_name):
        """
        Given an instance of a serializer field, return a dictionary
        of metadata about it.
        """
        field_info = OrderedDict([('name', field_name)])
        field_info['type'] = self.label_lookup[field]
        # field_info['required'] = getattr(field, 'required', False)

        attrs = [
            # 'read_only', 'label', 'help_text',
            # 'min_length', 'max_length',
            # 'min_value', 'max_value',
        ]

        for attr in attrs:
            value = getattr(field, attr, None)
            if value is not None and value != '':
                field_info[attr] = force_text(value, strings_only=True)

        if getattr(field, 'child', None):
            field_info['child'] = self.get_field_info(field.child)
        elif getattr(field, 'fields', None):
            field_info['children'] = self.get_serializer_info(field)

        if (not field_info.get('read_only') and
            not isinstance(field, (serializers.RelatedField, serializers.ManyRelatedField)) and
                hasattr(field, 'choices')):
            field_info['choices'] = [
                {
                    'value': choice_value,
                    'display_name': force_text(choice_name, strings_only=True)
                }
                for choice_value, choice_name in field.choices.items()
            ]

        return field_info
