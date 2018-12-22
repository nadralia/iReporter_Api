class Incident:
    """This class defines the incident sold by the store"""
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.type = kwargs['type']
        self.comment = kwargs['comment']
        self.location = kwargs['location']
        self.status = kwargs['status']
        self.images = kwargs['images']
        self.all_incidents = [{
           "id" : 1,
           "createdOn" : "2018-10-25 15:02:49",
           "createdBy" : "Adralia Nelson",
           "type" : "red-flag",
           "email" : "nadralia@gmail.com",
           "location" : "Kasanga",
           "status" : "draft",
           "images" : "police.jpg",
           "videos" : "police.mp4",
           "comment": "Police extortion at check point"
        }]


    def create_incident(self):
        return {
            "id": self.id,
            "type": self.type,
            "status": self.status,
            "location": self.location,
            "comment": self.comment,
            }

