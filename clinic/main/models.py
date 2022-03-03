from django.db import models

# Create your models here.


class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    clinic_name = models.CharField(max_length=200, null=False)
    clinic_address = models.CharField(max_length=500)


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=200, null=False)
    doctor_gender = models.CharField(max_length=20, null=False)
    doctor_email = models.EmailField(max_length=100, null=False)
    doctor_age = models.IntegerField(null=False)


class Assistant(models.Model):
    assistant_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assistant_name = models.CharField(max_length=200, null=False)
    assistant_gender = models.CharField(max_length=20, null=False)
    assistant_email = models.EmailField(max_length=100, null=False)
    assistant_age = models.IntegerField(null=False)
    patient_address = models.CharField(max_length=500)


class Patient(models.Model):
    patient_phone = models.CharField(max_length=20, primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=200, null=False)
    patient_gender = models.CharField(max_length=20, null=False)
    current_disease = models.CharField(max_length=1000)
    patient_email = models.EmailField(max_length=100, null=False)
    patient_age = models.IntegerField(null=False)
    patient_address = models.CharField(max_length=500)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=100 , null=False)
    patient_phone = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    checkup_type = models.CharField(max_length=25, null=False)
    completed = models.BooleanField(default=False)


class Labs(models.Model):
    Lab_id = models.AutoField(primary_key=True)
    patient_phone = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Lab_name = models.CharField(max_length=100, null=False)
    Lab_type = models.CharField(max_length=50, null=False)


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient_phone = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=200)
    drug_dose = models.CharField(max_length=100)
    drug_dosage_form = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    number_of_days = models.IntegerField()
    duration = models.CharField(max_length=50)
    instructions = models.CharField(max_length=500)


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient_phone = models.ForeignKey(Patient, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200, null=False)
    activity_price = models.IntegerField(null=False)
    total_price = models.IntegerField()


class Surgery(models.Model):
    surgery_id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    surgery_name = models.CharField(max_length=100, null=False)
    surgery_price = models.IntegerField(null=False)
    surgery_description = models.CharField(max_length=100, null=False)


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100, null=False)
    material_price = models.IntegerField( null=False)
    material_usage = models.CharField(max_length=200, null=False)


class Clinic_Phone(models.Model):
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    clinic_phone_id = models.AutoField(primary_key=True)
    clinic_phone = models.CharField(max_length=100, null=False)


