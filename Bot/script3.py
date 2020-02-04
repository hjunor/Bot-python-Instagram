"""Curtir fotos por localização"""
from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='up4.0' , password='3n5df3k9')

with  smart_run(session):
    session.set_do_follow(enabled=True, percentage=100) 
    session.set_do_like(enabled=True, percentage=100)
    
    session.like_by_locations(['247232162/porteirinha-minas-gerais-brazil/'], amount=60)

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comentarios,media='Photo')
    session.join_pods()