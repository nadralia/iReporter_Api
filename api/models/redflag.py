from datetime import datetime
class Redflag:
    def __init__(self):
        self.all_redflags = [{
           "id" : 1,
           "createdOn" : "Sat, 22 Dec 2018 11:42:19 GMT",
           "createdBy" : "Adralia Nelson",
           "type" : "red-flag",
           "email" : "nadralia@gmail.com",
           "location" : "Kasanga",
           "status" : "draft",
           "images" : "police.jpg",
           "videos" : "police.mp4",
           "comment": "Police extortion at check point"
        }]

    def add_redflag(self, data):
        #Add redflag issue
        date_added = datetime.now()
        redflag = dict(
                id = len(self.all_redflags) + 1,
                createdOn = date_added,
                createdBy = data['createdBy'] ,
                type = data['type'],
                email = data['email'],
                location = data['location'],
                status = data['status'],
                images = data['images'],
                videos = data['videos'],
                comment = data['comment']
            )
        self.all_redflags.append(redflag)
        return self.all_redflags

    def fetch_all_redflags(self):
        # fetch all available redflags
        if len(self.all_redflags) > 0:
            return self.all_redflags
        return False

    def fetch_single_redflag(self, id):
        # fetch a single redflag
        if len(self.all_redflags) > 0:
            try:
                redflag = next(item for item in self.all_redflags if item["id"] == int(id))
                return redflag 
            except Exception as error:
                return error   
        return False
    
    def update_comment(self):
        pass