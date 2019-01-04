from flask import Blueprint, jsonify, request
from datetime import datetime
from api.models.redflag import Redflag
from api.validations import Validation

redflag = Blueprint('redflag', __name__)

redflag_obj = Redflag()
validation_obj = Validation()



"""Redflag Views/Routes"""
@redflag.route("/api/v1/red-flags",methods=["POST"])
#adding redflag
def add_redflag():
    data = request.get_json()
    date_added = datetime.now()
    search_keys = ("createdBy", "type", "email", "location", "status", "images", "videos","comment")
    if all(key in data.keys() for key in search_keys):
        createdOn = date_added
        createdBy = data.get("createdBy")
        redflag_type = data.get("type")
        email = data.get("email")
        location = data.get("location")
        status = data.get("status")
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")

        invalid = validation_obj.redflag_validation(createdOn, createdBy, redflag_type, email, location, comment)

        if invalid:
            return jsonify({"message":invalid}), 400
        for redflag in range(len(redflag_obj.all_redflags)):
            if redflag_obj.all_redflags[redflag]["comment"] == comment:

                return jsonify({"message":"redflag already exists","redflags":redflag_obj.all_redflags}), 200
        if (redflag_obj.add_redflag(createdOn, createdBy, redflag_type,email,location,status,images,videos,comment)):
            return jsonify({"message":"redflag successfully added", "redflags":redflag_obj.all_redflags}), 201
    return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400 

@redflag.route("/api/v1/red-flags", methods=["GET"])
# fetching all redflags
def fetch_all_redflags():
    all_redflags = redflag_obj.fetch_all_redflags()
    if all_redflags:
        return jsonify({"Status":200, "All Redflags":all_redflags}), 200
    return jsonify({"message":"no redflags added yet"}), 404 

@redflag.route("/api/v1/red-flags/<redflag_id>", methods=["GET"])
# fetching a single redflag
def fetch_single_redflag(redflag_id):
    invalid = validation_obj.validate_input_type(redflag_id)
    if invalid:
        return jsonify({"message":invalid}), 400
    single_redflag = redflag_obj.fetch_single_redflag(redflag_id)
    if single_redflag:
        return jsonify({"redflag details": single_redflag}), 200
    return jsonify({"message":"redflag not added yet"}), 404

@redflag.route("/api/v1/red-flags/<redflag_id>/location", methods=["PATCH"])
# Edit the location of a specific red-flag record
def edit_location_of_a_specific_redflag_record(redflag_id, location):
    if redflag_id == 0 or redflag_id > len(redflag_obj.all_redflags):
        return jsonify({"message": "Index out of range"}), 400


@redflag.route("/api/v1/red-flags/<redflag_id>/comment", methods=["PATCH"])
# Edit the comment of a specific red-flag record
def edit_comment_of_a_specific_redflag_record(redflag_id, comment):
    if redflag_id == 0 or redflag_id > len(redflag_obj.all_redflags):
        return jsonify({"message": "Index out of range"}), 400

@redflag.route("/api/v1/red-flags/<redflag_id>", methods=["DELETE"])
# Delete a specific red flag record
def delete_a_specific_redflag_record(redflag_id):
    if redflag_id == 0 or redflag_id > len(redflag_obj.all_redflags):
        return jsonify({"message": "Index out of range"}), 400
