from flask import Blueprint
from app.api import auth

auth_bp = Blueprint("auth", __name__)

# Rute autentikasi
auth_bp.route("/google-login", methods=["POST"])(auth.google_login)
auth_bp.route("/register", methods=["POST"])(auth.register)
auth_bp.route("/login", methods=["POST"])(auth.login)
auth_bp.route("/logout", methods=["POST"])(auth.logout)