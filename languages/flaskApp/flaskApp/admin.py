from flaskApp import app

from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('adminTemplates/dashboard.html')

@app.route("/admin/profile")
def admin_profile():
    return render_template('adminTemplates/profile.html')