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
        
    def loop_through(self , redflag_id):
        returned_redflag = [redflag for redflag in self.all_redflags if redflag["id"] == int(redflag_id)]
        return  returned_redflag

    def delete_redflag(self, redflag_id):
        # fetch a single redflag
        if len(self.all_redflags) > 0:
            try:
                returned_redflag = self.loop_through(redflag_id)
                self.all_redflags.remove(returned_redflag[0])
                return self.all_redflags
            except Exception as error:
                return error   
        return False

    def update_comment(self, redflag_id,data):
        returned_redflag = self.loop_through(redflag_id)
        returned_redflag[0]['comment'] = data
        return True
    
    def update_location(self, redflag_id, data):
        returned_redflag = self.loop_through(redflag_id)
        returned_redflag[0]['location'] = data
        return True


