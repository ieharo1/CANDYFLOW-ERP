from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_type', models.CharField(choices=[('IN', 'Entrada'), ('OUT', 'Salida')], max_length=3)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='production.productionbatch')),
                ('candy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.candy')),
            ],
        ),
    ]
