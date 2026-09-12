from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            'id',
            'name',
            'age',
            'gender',
            'phone',
            'address',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_age(self, value):
        if value < 0 or value > 150:
            raise serializers.ValidationError(
                "Age must be between 0 and 150."
            )
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value