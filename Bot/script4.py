"""seguir pessoas de um certo perfil"""

from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='' , password='')

with  smart_run(session):
    session.follow_user_followers(['jhonattan_anttunes'], amount=3, randomize=False)
    """Seguir seguidores do perfill"""

    session.follow_user_following(['jhonattan_anttunes'], amount=3,randomize=False)
    """Seguir pessoas seguidas do perfil"""

    
