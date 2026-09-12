from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor


class MappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id',
            'patient',
            'doctor',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_patient(self, patient):
        request = self.context['request']

        if patient.created_by != request.user:
            raise serializers.ValidationError(
                "You do not have permission to use this patient."
            )

        return patient

    def validate(self, data):
        patient = data['patient']
        doctor = data['doctor']

        if PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return data