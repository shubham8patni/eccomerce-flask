from flask import Blueprint, render_template, request, session, redirect, url_for, flash, session, jsonify
import json
import requests
from connection import conn
import boto3


mycursor = conn.cursor()

s3_client = boto3.client('s3')
BUCKET = "flaskecommerce"

cat = Blueprint('cat', __name__) # not necessary to name variable same as file name and not necessay to name


@cat.route('/cat/create/', methods = ["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template('add_new_category.html')
    # record = json.loads(request.data)
    # seller_id = reqest.form["seller_id", int]
    elif request.method == 'POST':
        category = request.form["cat_name"]
        
        sql =  f"INSERT INTO `categories` (`category_name`) VALUES ('{category}')"
        mycursor.execute(sql)
        conn.commit()
        # result = mycursor.fetchall()
        # print(result)

        flash("New Category Successfully Added!", category='success')
        return render_template('add_new_category.html')
       


@cat.route('/cat/fetch/', methods = ["GET"])
def fetch():
    if request.method == 'GET':
        
        sql =  f"SELECT * FROM `categories`;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

        return jsonify(result)



