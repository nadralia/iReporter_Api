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
        self.assertEqual(reply["message"], "redflag successfully added")
        self.assertEqual(response.status_code, 201)

    def test_adding_redflag_with_missing_key(self):
        response = self.app.post("/api/v1/red-flags",
            content_type='application/json',
            data=json.dumps(dict(type="red-flag", comment="Power outage for 2 over weeks"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "a 'key(s)' is missing in your request body")
        self.assertEqual(response.status_code, 400)   

    def test_fetching_redflags(self):
        response = self.app.post("/api/v1/red-flags",
            content_type='application/json',
            data=json.dumps(dict(createdOn="2018-12-20 10:02:49", createdBy="Adralia Nelson", type="red-flag", email="xsdferty@gmail.com",location="kiwafu-estate",
            status="draft", images="poweroutage.jpg", videos="poweroutage.mp4", comment="Power outage for 2 over weeks"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/red-flags",
        content_type='application/json')
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)     

    def test_fetching_single_redflag(self):
        response = self.app.post("/api/v1/red-flags",
            content_type='application/json',
            data=json.dumps(dict(createdOn="2018-12-20 10:02:49", createdBy="Adralia Nelson", type="red-flag", email="xsdferty@gmail.com",location="kiwafu-estate",
            status="draft", images="poweroutage.jpg", videos="poweroutage.mp4", comment="Power outage for 2 over weeks"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/red-flags/2",
        content_type='application/json')
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)

    def test_fetching_single_redflag_with_impromper_id(self):
        response = self.app.post("/api/v1/red-flags",
            content_type='application/json',
            data=json.dumps(dict(createdOn="2018-12-20 10:02:49", createdBy="Adralia Nelson", type="red-flag", email="xsdferty@gmail.com",location="kiwafu-estate",
            status="draft", images="poweroutage.jpg", videos="poweroutage.mp4", comment="Power outage for 2 over weeks"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/red-flags/r",
        content_type='application/json')
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 400)  