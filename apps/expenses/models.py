from django.db import models
from apps.vehicles.models import Vehicle
from apps.common.models import IsDeletedModel


class Expense(IsDeletedModel):
    expense_date = models.DateField(
        verbose_name="Дата расхода",
        help_text="Дата совершения расхода"
    )
    category = models.CharField(
        max_length=50,
        verbose_name="Категория",
        help_text="Тип расхода"
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='expenses',
        null=True,
        blank=True,
        verbose_name="Транспортное средство",
        help_text="Транспорт, связанный с расходом (если применимо)"
    )
    responsible_person = models.CharField(
        max_length=255,
        verbose_name="Ответственное лицо",
        help_text="Кто произвел или согласовал расход"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма",
        help_text="Сумма расхода (в рублях)"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Подробное описание расхода"
    )

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"
        ordering = ['-expense_date']

    def __str__(self):
        return f"Расход {self.get_category_display()} - {self.expense_date} ({self.amount}₽)"
