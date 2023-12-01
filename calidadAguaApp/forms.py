from django import forms

class formularioAgregar(forms.Form):
    Nombre_Proyecto=forms.CharField(initial='Proyecto 1')
    Localidades=forms.CharField(initial='Localidad')
    Institucion_o_Empresa=forms.CharField(initial='Institucion o Empresa')
    Longitud=forms.IntegerField(initial='18.982928')

    Responsable=forms.CharField(initial='Responsable')
    Latitud=forms.IntegerField(initial='12.0394')
    Financiamiento=forms.CharField(initial='Financiamiento')
    Nombre_del_lugar_o_recurso=forms.CharField(initial='Nombre del lugar o recurso')

    Zona_o_Regiones=forms.CharField(initial='Zonas o Regiones')
    Tipos_de_fuente_o_recursos_hidricos=forms.CharField(initial='Tipos de fuente hidrica')
    
    Fecha=forms.DateField(initial='Seleccionar fecha', 
                        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),input_formats=["%Y-%m-%d"])
    Total_de_muestras_tomadas=forms.CharField(initial='Total muestras')
    Hora=forms.DateTimeField(initial='12:00',  # Hora inicial predeterminada
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=["%H:%M"])#, input_formats=[TIME_FORMAT],widget=TimePickerInput(format=TIME_FORMAT))
    email=forms.EmailField(initial='hola@dominnio.com')
   
    Descripcion_del_recurso_hidrico=forms.CharField(initial='Descripcion recurso hidrico')

