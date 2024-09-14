from extensions import db

# 1. Define the Tab model
class Tab(db.Model):
    __tablename__ = 'tabs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    icon_img_url = db.Column(db.String)



