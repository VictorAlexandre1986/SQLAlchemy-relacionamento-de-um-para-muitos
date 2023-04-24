from config_db import Post,User,session

class Crud():

    @staticmethod
    def cadastrar_user():
        new_user=User(
            username="testuser",
            email="testuser@gmail.com"
        )

        session.add(new_user)
        session.commit()


    @staticmethod
    def cadastrar_post():
    
        posts = [
      {
        "title":"Learn Django",
        "content":"Lorem ipsum"
      },
      {
        "title":"Learn Flask",
        "content":"Lorem ipsum"
      },
      {
        "title":"Learn Sqlalchemy",
        "content":"Lorem ipsum"
      },
      {
        "title":"Learn Node",
        "content":"Lorem ipsum"
      }
]

        user = session.query(User).filter_by(id=1).one_or_none()

        for post in posts:
            print(post['title'])
            new_post=Post(
                title=post['title'],
                content=post['content'],
                author=user
            )
            session.add(new_post)
            session.commit()

#------------------------------------------------------------
    @staticmethod
    def deletar_post():
        user_to_delete = session.query(User).filter_by(id=1).one_or_none()
        session.delete(user_to_delete)
        session.commit()

# post = session.query(Post).filter_by(id=1).first()
# print(post.author)

