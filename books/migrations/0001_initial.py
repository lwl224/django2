# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 10:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Antenna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antennaid', models.CharField(max_length=50)),
                ('antennaid1', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('physicalstationid', models.CharField(max_length=20)),
                ('rruid', models.CharField(max_length=100)),
                ('cellid1', models.CharField(max_length=100)),
                ('directionangle', models.FloatField(blank=True, null=True)),
                ('antennaheight', models.FloatField(blank=True, null=True)),
                ('electricaldowntilt', models.CharField(max_length=20)),
                ('mechanicaltilt', models.CharField(max_length=20)),
                ('antennatypes', models.CharField(max_length=20)),
                ('beautifytypes', models.CharField(max_length=20)),
                ('antennafactory', models.CharField(max_length=100)),
                ('antennamodel', models.CharField(max_length=100)),
                ('antennanum', models.CharField(max_length=20)),
                ('horizontalpowerangle', models.CharField(max_length=20)),
                ('verticalpowerangle', models.CharField(max_length=20)),
                ('antennagain', models.CharField(max_length=20)),
                ('picture1', models.CharField(max_length=20)),
                ('picture2', models.CharField(max_length=20)),
                ('picture3', models.CharField(max_length=20)),
                ('picture4', models.CharField(max_length=20)),
                ('towermast', models.CharField(max_length=20)),
                ('txrxmod', models.CharField(max_length=20)),
                ('verticalrange', models.CharField(max_length=20)),
                ('install', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Bbu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbuid', models.CharField(max_length=50)),
                ('bbuname', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('factory', models.CharField(max_length=20)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('enodebid3', models.CharField(max_length=50)),
                ('physicalstationid', models.CharField(max_length=50)),
                ('unittype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Cell2scenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('scenesid', models.CharField(max_length=50)),
                ('cellid1', models.CharField(max_length=30)),
                ('networktype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Enodeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enodebname', models.CharField(max_length=60)),
                ('enodebomcidentify', models.CharField(max_length=60)),
                ('enodebomcname', models.CharField(max_length=60)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('villages', models.CharField(max_length=20)),
                ('enodebid', models.CharField(max_length=20)),
                ('enodebid2', models.CharField(max_length=20)),
                ('enodebid3', models.CharField(max_length=20)),
                ('enodebdn', models.CharField(max_length=20)),
                ('emsid', models.CharField(max_length=30)),
                ('mmeid', models.CharField(max_length=80)),
                ('sgwid', models.CharField(max_length=30)),
                ('factory', models.CharField(max_length=20)),
                ('worktypes', models.CharField(max_length=20)),
                ('antennanumb', models.CharField(max_length=20)),
                ('antennanumb2g', models.CharField(max_length=20)),
                ('antennanumb3g', models.CharField(max_length=20)),
                ('antennanumb23g', models.CharField(max_length=20)),
                ('physicalstationnumb', models.CharField(max_length=20)),
                ('physicalstationnumb2g', models.CharField(max_length=20)),
                ('physicalstationnumb3g', models.CharField(max_length=20)),
                ('physicalstationnumb23g', models.CharField(max_length=20)),
                ('sourcetypes', models.CharField(max_length=20)),
                ('commonmode', models.CharField(max_length=20)),
                ('unittype', models.CharField(max_length=50)),
                ('hwversion', models.CharField(max_length=50)),
                ('swversion', models.CharField(max_length=50)),
                ('swbugversion', models.CharField(max_length=50)),
                ('s1ubandwidth', models.CharField(max_length=20)),
                ('enodebbandwidth1', models.CharField(max_length=20)),
                ('enodebbandwidth2', models.CharField(max_length=20)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('Carrier', models.CharField(max_length=20)),
                ('Sectortype', models.CharField(max_length=20)),
                ('bbunumb', models.CharField(max_length=20)),
                ('rrunumb', models.CharField(max_length=20)),
                ('rrunumb24G', models.CharField(max_length=20)),
                ('repeater', models.CharField(max_length=20)),
                ('bstype', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('bslevel', models.CharField(max_length=20)),
                ('mcc', models.CharField(max_length=20)),
                ('mnc', models.CharField(max_length=20)),
                ('enodebcell', models.CharField(max_length=20)),
                ('enodebip', models.CharField(max_length=50)),
                ('towerdelivery', models.CharField(max_length=20)),
                ('towerlocation', models.CharField(max_length=20)),
                ('towerlevel', models.CharField(max_length=20)),
                ('sharetelecom', models.CharField(max_length=20)),
                ('builder', models.CharField(max_length=20)),
                ('share', models.CharField(max_length=20)),
                ('sharebs', models.CharField(max_length=20)),
                ('customize1', models.CharField(max_length=50)),
                ('customize2', models.CharField(max_length=50)),
                ('customize3', models.CharField(max_length=50)),
                ('customize4', models.CharField(max_length=50)),
                ('customize5', models.CharField(max_length=50)),
                ('customize6', models.CharField(max_length=50)),
                ('customize7', models.CharField(max_length=50)),
                ('customize8', models.CharField(max_length=50)),
                ('customize9', models.CharField(max_length=50)),
                ('customize10', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ltecell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellname', models.CharField(max_length=100)),
                ('cellid1', models.CharField(max_length=20)),
                ('cellomcname', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('villages', models.CharField(max_length=20)),
                ('enodebid', models.CharField(max_length=10)),
                ('cellid2', models.CharField(max_length=10)),
                ('sector', models.CharField(max_length=50)),
                ('eutranCellid', models.CharField(max_length=50)),
                ('factory', models.CharField(max_length=10)),
                ('villagestypes', models.CharField(max_length=10)),
                ('MR', models.CharField(max_length=10)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('antennaid', models.CharField(max_length=255)),
                ('antennanum', models.CharField(max_length=50)),
                ('worktypes', models.CharField(max_length=5)),
                ('cp', models.CharField(max_length=10)),
                ('subframe', models.CharField(max_length=10)),
                ('specificsubframe', models.CharField(max_length=10)),
                ('remoterru', models.CharField(max_length=20)),
                ('upfpoint', models.CharField(max_length=50)),
                ('downfpoint', models.CharField(max_length=50)),
                ('pci', models.CharField(max_length=50)),
                ('pcilist', models.CharField(max_length=50)),
                ('cellmaxpower', models.CharField(max_length=50)),
                ('rspower', models.CharField(max_length=50)),
                ('atypepower1', models.CharField(max_length=20)),
                ('btypepower1', models.CharField(max_length=10)),
                ('atypepower2', models.CharField(max_length=50)),
                ('btypepower2', models.CharField(max_length=10)),
                ('bcchpower', models.CharField(max_length=50)),
                ('maxpower', models.CharField(max_length=50)),
                ('tac', models.CharField(max_length=10)),
                ('taclist', models.CharField(max_length=10)),
                ('operation', models.CharField(max_length=20)),
                ('coveragetypes', models.CharField(max_length=20)),
                ('coveragerange', models.CharField(max_length=20)),
                ('plmn', models.CharField(max_length=20)),
                ('mbms', models.CharField(max_length=10)),
                ('band', models.CharField(max_length=10)),
                ('centerfrequency', models.CharField(max_length=10)),
                ('bandwidth', models.CharField(max_length=10)),
                ('downCyclicPrefix', models.CharField(max_length=20)),
                ('upCyclicPrefix', models.CharField(max_length=20)),
                ('upbandwidth', models.CharField(max_length=10)),
                ('downbandwidth', models.CharField(max_length=10)),
                ('astat', models.CharField(max_length=10)),
                ('hs', models.CharField(max_length=10)),
                ('txrxmod', models.CharField(max_length=20)),
                ('worktypes1', models.CharField(max_length=20)),
                ('leadingformat', models.CharField(max_length=20)),
                ('isblocking', models.CharField(max_length=10)),
                ('boundarycell', models.CharField(max_length=10)),
                ('boundaryname', models.CharField(max_length=10)),
                ('csbf', models.CharField(max_length=10)),
                ('hs2', models.CharField(max_length=10)),
                ('istelecom', models.CharField(max_length=10)),
                ('build', models.CharField(max_length=10)),
                ('sharingmode', models.CharField(max_length=10)),
                ('isca', models.CharField(max_length=10)),
                ('catypes', models.CharField(max_length=10)),
                ('catypeassociation', models.CharField(max_length=10)),
                ('camaincellid', models.CharField(max_length=20)),
                ('customize1', models.CharField(max_length=50)),
                ('customize2', models.CharField(max_length=50)),
                ('customize3', models.CharField(max_length=50)),
                ('customize4', models.CharField(max_length=50)),
                ('customize5', models.CharField(max_length=50)),
                ('customize6', models.CharField(max_length=50)),
                ('customize7', models.CharField(max_length=50)),
                ('customize8', models.CharField(max_length=50)),
                ('customize9', models.CharField(max_length=50)),
                ('customize10', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=16)),
                ('permission', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Physicalstation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physicalstationid', models.CharField(max_length=50)),
                ('physicalstationname', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('fulladdress', models.CharField(max_length=100)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('altitude', models.CharField(max_length=20)),
                ('isboundary', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Rru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rruid', models.CharField(max_length=50)),
                ('rruname', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('bbuid', models.CharField(max_length=50)),
                ('cellid1', models.CharField(max_length=50)),
                ('physicalstationid', models.CharField(max_length=50)),
                ('rrutypes', models.CharField(max_length=20)),
                ('rruport', models.CharField(max_length=20)),
                ('txrxtypes', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Scenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('scenesid', models.CharField(max_length=50)),
                ('scenesname', models.CharField(max_length=50)),
                ('parentscenes', models.CharField(max_length=50)),
                ('scenesdescription', models.CharField(max_length=1000)),
                ('scenesrange', models.CharField(max_length=3000)),
                ('sceneslon', models.FloatField(blank=True, null=True)),
                ('sceneslat', models.FloatField(blank=True, null=True)),
                ('firstscenes', models.CharField(max_length=50)),
                ('secondscenes', models.CharField(max_length=50)),
                ('hotregion', models.CharField(max_length=50)),
                ('vitalarea', models.CharField(max_length=50)),
                ('population', models.FloatField(blank=True, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('cell2g', models.CharField(max_length=50)),
                ('cell3g', models.CharField(max_length=50)),
                ('cell4g', models.CharField(max_length=50)),
                ('carrier2g', models.CharField(max_length=50)),
                ('carrier3g', models.CharField(max_length=50)),
                ('carrier4g', models.CharField(max_length=50)),
                ('fpoint2g', models.CharField(max_length=200)),
                ('fpoint3g', models.CharField(max_length=100)),
                ('fpoint4g', models.CharField(max_length=100)),
                ('mobilecover2g', models.CharField(max_length=50)),
                ('mobilecover3g', models.CharField(max_length=50)),
                ('mobilecover4g', models.CharField(max_length=50)),
                ('mobilefpoint', models.CharField(max_length=50)),
                ('telecomcover2g', models.CharField(max_length=50)),
                ('telecomcover3g', models.CharField(max_length=50)),
                ('telecomcover4g', models.CharField(max_length=50)),
                ('telecomfpoint', models.CharField(max_length=50)),
                ('sceneslevel', models.CharField(max_length=50)),
                ('customize1', models.CharField(max_length=50)),
                ('customize2', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher'),
        ),
    ]
