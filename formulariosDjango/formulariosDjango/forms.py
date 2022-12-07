from django import forms 

class CommentForm(forms.Form):
    name = forms.CharField(label='Escribe tu nombre', max_length=10, help_text='Máximo 10 caracteres')
    url = forms.URLField(label='Tu sitio web', required=False, initial='https://')
    comment = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=15, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email', 
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Definimos validaciones extra
    def clean_name(self):
        # Asignamos al nombre los datos limpios, 
        # una vez ya han pasado la validación estándar
        name = self.cleaned_data.get("name")

        # Añadimos la validación adicional
        if name != "Franky":
            raise forms.ValidationError('El único valor permitido es "Franky"')
        else:
            return name

