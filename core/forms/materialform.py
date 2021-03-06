# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.material import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

        widgets = {
            'material': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_mprima': forms.TextInput(attrs={'class':'form-control'}),
            'classificacao': forms.TextInput(attrs={'class':'form-control'}),
            'cor': forms.TextInput(attrs={'class':'form-control'}),
            'cod_mprima': forms.TextInput(attrs={'class':'form-control'}),
            'nome_fabricante': forms.TextInput(attrs={'class':'form-control'}),
            }
