from __future__ import unicode_literals

from collections import OrderedDict

from django.utils.encoding import force_text

from rest_framework import serializers
from rest_framework.utils.field_mapping import ClassLookupDict
from rest_framework.metadata import SimpleMetadata


class NgMetadata(SimpleMetadata):
    label_lookup = ClassLookupDict({
        serializers.Field: 'input',
        serializers.BooleanField: 'checkbox',
        serializers.NullBooleanField: 'checkbox',
        serializers.CharField: 'input',
        serializers.URLField: 'input',
        serializers.EmailField: 'input',
        serializers.RegexField: 'input',
        serializers.SlugField: 'input',
        serializers.IntegerField: 'input',
        serializers.FloatField: 'input',
        serializers.DecimalField: 'input',
        serializers.DateField: 'input',
        serializers.DateTimeField: 'input',
        serializers.TimeField: 'input',
        serializers.ChoiceField: 'input',
        serializers.MultipleChoiceField: 'input',
        serializers.FileField: 'input',
        serializers.ImageField: 'input',
        serializers.ListField: 'input',
        serializers.DictField: 'input',
        serializers.Serializer: 'nested object',
    })

    template_type_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'boolean',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'string',
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

    option_name_lookup = {
        'help_text': 'placeholder',
        'label': 'label',
    }

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
        field_info = OrderedDict([
            ('name', field_name),
            ('templateOptions', {}),
        ])
        field_info['type'] = self.label_lookup[field]
        field_info['templateOptions']['required'] = getattr(
            field, 'required', False)

        # attrs = [
        #     'read_only', 'label', 'help_text',
        #     'min_length', 'max_length',
        #     'min_value', 'max_value',
        # ]

        for src_attr, dest_attr in self.option_name_lookup.items():
            value = getattr(field, src_attr, None)
            if value is not None and value != '':
                field_info['templateOptions'][dest_attr] = force_text(
                    value, strings_only=True)

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
