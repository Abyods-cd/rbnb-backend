from crypt import methods

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from flask import jsonify
from extensions import db
from flask_migrate import Migrate
from models.tabs_model import Tab
from models.past_experience_model import PastExperience
from models.home_footer_model import HomeFooter
from models.icon_model import Icon

# load .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# database configuration
DATABASE_URI = os.getenv('DATABASE_URI')
if not DATABASE_URI:
    raise ValueError('DATABASE_URI is not set')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Rbnb APIs'

# send tabs data when the path is /api/tabs
@app.route('/api/tabs', methods=['GET'])
def get_tabs():
    tabs = Tab.query.all()
    data = []
    for tab in tabs:
        data.append({
            'id': tab.id,
            'name': tab.name,
            'iconImgUrl': tab.icon_img_url
        })
    return jsonify(data)

# send past experience data when the path is /api/past-experience
@app.route('/api/past-experience', methods=['GET'])
def get_past_experience():
    past_experiences = PastExperience.query.all()
    data = []
    for past_experience in past_experiences:
        data.append({
            'itemId': past_experience.item_id,
            'icons': past_experience.icons,
            'past': past_experience.past,
            'title': past_experience.title,
            'host': past_experience.host,
            'otherInfo': past_experience.other_info,
            'imgUrl': [img.img_url for img in past_experience.images]
        })
    return jsonify(data)

# send home footer data when the path is /api/home-footer
@app.route('/api/home-footer', methods=['GET'])
def get_home_footer():
    home_footer = HomeFooter.query.all()
    data = []
    for home_footer_item in home_footer:
        children = []
        for child in home_footer_item.children:
            children.append({
                'id': child.id,
                'title': child.title,
                'text': child.text
            })
        data.append({
            'key': home_footer_item.key,
            'label': home_footer_item.label,
            'children': children
        })
    return jsonify(data)

# send home footer data when the path is /api/icons
@app.route('/api/icons', methods=['GET'])
def get_icons():
    icons = Icon.query.all()
    data = []
    for icon in icons:
        if icon.host_name or icon.host_img_url or icon.host_profession:
            # when have host details
            host_info = {
                'hostName': icon.host_name,
                'hostImgUrl': icon.host_img_url,
                'hostProfession': icon.host_profession
            }
        elif icon.host_description:
            # when only have host_description
            host_info = icon.host_description
        else:
            host_info = None

        data.append({
            'itemId': icon.item_id,
            'icons': str(icon.icons).lower(),
            'title': icon.title,
            'otherInfo': icon.other_info,
            'detailHTML': icon.detail_html,
            'host': host_info,
            'imgUrl': json.loads(icon.img_url or '[]'),
            'meetInfo': {
                'startHostYear': icon.start_host_year,
                'iconSvg': json.loads(icon.icon_svg or '[]'),
                'hostDesc': json.loads(icon.host_desc or '[]')
            }
        })
    return jsonify(data)


# Create tables immediately within the app context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)