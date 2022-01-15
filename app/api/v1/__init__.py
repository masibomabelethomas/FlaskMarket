from flask import Blueprint

app_v1 = Blueprint("app_v1", __name__, template_folder="../../../templates", static_folder="../../../static")

from app.api.v1.views import market  # noqa

