from distutils import config
from flask import Blueprint, render_template, request, session, redirect, url_for, flash, session, jsonify
import json
import requests
from connection import conn
import boto3
import os, io
from werkzeug.utils import secure_filename
import uuid

mycursor = conn.cursor()
s3_client = boto3.client('s3')
BUCKET = "flaskecommerce"

product = Blueprint('product', __name__) # not necessary to name variable same as file name and not necessay to name


@product.route('/product/create/', methods = ["GET", "POST"])
def create_prod():
    if request.method == 'GET':
        sql =  f"SELECT * FROM `categories`;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
        
        return render_template('add_new_product.html', cat = result)
    # record = json.loads(request.data)
    # seller_id = reqest.form["seller_id", int]
    elif request.method == 'POST':
        category = request.form["categories"]
        product_name = request.form["product_name"]
        description = request.form["description"]
        amount = request.form["amount"]
        image = request.files['image']
        ext = image.filename.split(".")
        print(ext)
        image.filename = secure_filename(str(uuid.uuid4().hex + "." + ext[1]))

        # response = s3_client.upload_file(image, BUCKET, image.filename)
        try:
            s3_client.upload_fileobj(image, BUCKET, image.filename)
        except Exception as e:
                return (str(e))
        head = s3_client.head_object(Bucket=BUCKET, Key=image.filename)
        success = head['ContentLength']
        # print("11111111222222222", head)
        img_url = "https://flaskecommerce.s3.ap-south-1.amazonaws.com/" + str(image.filename)
        print("1111111",img_url,amount,description,product_name,category)
        sql =  f"INSERT INTO `products` (`category_id`, `product_name`, `description`, `amount`, `image_url`, `status`) VALUES ('{category}', '{product_name}', '{description}', '{amount}', '{img_url}', 'available')"   # status = enum ('available','unavailable','deleted')"
        mycursor.execute(sql)
        conn.commit()


        # if result[''] == :
        #     return {
        #         'status' : 201 ,
        #         'data' : "New Product Created" 
        #     }
        # else:
        #     return {
        #         'status' : 401 ,
        #         'data' : "New Product Created" 
        #     }
        flash("New Product Successfully Added!", category='success')
        return render_template('add_new_product.html')

# @product.route('/product', methods = ["POST"])
# def create():
#     # record = json.loads(request.data)
#     # seller_id = request.form["seller_id", int]
#     category = request.form["category" : int]
#     product_name = request.form["product_name" : str]
#     description = request.form["description" : str]
#     amount = request.form["amount" : int ]
#     image = request.files.get('imagefile', '')
#     print(image)

#     img_res = upload_image()
#     img_url = img_res['id']

#     sql =  f"INSERT INTO `produucts` (`category`, `product_name`, `description`, `amount`, `image`, `status`) VALUES ('{category}', '{product_name}', '{description}', '{amount}', '{img_url}')"   # status = enum ('available','unavailable','deleted')
#     mycursor.execute(sql)
#     result = mycursor.fetchall()
#     print(result)
#     # return {
#     #     'status' : 201 ,
#     #     'data' : "New Product Created" 
#     # }

#     return "haha"





# @product.route('/product/update', methods = ["PUT"])
# def update():
#     # record = json.loads(request.data)
#     # seller_id = request.form["seller_id", int]
#     id = request.form["id" : int]
#     description = request.form["description" : str]
#     amount = request.form["amount" : int ]
#     status = request.form["status" : str ]

#     if len(description) == 0:
#         description = ''
    
#     if len(amount) == 0:
#         amount

#     sql =  f"UPDATE `produucts` SET `amount` = '{amount}', `description` = '{description}' , `status` = '{status}' where id = '{id}'"
#     mycursor.execute(sql)
#     result = mycursor.fetchall()
#     print(result)
#     if result[''] == :
#         return {
#             'status' : 201 ,
#             'data' : "Product Updated" 
#         }
#     else:
#         return {
#             'status' : 401 ,
#             'data' : "Could not update Product" 
#         }


#     return "haha"

# @product.route('/product/delete', methods = ["DELETE"])
# def delete():
#     # record = json.loads(request.data)
#     # seller_id = request.form["seller_id", int]
#     id = request.form["id" : int]
    
#     sql =  f"UPDATE `produucts` SET `status` = 'deleted' where id = '{id}'"
#     mycursor.execute(sql)
#     result = mycursor.fetchall()
#     print(result)
#     if result[''] == :
#         return {
#             'status' : 201 ,
#             'data' : "New Product Created" 
#         }
#     else:
#         return {
#             'status' : 401 ,
#             'data' : "New Product Created" 
#         }

#     return "haha"


