from django.db import models

APPOINTMENT_HOURS = (
    (1, '09:00'),
    (2, '09:30'),
    (3, '10:00'),
    (4, '10:30'),
    (5, '11:00'),
    (6, '11:30'),
    (7, '13:00'),
    (8, '13:30'),
    (9, '14:00'),
    (10, '14:30'),
    (11, '15:00'),
    (12, '15:30'),
    (13, '16:00'),
    (14, '16:30'),
)


class Employee(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    id_number = models.CharField(max_length=16)
    birthday = models.TextField(max_length=16)
    ssn = models.CharField(max_length=16) # ssk no


class Officer(models.Model):
    base = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Polyclinic(models.Model):
    name = models.TextField(max_length=128)
    address = models.TextField(max_length=128)


class Clinic(models.Model):
    polyclinic = models.ForeignKey(Polyclinic, on_delete=models.CASCADE)
    name = models.TextField(max_length=64)


class Doctor(Employee):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)


class Patient(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    id_number = models.CharField(max_length=16)
    birthday = models.TextField(max_length=16)
    ssn = models.CharField(max_length=16) # ssk no


class Register(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.TextField(max_length=16)
    hour = models.IntegerField(choices=APPOINTMENT_HOURS)


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)


class Prescription(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    meds = models.TextField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()


class Payment(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    price = models.FloatField()

