class Redflag:
    def __init__(self):
        self.all_redflags = [{
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

    def add_redflag(self, createdOn, createdBy, redflag_type, email, location, status, images, videos, comment):
        #Add redflag issue
        redflag = dict(
                id = len(self.all_redflags) + 1,
                createdOn = createdOn,
                createdBy = createdBy,
                type = redflag_type,
                email = email,
                location = location,
                status = status,
                images = images,
                videos = videos,
                comment = comment
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