#parar de seguir seguidores ...
from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='up4.0' , password='3n5df3k9')

with  smart_run(session):
    session.set_do_follow(enabled=True, percentage=100) 
    session.set_do_like(enabled=True, percentage=100)

    session.unfollow_users(amount=100, allFollowing=True, style="RANDOM", unfollow_after=3*60*60*60, sleep_delay=450)
    # 'allfollowing =true' para de seguir qualquer um.

    session.unfollow_users(amount=100, nonFollowers= True, style="RANDOM", unfollow_after=3*60*60*60, sleep_delay=450)
    # 'nonfollowers =true' para de seguir quem não te segue.

    comentarios = ['Very good', 'Nice short','Gostei do seu post', ':)', ':D', 'Parabens', 'Perfect :)','Muito bom', 'Very nice'] 
    """Comentarios pré definidos """

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comentarios,media='Photo')
    session.join_pods()

    