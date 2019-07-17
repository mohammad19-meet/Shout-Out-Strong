from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def auth_user(username, password):
    session = DBSession()
    user = session.query(User).filter_by(username = username, password= password).first()
    print(user)
    return user

def add_user(username,password,role):
    user_object = User(username=username,
    password=password,
    role=role)
    session.add(user_object)
    session.commit()

def add_story(name, title, the_story):
	summary=the_story[0:30]
	story_object= Story(name=name, title=title, the_story=the_story, summary=summary)
	session.add(story_object)
	session.commit()

def story_by_name(name):
	session = DBSession()
	stories= session.query(Story).filter_by(name=name).all()
	return stories

def get_all_stories():
    stories = session.query(Story).all()
    return stories

def get_story_id(id):
    story=session.query(Story).filter_by(id=id).first()
    return story

def add_event(name, time, date, place, info, picture):
    user_event= Event(name=name, time=time, date=date, place=place, info=info, picture=picture)
    session.add(user_event)
    session.commit()

def get_all_events():
    events = session.query(Event).all()
    return events

def get_event_id(id):
    event=session.query(Event).filter_by(id=id).first()
    return event

def get_event_id(id):
    event=session.query(Event).filter_by(id=id).first()
    return event

def get_all_id():
    ids=[]
    s=get_all_stories()
    for i in s:
        ids.append(i.id)
    return ids

def get_all_products():
    products = session.query(Product).all()
    return products

def add_product(name, color, picture, price, info):
    user_product= Product(name=name, color=color, picture=picture, price=price, info=info)
    session.add(user_product)
    session.commit()

def get_product_id(id):
    product=session.query(Product).filter_by(id=id).first()
    return product



#add_user("user", "pass", 0)
#add_user("shelly", 1234,0)
#add_story("hey", "story 1", "so i was going to buy something but then from nowhere somebody")
#add_event("event 1", "4:30", "4.6", "Tel Aviv", "bla bla bla", "sexual.jpg")
#add_product("shirt", "red", "sexual.jpg", 24, "bla bla bla")