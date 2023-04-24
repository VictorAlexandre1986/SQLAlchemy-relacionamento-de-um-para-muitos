from main import Post,User,session

user_to_delete = session.query(User).filter_by(id=1).one_or_none()

posts = session.query(Post).all()

all_posts = session.query(Post).all()

all_users = session.query(User).all()

session.delete(user_to_delete)
session.commit()

print(all_posts)
print(all_users)