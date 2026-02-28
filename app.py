from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from flask_migrate import Migrate
from maestros.routes import maestros
from models import db, Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
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
		return redirect(url_for('index'))
	alumnos = Alumnos.query.all()
	return render_template("index.html", form=create_form, alumnos=alumnos)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.route("/Alumnos", methods=["GET", "POST"])
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
		return redirect(url_for('index'))
	return render_template("Alumnos.html", form=create_form)

@app.route("/detalles", methods=["GET", "POST"])
def detalles():

	if request.method == 'GET':
		id=request.args.get('id')

		#select de alumno tomando un id
		alum1=db.session.query(Alumnos).filter(Alumnos.id == id).first()

		nombre=alum1.nombre
		apellidos=alum1.apellidos
		email=alum1.email
		telefono=alum1.telefono

		return render_template('detalles.html', id=id,nombre=nombre,apellidos=apellidos,email=email,telefono=telefono)


@app.route("/eliminar", methods=["GET", "POST"])
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
		return redirect(url_for('index'))
	return render_template("eliminar.html", form=create_form)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
	create_form = forms.UserForm2(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

		# Llenamos el formulario con los datos actuales
		if alum1:
			create_form.id.data = alum1.id
			create_form.nombre.data = alum1.nombre
			create_form.apellidos.data = alum1.apellidos
			create_form.email.data = alum1.email
			create_form.telefono.data = alum1.telefono

	# Entra aquí cuando el usuario envía el formulario
	if request.method == 'POST' and create_form.validate():
		id = create_form.id.data
		alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

		# Actualizamos el objeto con los datos nuevos que vienen del POST
		if alum:
			alum.nombre = create_form.nombre.data
			alum.apellidos = create_form.apellidos.data
			alum.email = create_form.email.data
			alum.telefono = create_form.telefono.data
			# Nota: db.session.add(alum) no es estrictamente necesario en una actualización si ya consultaste el objeto, pero no hace daño.
			db.session.commit()

		return redirect(url_for('index'))

	return render_template("modificar.html", form=create_form)

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()
