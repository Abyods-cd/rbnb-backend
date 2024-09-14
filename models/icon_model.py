from extensions import db

class Icon(db.Model):
    __tablename__ = 'icons'
    item_id = db.Column(db.Integer, primary_key=True)
    icons = db.Column(db.Boolean)
    title = db.Column(db.String)
    other_info = db.Column(db.String)
    detail_html = db.Column(db.Text)
    host_name = db.Column(db.String)
    host_img_url = db.Column(db.String)
    host_profession = db.Column(db.String)
    host_description = db.Column(db.String)  # 新增字段
    img_url = db.Column(db.Text)
    start_host_year = db.Column(db.String)
    icon_svg = db.Column(db.Text)  # 存储为 JSON 字符串
    host_desc = db.Column(db.Text)  # 存储为 JSON 字符串

