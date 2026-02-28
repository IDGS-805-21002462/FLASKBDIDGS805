import forms
from . import maestros
from flask import render_template, request, redirect, url_for, flash
from models import db, Maestros

@maestros.route("/maestros", methods=["GET", "POST"])
def listado_maestros():
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaestros.html", maestros=maestros_list)

@maestros.route("/maestros/insertar", methods=["GET", "POST"])
def insertar_maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST' and create_form.validate():
        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            especialidad=create_form.especialidad.data
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))
    return render_template("maestros/insertar.html", form=create_form)

@maestros.route("/maestros/modificar", methods=["GET", "POST"])
def modificar_maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        if maestro:
            create_form.id.data = maestro.matricula
            create_form.nombre.data = maestro.nombre
            create_form.apellidos.data = maestro.apellidos
            create_form.email.data = maestro.email
            create_form.especialidad.data = maestro.especialidad

    if request.method == 'POST' and create_form.validate():
        id = create_form.id.data
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        if maestro:
            maestro.nombre = create_form.nombre.data
            maestro.apellidos = create_form.apellidos.data
            maestro.email = create_form.email.data
            maestro.especialidad = create_form.especialidad.data
            db.session.commit()
            return redirect(url_for('maestros.listado_maestros'))
    return render_template("maestros/modificar.html", form=create_form)

@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar_maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        if maestro:
            create_form.id.data = maestro.matricula
            create_form.nombre.data = maestro.nombre
            create_form.apellidos.data = maestro.apellidos
            create_form.email.data = maestro.email
            create_form.especialidad.data = maestro.especialidad

    if request.method == 'POST':
        id = create_form.id.data
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        if maestro:
            db.session.delete(maestro)
            db.session.commit()
            return redirect(url_for('maestros.listado_maestros'))
    return render_template("maestros/eliminar.html", form=create_form)

@maestros.route("/maestros/detalles", methods=["GET"])
def detalles_maestro():
    id = request.args.get('id')
    maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    if maestro:
        return render_template("maestros/detalles.html", 
                               id=maestro.matricula,
                               nombre=maestro.nombre,
                               apellidos=maestro.apellidos,
                               email=maestro.email,
                               especialidad=maestro.especialidad)
    return redirect(url_for('maestros.listado_maestros'))
