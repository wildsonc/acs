from django.db import models
from django.utils import timezone


class Parameter(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=255, unique=True)
    writable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "parameters"
        ordering = ["path"]
        unique_together = [["name", "path"]]


class Model(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    parameters = models.ManyToManyField(Parameter, related_name="models")

    def __str__(self):
        return f"{self.name} -  {self.manufacturer}"

    class Meta:
        db_table = "models"
        ordering = ["created_at"]


class CPE(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    sn = models.CharField(max_length=12, db_index=True)
    parameters = models.JSONField(default=dict)
    manufacturer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(null=True)

    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name="cpes")

    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save(update_fields=["last_seen"])

    def __str__(self):
        return self.sn

    class Meta:
        db_table = "cpes"
        ordering = ["created_at"]
