from extensions import db

# Define the HomeFooter model
class HomeFooter(db.Model):
    __tablename__ = 'home_footer'
    key = db.Column(db.String, primary_key=True)
    label = db.Column(db.String)
    children = db.relationship('HomeFooterChild', backref='home_footer', lazy=True)

# Define the HomeFooterChild model
class HomeFooterChild(db.Model):
    __tablename__ = 'home_footer_child'
    childid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String)
    title = db.Column(db.String)
    text = db.Column(db.String)
    parent_key = db.Column(db.String, db.ForeignKey('home_footer.key'), nullable=False)