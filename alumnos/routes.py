import forms
from . import alumnos
from flask import render_template, request, redirect, url_for, flash
from models import db, Alumnos, Curso


@alumnos.route("/alumnos/index")
def index():
	create_form = forms.UserForm2(request.form)
	if request.method == 'POST' and create_form.validate():
		alum = Alumnos(
			nombre=create_form.nombre.data,
			apellidos=create_form.apellidos.data,
			email=create_form.email.data,
			telefono=create_form.telefono.data
		)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	alumnos = Alumnos.query.all()
	return render_template("alumnos/index.html", form=create_form, alumnos=alumnos)

@alumnos.route("/alumnos/Alumnos", methods=["GET", "POST"])
def alumnos_view():
	create_form = forms.UserForm2(request.form)
	if request.method == 'POST' and create_form.validate():
		alum = Alumnos(
			nombre=create_form.nombre.data,
			apellidos=create_form.apellidos.data,
			email=create_form.email.data,
			telefono=create_form.telefono.data
		)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/alumnos/detalles", methods=["GET", "POST"])
def detalles():

	if request.method == 'GET':
		id=request.args.get('id')

		#select de alumno tomando un id
		alum1=db.session.query(Alumnos).filter(Alumnos.id == id).first()

		todos_los_cursos = Curso.query.all()

		nombre=alum1.nombre
		apellidos=alum1.apellidos
		email=alum1.email
		telefono=alum1.telefono

		return render_template('alumnos/detalles.html',
							   alumno=alum1,
							   todos_los_cursos=todos_los_cursos)


@alumnos.route("/alumnos/eliminar", methods=["GET", "POST"])
def delete():
	create_form = forms.UserForm2(request.form)
	id = request.args.get('id')

	# select de alumno tomando un id
	alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

	create_form.id.data = alum1.id
	create_form.nombre.data = alum1.nombre
	create_form.apellidos.data = alum1.apellidos
	create_form.email.data = alum1.email
	create_form.telefono.data = alum1.telefono

	if request.method == 'POST':
		id=create_form.id.data
		alum = Alumnos.query.get(id)
		db.session.delete(alum)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/eliminar.html", form=create_form)

@alumnos.route("/alumnos/modificar", methods=["GET", "POST"])
def modificar():
	create_form = forms.UserForm2(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

		if alum1:
			create_form.id.data = alum1.id
			create_form.nombre.data = alum1.nombre
			create_form.apellidos.data = alum1.apellidos
			create_form.email.data = alum1.email
			create_form.telefono.data = alum1.telefono

	if request.method == 'POST' and create_form.validate():
		id = create_form.id.data
		alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

		if alum:
			alum.nombre = create_form.nombre.data
			alum.apellidos = create_form.apellidos.data
			alum.email = create_form.email.data
			alum.telefono = create_form.telefono.data
			db.session.commit()

		return redirect(url_for('alumnos.index'))

	return render_template("alumnos/modificar.html", form=create_form)


@alumnos.route("/inscribir", methods=["POST"])
def inscribir():
	id_alumno = request.form.get('alumno_id')
	id_curso = request.form.get('curso_id')

	alumno = Alumnos.query.get(id_alumno)
	curso = Curso.query.get(id_curso)

	if alumno and curso:
		if curso not in alumno.cursos:
			alumno.cursos.append(curso)
			db.session.commit()
			flash(f"¡Éxito! Inscrito en {curso.nombre}")
		else:
			flash("El alumno ya pertenece a este curso.")

	return redirect(url_for('cursos.detalles_curso', id=id_curso))
