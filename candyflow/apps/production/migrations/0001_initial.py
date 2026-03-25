from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, unique=True)),
                ('production_date', models.DateField()),
                ('quantity_produced', models.DecimalField(decimal_places=2, max_digits=10)),
                ('labor_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('overhead_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('candy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.candy')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=120)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_items', to='production.productionbatch')),
            ],
        ),
    ]
