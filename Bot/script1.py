from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='up4.0' , password='3n5df3k9')

with  smart_run(session):
    session.set_do_follow(enabled=True, percentage=100) 
    session.set_do_like(enabled=True, percentage=100)

    session.like_by_tags(['tech','javascript']) 
    """ Tags para o bot seguir """

    comentarios = ['Very good', 'Nice short'] 
    """Comentarios pré definidos """

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comentarios,media='Photo')
    session.join_pods()