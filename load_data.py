import json
from idlelib.iomenu import encoding

from app import app, db
from models.tabs_model import Tab
from models.past_experience_model import PastExperience, PastExperienceImage
from models.home_footer_model import HomeFooter, HomeFooterChild
from models.icon_model import Icon
import os

# load tabs data to the database
def load_tabs_data():
    with open('data/tabs.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            tab = Tab(
                id=item['id'],
                name=item['name'],
                icon_img_url=item['iconImgUrl']
            )
            db.session.add(tab)
        db.session.commit()

# load past experiences data to the database
def load_past_experience_data():
    with open('data/past-experience.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            past_experience = PastExperience(
                item_id=item['itemId'],
                icons=item['icons'],
                past=item['past'],
                title=item['title'],
                host=item['host'],
                other_info=item['otherInfo']
            )
            db.session.add(past_experience)

            for img_url in item['imgUrl']:
                past_experience_image = PastExperienceImage(
                    past_experience_id=item['itemId'],
                    img_url=img_url
                )
                db.session.add(past_experience_image)
        db.session.commit()

# load home footer data to the database
def load_home_footer_data():
    with open('data/home-footer.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            home_footer = HomeFooter(
                key=item['key'],
                label=item['label']
            )
            db.session.add(home_footer)
            for child in item['children']:
                home_footer_child = HomeFooterChild(
                    id=child['id'],
                    title=child['title'],
                    text=child['text'],
                    parent_key=home_footer.key
                )
                db.session.add(home_footer_child)
        db.session.commit()

# load icon data to db
def load_icons_data():
    with open('data/icons.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            # handle icons value
            icons_value = item.get('icons', 'false').lower() == 'true'

            # handle host info
            host_field = item.get('host', {})
            if isinstance(host_field, dict):
                # when host is dict type
                host_name = host_field.get('hostName', '')
                host_img_url = host_field.get('hostImgUrl', '')
                host_profession = host_field.get('hostProfession', '')
                host_description = ''
            elif isinstance(host_field, str):
                # when host is string type
                host_name = ''
                host_img_url = ''
                host_profession = ''
                host_description = host_field.strip()
            else:
                # provide default value
                host_name = ''
                host_img_url = ''
                host_profession = ''
                host_description = ''

            img_url_json = json.dumps(item.get('imgUrl', []), ensure_ascii=False)
            meet_info = item.get('meetInfo', {})
            icon_svg_json = json.dumps(meet_info.get('iconSvg', []), ensure_ascii=False)
            host_desc_json = json.dumps(meet_info.get('hostDesc', []), ensure_ascii=False)

            # create icon instance
            icon = Icon(
                item_id=item.get('itemId'),
                icons=icons_value,
                title=item.get('title', ''),
                other_info=item.get('otherInfo', ''),
                detail_html=item.get('detailHTML', ''),
                host_name=host_name,
                host_img_url=host_img_url,
                host_profession=host_profession,
                host_description=host_description,
                img_url=img_url_json,
                start_host_year=meet_info.get('startHostYear', ''),
                icon_svg=icon_svg_json,
                host_desc=host_desc_json
            )
            db.session.add(icon)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # load_tabs_data()
        # load_past_experience_data()
        # load_home_footer_data()
        load_icons_data()
