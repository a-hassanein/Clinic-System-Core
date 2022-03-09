from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=200, null=False)
    doctor_gender = models.CharField(max_length=20, null=False)
    doctor_email = models.EmailField(max_length=100, null=False)
    doctor_age = models.IntegerField(null=False)
    doctor_password = models.CharField(null=False, max_length=300)
    doctor_confirm_password = models.CharField(null=False, max_length=300)



class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic_name = models.CharField(max_length=200, null=False)
    clinic_address = models.CharField(max_length=500)



class Assistant(models.Model):
    assistant_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assistant_name = models.CharField(max_length=200, null=False)
    assistant_gender = models.CharField(max_length=20, null=False)
    assistant_email = models.EmailField(max_length=100, null=False)
    assistant_age = models.CharField(max_length=5, null=False)
    assistant_address = models.CharField(max_length=500)
    assistant_number = models.CharField(max_length=11, null=False)
    assistant_pass = models.CharField(max_length=200, null=False)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_phone = models.CharField(max_length=20, unique=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=200, null=False)
    patient_gender = models.CharField(max_length=20, null=False)
    current_disease = models.CharField(max_length=1000)
    patient_email = models.EmailField(max_length=100, null=False)
    patient_age = models.IntegerField(null=False)
    patient_address = models.CharField(max_length=500)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100 , null=False)
    patient_phone = models.CharField(max_length=25 , null=False)
    appointment_date = models.DateTimeField(null=False)
    checkup_type = models.CharField(max_length=25, null=False)
    completed = models.BooleanField(default=False)



class Labs(models.Model):
    Lab_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Lab_name = models.CharField(max_length=100, null=False)


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=200, null=True)
    drug_dose = models.CharField(max_length=100, null=True)
    drug_dosage_form = models.CharField(max_length=100, null=True)
    frequency = models.CharField(max_length=100, null=True)
    number_of_days = models.IntegerField(null=True)
    duration = models.CharField(max_length=50, null=True)
    instructions = models.CharField(max_length=500, null=True)


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200, null=False)
    activity_price = models.IntegerField(null=False)
    total_price = models.IntegerField(null=True)


class Surgery(models.Model):
    surgery_id = models.AutoField(primary_key=True)
    surgery_name = models.CharField(max_length=100, null=False)
    surgery_price = models.IntegerField(null=False)
    surgery_description = models.CharField(max_length=100, null=False)


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=100, null=False)
    material_price = models.IntegerField(null=False)
    material_usage = models.CharField(max_length=200, null=False)


class Clinic_Phone(models.Model):
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    clinic_phone_id = models.AutoField(primary_key=True)
    clinic_phone = models.CharField(max_length=100, null=False)


