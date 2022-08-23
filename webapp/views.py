
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import json
import requests
from connection import conn


mycursor = conn.cursor()

# sql =  f"show tables;"
# mycursor.execute(sql)
# result = mycursor.fetchall()

views = Blueprint('views', __name__) # not necessary to name variable same as file name and not necessay to name




@views.context_processor
def inject_user():
    return dict(session_context=session)


@views.route('/')
def index():
    # if not session.get("email"):
    #     return redirect(url_for('auth.login'))
    # else:
    #     return render_template("index.html")
    return redirect(url_for('views.product_list'))



@views.route('/product_list', methods = ['GET'])
def product_list():
    # # return redirect(url_for('success',email = user))
    # if not session.get("email") or session.get('user_level') != 1:       
    #     return redirect(url_for('auth.logout', status = 'error'))

    sql =  f"SELECT * FROM `products`;"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    fin_result = []
    for i in result:
        temp = {
            "id" : i[0],
            "category_id" : i[1],
            "product_name" : i[2],
            "description" : i[3],
            "amount" : i[4],
            "image_url" : i[5],
            "status" : i[6]
        }
        fin_result.append(temp)
    return render_template("product_list.html", list = fin_result)

@views.route('/product_description', methods = ['POST'])
def product_description():
    # # return redirect(url_for('success',email = user))
    # if not session.get("email") or session.get('user_level') != 1:       
    #     return redirect(url_for('auth.logout', status = 'error'))
    product_id = request.form['product_id']
    sql =  f"SELECT * FROM `products` where id =  {product_id};"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    # fin_result = []
    for i in result:
        temp = {
            "id" : i[0],
            "category_id" : i[1],
            "product_name" : i[2],
            "description" : i[3],
            "amount" : i[4],
            "image_url" : i[5],
            "status" : i[6]
        }
        # fin_result.append(temp)
    return render_template("product_description.html", data = temp)


