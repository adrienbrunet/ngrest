from __future__ import unicode_literals

from collections import OrderedDict

from django.utils.encoding import force_text

from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.metadata import SimpleMetadata
from rest_framework.utils.field_mapping import ClassLookupDict


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
        serializers.ChoiceField: 'select',
        serializers.MultipleChoiceField: 'select',
        serializers.FileField: 'input',
        serializers.ImageField: 'input',
        serializers.ListField: 'input',
        serializers.DictField: 'input',
        serializers.Serializer: 'nested object',
        serializers.RelatedField: 'select',
    })

    template_type_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'boolean',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'text',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'regex',
        serializers.SlugField: 'slug',
        serializers.IntegerField: 'number',
        serializers.FloatField: 'float',
        serializers.DecimalField: 'decimal',
        serializers.DateField: 'date',
        serializers.DateTimeField: 'datetime-local',
        serializers.TimeField: 'time',
        serializers.ChoiceField: 'select',
        serializers.MultipleChoiceField: 'multiple choice',
        serializers.FileField: 'file upload',
        serializers.ImageField: 'image upload',
        serializers.ListField: 'list',
        serializers.DictField: 'nested object',
        serializers.Serializer: 'nested object',
        serializers.RelatedField: 'select',
    })

    option_name_lookup = {
        'help_text': 'description',
        'label': 'label',
        'min_value': 'min',
        'max_value': 'max',
    }

    def get_field_info(self, field):
        """
        Given an instance of a serializer field, return a dictionary
        of metadata about it.
        """
        template_options = {
            'required': getattr(field, 'required', False),
            'type': self.template_type_lookup[field],
        }
        field_info = OrderedDict([
            ('key', field.field_name),
            ('type', self.label_lookup[field]),
            ('hide', field.field_name in ['id', 'pk']),
            ('templateOptions', template_options),
        ])

        if field.default is not empty:
            field_info['defaultValue'] = getattr(field, 'default', None)

        for src_attr, dest_attr in self.option_name_lookup.items():
            value = getattr(field, src_attr, None)
            if value is not None and value != '':
                field_info['templateOptions'][dest_attr] = force_text(
                    value, strings_only=True)

        if getattr(field, 'child', None):
            field_info['child'] = self.get_field_info(field.child)
        elif getattr(field, 'fields', None):
            field_info['children'] = self.get_serializer_info(field)

        if (not field_info.get('read_only') and hasattr(field, 'choices')):
            field_info['templateOptions']['options'] = [
                {
                    'value': choice_value,
                    'name': force_text(choice_name, strings_only=True)
                }
                for choice_value, choice_name in field.choices.items()
            ]

        return field_info
