from extensions import db

# Define the PastExperience model
class PastExperience(db.Model):
    __tablename__ = 'past_experience'
    item_id = db.Column(db.Integer, primary_key=True)
    icons = db.Column(db.String)
    past = db.Column(db.String)
    title = db.Column(db.String)
    host = db.Column(db.String)
    other_info = db.Column(db.String)
    images = db.relationship('PastExperienceImage', backref='past_experience', lazy=True)

# Define the PastExperienceImage model
class PastExperienceImage(db.Model):
    __tablename__ = 'past_experience_images'
    image_id = db.Column(db.Integer, primary_key=True)
    past_experience_id = db.Column(db.Integer, db.ForeignKey('past_experience.item_id'), nullable=False)
    img_url = db.Column(db.String)