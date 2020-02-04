from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='' , password='')

with  smart_run(session):
    session.set_do_follow(enabled=True, percentage=100) 
    session.set_do_like(enabled=True, percentage=100)

    session.follow_likers(['jhonattan_anttunes'], photos_grab_amount=1, follow_likers_per_photo=2, randomize=True) 
    """ Seguir pessoas que curtiram perfil """

    comentarios = ['Very good', 'Nice short'] 
    """Comentarios pré definidos """

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comentarios,media='Photo')
    session.join_pods()

    
