import pytest
from pydat.api import create_app
from pydat.core.plugins import PluginBase, register
from flask import Blueprint


@pytest.fixture
def config_app():
    app = create_app(
        {
            "TESTING": True,
            "SEARCH_KEYS": [
                "domainName",
                "registrant_name",
                "contactEmail",
                "registrant_telephone",
            ],
            "SORT_KEYS": [
                "domainName",
                "details.registrant_name",
                "details.contactEmail",
                "details.standardRegCreatedDate",
                "details.registrant_telephone",
                "dataVersion",
                "_score",
            ],
            "LIMIT": 100,
        }
    )
    return app


@pytest.fixture
def client():
    app = create_app({"TESTING": True, })
    return app.test_client()


# simple test plugin, returns created valid plugin
@pytest.fixture
def create_plugin():
    def _create_plugin(user_pref=None, name="hello", jsfiles=[]):
        bp = Blueprint(name, __name__)

        @bp.route("/hello")
        def hello():
            return "Success!"

        class TestPlugin(PluginBase):
            @property
            def blueprint(self):
                return bp

            @property
            def user_pref(self):
                return user_pref

            @property
            def name(self):
                return name

            @property
            def jsfiles(self):
                return jsfiles

        @register
        def start_plugin():
            test = TestPlugin()
            return test

        test_plugin = start_plugin()
        return test_plugin

    return _create_plugin
