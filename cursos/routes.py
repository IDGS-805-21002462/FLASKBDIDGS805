from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Curso, Maestros
import forms
from . import cursos


@cursos.route("/cursos", methods=["GET", "POST"])
def index():
    cursos_list = Curso.query.all()
    return render_template("cursos/listadoCursos.html", cursos=cursos_list)

@cursos.route("/cursos/insertar", methods=["GET", "POST"])
def insertar_curso():
    create_form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros]

    if request.method == 'POST' and create_form.validate():
        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template("cursos/insertar.html", form=create_form)

@cursos.route("/cursos/modificar", methods=["GET", "POST"])
def modificar_curso():
    create_form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros]

    if request.method == 'GET':
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        if curso:
            create_form.id.data = curso.id
            create_form.nombre.data = curso.nombre
            create_form.descripcion.data = curso.descripcion
            create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST' and create_form.validate():
        id = create_form.id.data
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        if curso:
            curso.nombre = create_form.nombre.data
            curso.descripcion = create_form.descripcion.data
            curso.maestro_id = create_form.maestro_id.data
            db.session.commit()
            return redirect(url_for('cursos.index'))
    return render_template("cursos/modificar.html", form=create_form)

@cursos.route("/cursos/eliminar", methods=["GET", "POST"])
def eliminar_curso():
    create_form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros]

    if request.method == 'GET':
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        if curso:
            create_form.id.data = curso.id
            create_form.nombre.data = curso.nombre
            create_form.descripcion.data = curso.descripcion
            create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST':
        id = create_form.id.data
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        if curso:
            db.session.delete(curso)
            db.session.commit()
            return redirect(url_for('cursos.index'))
    return render_template("cursos/eliminar.html", form=create_form)

@cursos.route("/cursos/detalles", methods=["GET"])
def detalles_curso():
    id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == id).first()
    if curso:
        return render_template("cursos/detalles.html", curso=curso)
    return redirect(url_for('cursos.index'))
