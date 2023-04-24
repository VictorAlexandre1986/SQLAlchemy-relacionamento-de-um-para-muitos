from main import Post,User,session

# #------------------Rode esse comando primeiro------------------------
# new_user=User(
#     username="testuser",
#     email="testuser@gmail.com"
# )

# session.add(new_user)
# session.commit()

#----------------------Rode esse comando segundo-----------------------
# posts = [
#     {
#         "title":"Learn Django",
#         "content":"Lorem ipsum"
#     },
#     {
#         "title":"Learn Flask",
#         "content":"Lorem ipsum"
#     },
#     {
#         "title":"Learn Sqlalchemy",
#         "content":"Lorem ipsum"
#     },
#     {
#         "title":"Learn Node",
#         "content":"Lorem ipsum"
#     }
# ]

# user = session.query(User).filter_by(id=1).one_or_none()

# for post in posts:
#     print(post['title'])
#     new_post=Post(
#         title=post['title'],
#         content=post['content'],
#         author=user
#         )
#     session.add(new_post)
#     session.commit()

#------------------------------------------------------------

post = session.query(Post).filter_by(id=1).first()
print(post.author)

