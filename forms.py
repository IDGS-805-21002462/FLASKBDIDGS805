from wtforms import Form, PasswordField, HiddenField
from wtforms import IntegerField, StringField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = HiddenField("id")
    nombre = StringField("Nombre",[
        validators.DataRequired("Ingresa tu nombre"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    apellidos = StringField("apellidos",[
        validators.DataRequired("Ingresa tu Apellido Paterno"),
        validators.length(min=4, max=10, message="Ingresa un apellido Paterno valido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired("Ingresa tu Correo"),
        validators.Email(message="Ingresa un correo valido")
    ])

class UserForm2(Form):
    id=IntegerField("id")
    nombre = StringField("Nombre",[
        validators.DataRequired("Ingresa tu nombre"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    apellidos = StringField("apellidos",[
        validators.DataRequired("Ingresa tu Apellido Paterno"),
        validators.length(min=4, max=10, message="Ingresa un apellido Paterno valido")
    ])
    email = EmailField("Correo",[
        validators.DataRequired("Ingresa tu Correo"),
        validators.Email(message="Ingresa un correo valido")
    ])
    telefono = StringField("Telefono",[
        validators.DataRequired("Ingresa tu Telefono"),
        validators.length(min=10, max=10, message="Ingresa un telefono valido")
    ])

class MaestroForm(Form):
    id = IntegerField("id")
    nombre = StringField("Nombre",[
        validators.DataRequired("Ingresa tu nombre"),
        validators.length(min=4, max=50, message="Ingresa un nombre valido")
    ])
    apellidos = StringField("Apellidos",[
        validators.DataRequired("Ingresa tus Apellidos"),
        validators.length(min=4, max=50, message="Ingresa apellidos validos")
    ])
    email = EmailField("Correo",[
        validators.DataRequired("Ingresa tu Correo"),
        validators.Email(message="Ingresa un correo valido")
    ])
    especialidad = StringField("Especialidad",[
        validators.DataRequired("Ingresa tu Especialidad"),
        validators.length(min=4, max=50, message="Ingresa una especialidad valida")
    ])