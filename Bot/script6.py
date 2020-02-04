from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='up4.0' , password='3n5df3k9')

with  smart_run(session):
    session.set_do_follow(enabled=True, percentage=100) 
    session.set_do_like(enabled=True, percentage=100)

    session.follow_commenters(['jhonattan_anttunes'], amount = 2, daysold = 100, max_pic = 100, sleep_delay=600, interact=True) 
    """ Seguir pessoas que curtiram perfil """

    comentarios = ['Very good', 'Nice short','Gostei do seu post', ':)', ':D', 'Parabens', 'Perfect :)','Muito bom', 'Very nice'] 
    """Comentarios pré definidos """

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comentarios,media='Photo')
    session.join_pods()

    