from django import forms

class formularioAgregar(forms.Form):
    Nombre_Proyecto=forms.CharField()
    INstitucion_o_Empresa=forms.CharField()
    Responsable=forms.CharField()
    Financiamiento=forms.CharField()
    Zona_o_Regiones=forms.CharField()
    Fecha=forms.DateField()
    Hora=forms.DateField()
    email=forms.EmailField()
    mensaje=forms.CharField()
    Localidades=forms.CharField()
    Longitud=forms.IntegerField()
    Latitud=forms.IntegerField()
    Nombre_del_lugar_o_recurso=forms.CharField()
    Tipos_de_fuente_o_recursos_hidricos=forms.CharField()
    Total_de_muestras_tomadas=forms.CharField()
    Descripcion_del_recurso_hidrico=forms.CharField()

