from datetime import datetime
import json
import os
import random
import string
from flask import Flask, redirect, render_template, request, send_file, url_for, Response
import flask
from flask_sqlalchemy import SQLAlchemy
import sys

import requests
import io

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))

if 'PRODUCTION' in os.environ:
    print(1)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////var/www/harrysmith/harrysmith/utils/app.db"
    app.config["UPLOAD_FOLDER"] = "/var/www/harrysmith/harrysmith/images"

    app.config['SQLALCHEMY_BINDS'] = {
    "db": "sqlite:////var/www/harrysmith/harrysmith/utils/dataset.db"
}
elif 'TEST' in os.environ:
    print(2)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////var/www/harrysmith/harrysmith/utils/app.db"
    app.config["UPLOAD_FOLDER"] = "/var/www/harrysmith/harrysmith/images"

    app.config['SQLALCHEMY_BINDS'] = {
    "db": "sqlite:////var/www/harrysmith/harrysmith/utils/dataset.db"
}
else:
    print(3)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///utils/app.db"
    app.config["UPLOAD_FOLDER"] = dir_path+"\\images"

    app.config['SQLALCHEMY_BINDS'] = {
    "db": "sqlite:///utils/dataset.db"
}

app.config["MAX_CONTENT_PATH"] = 50 * 1024 * 1024
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

######################################
### STARTING MODELS FOR ASSIGNMENT ###
######################################
class en(db.Model):
    __bind_key__ = "db"
    year = db.Column('year', db.Integer, primary_key = True)
    minRainfall = db.Column(db.Float)
    maxRainfall = db.Column(db.Float)
    minSunshine = db.Column(db.Float)
    maxSunshine = db.Column(db.Float)
    minLowTemp = db.Column(db.Float)
    maxLowTemp = db.Column(db.Float)
    minHighTemp = db.Column(db.Float)
    maxHighTemp = db.Column(db.Float)
    avgRainfall = db.Column(db.Float)
    avgSunshine = db.Column(db.Float)
    avgLowTemp = db.Column(db.Float)
    avgHighTemp = db.Column(db.Float)

    janRainfall = db.Column(db.Float)
    febRainfall = db.Column(db.Float)
    marRainfall = db.Column(db.Float)
    aprRainfall = db.Column(db.Float)
    mayRainfall = db.Column(db.Float)
    junRainfall = db.Column(db.Float)
    julRainfall = db.Column(db.Float)
    augRainfall = db.Column(db.Float)
    sepRainfall = db.Column(db.Float)
    octRainfall = db.Column(db.Float)
    novRainfall = db.Column(db.Float)
    decRainfall = db.Column(db.Float)

    janSunshine = db.Column(db.Float)
    febSunshine = db.Column(db.Float)
    marSunshine = db.Column(db.Float)
    aprSunshine = db.Column(db.Float)
    maySunshine = db.Column(db.Float)
    junSunshine = db.Column(db.Float)
    julSunshine = db.Column(db.Float)
    augSunshine = db.Column(db.Float)
    sepSunshine = db.Column(db.Float)
    octSunshine = db.Column(db.Float)
    novSunshine = db.Column(db.Float)
    decSunshine = db.Column(db.Float)

    janLowTemp = db.Column(db.Float)
    febLowTemp = db.Column(db.Float)
    marLowTemp = db.Column(db.Float)
    aprLowTemp = db.Column(db.Float)
    mayLowTemp = db.Column(db.Float)
    junLowTemp = db.Column(db.Float)
    julLowTemp = db.Column(db.Float)
    augLowTemp = db.Column(db.Float)
    sepLowTemp = db.Column(db.Float)
    octLowTemp = db.Column(db.Float)
    novLowTemp = db.Column(db.Float)
    decLowTemp = db.Column(db.Float)

    janHighTemp = db.Column(db.Float)
    febHighTemp = db.Column(db.Float)
    marHighTemp = db.Column(db.Float)
    aprHighTemp = db.Column(db.Float)
    mayHighTemp = db.Column(db.Float)
    junHighTemp = db.Column(db.Float)
    julHighTemp = db.Column(db.Float)
    augHighTemp = db.Column(db.Float)
    sepHighTemp = db.Column(db.Float)
    octHighTemp = db.Column(db.Float)
    novHighTemp = db.Column(db.Float)
    decHighTemp = db.Column(db.Float)

class sc(db.Model):
    __bind_key__ = "db"
    year = db.Column('year', db.Integer, primary_key = True)
    minRainfall = db.Column(db.Float)
    maxRainfall = db.Column(db.Float)
    minSunshine = db.Column(db.Float)
    maxSunshine = db.Column(db.Float)
    minLowTemp = db.Column(db.Float)
    maxLowTemp = db.Column(db.Float)
    minHighTemp = db.Column(db.Float)
    maxHighTemp = db.Column(db.Float)
    avgRainfall = db.Column(db.Float)
    avgSunshine = db.Column(db.Float)
    avgLowTemp = db.Column(db.Float)
    avgHighTemp = db.Column(db.Float)

    janRainfall = db.Column(db.Float)
    febRainfall = db.Column(db.Float)
    marRainfall = db.Column(db.Float)
    aprRainfall = db.Column(db.Float)
    mayRainfall = db.Column(db.Float)
    junRainfall = db.Column(db.Float)
    julRainfall = db.Column(db.Float)
    augRainfall = db.Column(db.Float)
    sepRainfall = db.Column(db.Float)
    octRainfall = db.Column(db.Float)
    novRainfall = db.Column(db.Float)
    decRainfall = db.Column(db.Float)

    janSunshine = db.Column(db.Float)
    febSunshine = db.Column(db.Float)
    marSunshine = db.Column(db.Float)
    aprSunshine = db.Column(db.Float)
    maySunshine = db.Column(db.Float)
    junSunshine = db.Column(db.Float)
    julSunshine = db.Column(db.Float)
    augSunshine = db.Column(db.Float)
    sepSunshine = db.Column(db.Float)
    octSunshine = db.Column(db.Float)
    novSunshine = db.Column(db.Float)
    decSunshine = db.Column(db.Float)

    janLowTemp = db.Column(db.Float)
    febLowTemp = db.Column(db.Float)
    marLowTemp = db.Column(db.Float)
    aprLowTemp = db.Column(db.Float)
    mayLowTemp = db.Column(db.Float)
    junLowTemp = db.Column(db.Float)
    julLowTemp = db.Column(db.Float)
    augLowTemp = db.Column(db.Float)
    sepLowTemp = db.Column(db.Float)
    octLowTemp = db.Column(db.Float)
    novLowTemp = db.Column(db.Float)
    decLowTemp = db.Column(db.Float)

    janHighTemp = db.Column(db.Float)
    febHighTemp = db.Column(db.Float)
    marHighTemp = db.Column(db.Float)
    aprHighTemp = db.Column(db.Float)
    mayHighTemp = db.Column(db.Float)
    junHighTemp = db.Column(db.Float)
    julHighTemp = db.Column(db.Float)
    augHighTemp = db.Column(db.Float)
    sepHighTemp = db.Column(db.Float)
    octHighTemp = db.Column(db.Float)
    novHighTemp = db.Column(db.Float)
    decHighTemp = db.Column(db.Float)


class wa(db.Model):
    __bind_key__ = "db"
    year = db.Column('year', db.Integer, primary_key = True)
    minRainfall = db.Column(db.Float)
    maxRainfall = db.Column(db.Float)
    minSunshine = db.Column(db.Float)
    maxSunshine = db.Column(db.Float)
    minLowTemp = db.Column(db.Float)
    maxLowTemp = db.Column(db.Float)
    minHighTemp = db.Column(db.Float)
    maxHighTemp = db.Column(db.Float)
    avgRainfall = db.Column(db.Float)
    avgSunshine = db.Column(db.Float)
    avgLowTemp = db.Column(db.Float)
    avgHighTemp = db.Column(db.Float)

    janRainfall = db.Column(db.Float)
    febRainfall = db.Column(db.Float)
    marRainfall = db.Column(db.Float)
    aprRainfall = db.Column(db.Float)
    mayRainfall = db.Column(db.Float)
    junRainfall = db.Column(db.Float)
    julRainfall = db.Column(db.Float)
    augRainfall = db.Column(db.Float)
    sepRainfall = db.Column(db.Float)
    octRainfall = db.Column(db.Float)
    novRainfall = db.Column(db.Float)
    decRainfall = db.Column(db.Float)

    janSunshine = db.Column(db.Float)
    febSunshine = db.Column(db.Float)
    marSunshine = db.Column(db.Float)
    aprSunshine = db.Column(db.Float)
    maySunshine = db.Column(db.Float)
    junSunshine = db.Column(db.Float)
    julSunshine = db.Column(db.Float)
    augSunshine = db.Column(db.Float)
    sepSunshine = db.Column(db.Float)
    octSunshine = db.Column(db.Float)
    novSunshine = db.Column(db.Float)
    decSunshine = db.Column(db.Float)

    janLowTemp = db.Column(db.Float)
    febLowTemp = db.Column(db.Float)
    marLowTemp = db.Column(db.Float)
    aprLowTemp = db.Column(db.Float)
    mayLowTemp = db.Column(db.Float)
    junLowTemp = db.Column(db.Float)
    julLowTemp = db.Column(db.Float)
    augLowTemp = db.Column(db.Float)
    sepLowTemp = db.Column(db.Float)
    octLowTemp = db.Column(db.Float)
    novLowTemp = db.Column(db.Float)
    decLowTemp = db.Column(db.Float)

    janHighTemp = db.Column(db.Float)
    febHighTemp = db.Column(db.Float)
    marHighTemp = db.Column(db.Float)
    aprHighTemp = db.Column(db.Float)
    mayHighTemp = db.Column(db.Float)
    junHighTemp = db.Column(db.Float)
    julHighTemp = db.Column(db.Float)
    augHighTemp = db.Column(db.Float)
    sepHighTemp = db.Column(db.Float)
    octHighTemp = db.Column(db.Float)
    novHighTemp = db.Column(db.Float)
    decHighTemp = db.Column(db.Float)


class ni(db.Model):
    __bind_key__ = "db"
    year = db.Column('year', db.Integer, primary_key = True)
    minRainfall = db.Column(db.Float)
    maxRainfall = db.Column(db.Float)
    minSunshine = db.Column(db.Float)
    maxSunshine = db.Column(db.Float)
    minLowTemp = db.Column(db.Float)
    maxLowTemp = db.Column(db.Float)
    minHighTemp = db.Column(db.Float)
    maxHighTemp = db.Column(db.Float)
    avgRainfall = db.Column(db.Float)
    avgSunshine = db.Column(db.Float)
    avgLowTemp = db.Column(db.Float)
    avgHighTemp = db.Column(db.Float)

    janRainfall = db.Column(db.Float)
    febRainfall = db.Column(db.Float)
    marRainfall = db.Column(db.Float)
    aprRainfall = db.Column(db.Float)
    mayRainfall = db.Column(db.Float)
    junRainfall = db.Column(db.Float)
    julRainfall = db.Column(db.Float)
    augRainfall = db.Column(db.Float)
    sepRainfall = db.Column(db.Float)
    octRainfall = db.Column(db.Float)
    novRainfall = db.Column(db.Float)
    decRainfall = db.Column(db.Float)

    janSunshine = db.Column(db.Float)
    febSunshine = db.Column(db.Float)
    marSunshine = db.Column(db.Float)
    aprSunshine = db.Column(db.Float)
    maySunshine = db.Column(db.Float)
    junSunshine = db.Column(db.Float)
    julSunshine = db.Column(db.Float)
    augSunshine = db.Column(db.Float)
    sepSunshine = db.Column(db.Float)
    octSunshine = db.Column(db.Float)
    novSunshine = db.Column(db.Float)
    decSunshine = db.Column(db.Float)

    janLowTemp = db.Column(db.Float)
    febLowTemp = db.Column(db.Float)
    marLowTemp = db.Column(db.Float)
    aprLowTemp = db.Column(db.Float)
    mayLowTemp = db.Column(db.Float)
    junLowTemp = db.Column(db.Float)
    julLowTemp = db.Column(db.Float)
    augLowTemp = db.Column(db.Float)
    sepLowTemp = db.Column(db.Float)
    octLowTemp = db.Column(db.Float)
    novLowTemp = db.Column(db.Float)
    decLowTemp = db.Column(db.Float)

    janHighTemp = db.Column(db.Float)
    febHighTemp = db.Column(db.Float)
    marHighTemp = db.Column(db.Float)
    aprHighTemp = db.Column(db.Float)
    mayHighTemp = db.Column(db.Float)
    junHighTemp = db.Column(db.Float)
    julHighTemp = db.Column(db.Float)
    augHighTemp = db.Column(db.Float)
    sepHighTemp = db.Column(db.Float)
    octHighTemp = db.Column(db.Float)
    novHighTemp = db.Column(db.Float)
    decHighTemp = db.Column(db.Float)


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(20))
    ext = db.Column(db.String(20))
    created = db.Column(db.String(68))


def random_name():
    return "".join(random.choices(string.ascii_lowercase, k=5))


def filename():
    random = random_name()
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    for file in files:
        while random == file:
            random = random_name()
        continue
    return random


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    resp = requests.get(
        "https://raw.githubusercontent.com/hazzakak/harrsmith.dev/master/projects.json")
    data = json.loads(resp.text)

    return render_template('index.html', projects=data)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, n):
        yield l[i::n]


@app.route('/images/<page>', methods=['GET'])
def view_images(page: int):
    if request.args.get("pswdpin") != os.getenv("password_hs"):
        return redirect(url_for("index"))

    images = Images.query.order_by(Images.created.desc()).paginate(
        page=int(page), per_page=21
    )

    files_list = []
    list_meta = list(chunks(images.items, 3))
    for file in images.items:
        filename, ext = file.filename.rsplit(".", 1)
        files_list.append([file, ext])

    return render_template(
        "images.html",
        file_amount=images.total,
        files_list=files_list,
        paginator=images,
        images=images.items,
        pswd=os.getenv("password_hs")
    )


@app.route('/i/<fn>')
def view_image(fn):
    #try:
    filename2 = "images/" + fn
    return send_file(filename2)
    #except:
    #    return redirect(url_for("index"))


@app.route("/api/v1.0/images/upload", methods=["POST"])
def api_image_upload():
    print(os.getenv("api_key_hs"))
    if request.method == "POST":
        image = request.files["api_image"]
        key = request.form.get("api_key")
        if key == os.getenv("api_key_hs"):
            ext = image.filename.rsplit(".", 1)[1].lower()
            if ext not in [
                "png",
                "jpg",
                "jpeg",
                "gif",
                "txt",
                "py",
                "json",
                "mp4",
                "pdf",
            ]:
                return Response(
                    response=json.dumps({"error code": "20"}),
                    status=404,
                    mimetype="application/json",
                )
            file = filename() + "." + ext
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], file))
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            img = Images(
                filename=file,
                ext=ext,
                created=now
            )
            db.session.add(img)
            db.session.commit()

            response = {
                "message": "image received",
                "url": f"https://harrysmith.dev/i/{file}",
            }

            return Response(
                response=json.dumps(response), status=200, mimetype="application/json"
            )
        else:
            response = {
                "message": "INCORRECT API KEY"
            }
            return Response(
                response=json.dumps(response), status=401, mimetype="application/json"
            )

###################################
###   STARTING ASSIGNMENT TEST  ###
###################################

@app.route('/api/data_max_values')
def api_data_max_values():
    en_response = en.query.filter_by(year=2022).first()
    sc_response = sc.query.filter_by(year=2022).first()
    wa_response = wa.query.filter_by(year=2022).first()
    ni_response = ni.query.filter_by(year=2022).first()

    
    rtn_json = {
        "en": {
            "min_rainfall": en_response.minRainfall,
            "max_rainfall": en_response.maxRainfall,
            "min_sunshine": en_response.minSunshine,
            "max_sunshine": en_response.maxSunshine,
            "min_lowTemp": en_response.minLowTemp,
            "max_lowTemp": en_response.maxLowTemp,
            "min_highTemp": en_response.minHighTemp,
            "max_highTemp": en_response.maxHighTemp
        },
        "sc": {
            "min_rainfall": sc_response.minRainfall,
            "max_rainfall": sc_response.maxRainfall,
            "min_sunshine": sc_response.minSunshine,
            "max_sunshine": sc_response.maxSunshine,
            "min_lowTemp": sc_response.minLowTemp,
            "max_lowTemp": sc_response.maxLowTemp,
            "min_highTemp": sc_response.minHighTemp,
            "max_highTemp": sc_response.maxHighTemp
        },
        "wa": {
            "min_rainfall": wa_response.minRainfall,
            "max_rainfall": wa_response.maxRainfall,
            "min_sunshine": wa_response.minSunshine,
            "max_sunshine": wa_response.maxSunshine,
            "min_lowTemp": wa_response.minLowTemp,
            "max_lowTemp": wa_response.maxLowTemp,
            "min_highTemp": wa_response.minHighTemp,
            "max_highTemp": wa_response.maxHighTemp
        },
        "ni": {
            "min_rainfall": ni_response.minRainfall,
            "max_rainfall": ni_response.maxRainfall,
            "min_sunshine": ni_response.minSunshine,
            "max_sunshine": ni_response.maxSunshine,
            "min_lowTemp": ni_response.minLowTemp,
            "max_lowTemp": ni_response.maxLowTemp,
            "min_highTemp": ni_response.minHighTemp,
            "max_highTemp": ni_response.maxHighTemp
        }
    }
    resp = flask.jsonify(rtn_json)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/api/data_year_averages')
def api_data_year_averages():
    year = int(request.args.get('year'))

    if year < 1910 or year > 2022:
        response = app.response_class(
        response="Year must be between 1910 and 2022",
        status=400,
        mimetype='application/json')
        return response
    
    en_response = en.query.filter_by(year=year).first()
    sc_response = sc.query.filter_by(year=year).first()
    wa_response = wa.query.filter_by(year=year).first()
    ni_response = ni.query.filter_by(year=year).first()

    rtn_json = {
        "year": year,
        "en": {
            "rainfall": en_response.avgRainfall,
            "sunshine": en_response.avgSunshine,
            "lowTemp": en_response.avgLowTemp,
            "highTemp": en_response.avgHighTemp
        },
        "sc": {
            "rainfall": sc_response.avgRainfall,
            "sunshine": sc_response.avgSunshine,
            "lowTemp": sc_response.avgLowTemp,
            "highTemp": sc_response.avgHighTemp
        },
        "wa": {
            "rainfall": wa_response.avgRainfall,
            "sunshine": wa_response.avgSunshine,
            "lowTemp": wa_response.avgLowTemp,
            "highTemp": wa_response.avgHighTemp
        },
        "ni": {
            "rainfall": ni_response.avgRainfall,
            "sunshine": ni_response.avgSunshine,
            "lowTemp": ni_response.avgLowTemp,
            "highTemp": ni_response.avgHighTemp
        }
    }
    resp = flask.jsonify(rtn_json)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/api/data_full_year_values')
def api_data_full_year_averages():
    year = int(request.args.get('year'))
    country = str(request.args.get('country'))

    if year < 1910 or year > 2022:
        response = app.response_class(
        response="Year must be between 1910 and 2022",
        status=400,
        mimetype='application/json')
        return response
    
    if country not in ['en', 'wa', 'ni', 'sc']:
        response = app.response_class(
        response="Country must be en, wa, ni or sc",
        status=400,
        mimetype='application/json')
        return response
    
    db_obj = None
    
    if country == "en":
        db_obj = en.query.filter_by(year=year).first()
    elif country == "sc":
        db_obj = sc.query.filter_by(year=year).first()
    elif country == "wa":
        db_obj = wa.query.filter_by(year=year).first()
    elif country == "ni":
        db_obj = ni.query.filter_by(year=year).first()

    rtn_json = {
        "year": year,
        "country": country,
        "rainfall": {
            "jan": db_obj.janRainfall,
            "feb": db_obj.febRainfall,
            "mar": db_obj.marRainfall,
            "apr": db_obj.aprRainfall,
            "may": db_obj.mayRainfall,
            "jun": db_obj.junRainfall,
            "jul": db_obj.julRainfall,
            "aug": db_obj.augRainfall,
            "sep": db_obj.sepRainfall,
            "oct": db_obj.octRainfall,
            "nov": db_obj.novRainfall,
            "dec": db_obj.decRainfall
        },

        "sunshine": {
            "jan": db_obj.janSunshine,
            "feb": db_obj.febSunshine,
            "mar": db_obj.marSunshine,
            "apr": db_obj.aprSunshine,
            "may": db_obj.maySunshine,
            "jun": db_obj.junSunshine,
            "jul": db_obj.julSunshine,
            "aug": db_obj.augSunshine,
            "sep": db_obj.sepSunshine,
            "oct": db_obj.octSunshine,
            "nov": db_obj.novSunshine,
            "dec": db_obj.decSunshine
        },

        "highTemp": {
            "jan": db_obj.janHighTemp,
            "feb": db_obj.febHighTemp,
            "mar": db_obj.marHighTemp,
            "apr": db_obj.aprHighTemp,
            "may": db_obj.mayHighTemp,
            "jun": db_obj.junHighTemp,
            "jul": db_obj.julHighTemp,
            "aug": db_obj.augHighTemp,
            "sep": db_obj.sepHighTemp,
            "oct": db_obj.octHighTemp,
            "nov": db_obj.novHighTemp,
            "dec": db_obj.decHighTemp
        },

        "lowTemp": {
            "jan": db_obj.janLowTemp,
            "feb": db_obj.febLowTemp,
            "mar": db_obj.marLowTemp,
            "apr": db_obj.aprLowTemp,
            "may": db_obj.mayLowTemp,
            "jun": db_obj.junLowTemp,
            "jul": db_obj.julLowTemp,
            "aug": db_obj.augLowTemp,
            "sep": db_obj.sepLowTemp,
            "oct": db_obj.octLowTemp,
            "nov": db_obj.novLowTemp,
            "dec": db_obj.decLowTemp
        }

        
    }
    resp = flask.jsonify(rtn_json)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
