from api.models.redflag import Redflag
from tests.base_test import BaseTestCase
from flask import json

redflag_obj = Redflag()

class TestRedflags(BaseTestCase):

    def test_data_structure(self):
        self.assertTrue(isinstance(redflag_obj.all_redflags, list))

    def test_add_redflag(self):
        response = self.app.post("/api/v1/red-flags",
            content_type='application/json',
            data=json.dumps(dict(createdOn="2018-12-20 10:02:49", createdBy="Adralia Nelson", type="red-flag", email="xsdferty@gmail.com",location="kiwafu-estate",
            status="draft", images="poweroutage.jpg", videos="poweroutage.mp4", comment="Power outage for 2 over weeks" ),))

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "redflag successfully added")
        self.assertEquals(response.status_code, 201)
        