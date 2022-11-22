from models import User, Post, Tag, PostTag, db
from app import app


db.drop_all()
db.create_all()

u1 = User(first_name="Chris",last_name="Richter",img_url="https://scontent-iad3-1.xx.fbcdn.net/v/t39.30808-6/288319172_10101442272268649_3951561415509359858_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=x3G3JDIdz_MAX8jHtUp&_nc_ht=scontent-iad3-1.xx&oh=00_AfCYbY_bf-s_wfyW8HgZsFptCyZRd8xSAHV_sqFBBs_ISA&oe=63768031")
u2 = User(first_name="Katie",last_name="Richter",img_url="https://scontent-iad3-1.xx.fbcdn.net/v/t39.30808-6/309546671_4434895350385_4946490284071586233_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=RMxzigr8lK0AX8dBswR&tn=DtOdEUKjGIl3ut5_&_nc_ht=scontent-iad3-1.xx&oh=00_AfDBch_WYTvsUuTGkIrSwR0j6uvnIe9LT0bNaNmdBitYmw&oe=6375466E")
u3 = User(first_name="Ryan",last_name="Gosling")
u4 = User(first_name="Mary",last_name="Lewis",img_url="https://images.pexels.com/photos/733872/pexels-photo-733872.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
u5 = User(first_name="Stephen",last_name="Grape",img_url="https://www.cdc.gov/cancer/prostate/images/man-750.jpg?_=76964")

p1 = Post(title="Lets Get Posting",content="First post here on Blogly",user_id=5)
p2 = Post(title="Actually Im Out",content="Not as versatile as i thought",user_id=5)
p3 = Post(title="I Love My Husband", content="He is the greaatest thing to happen",user_id=2)
p4 = Post(title="Christmas Season Starts Nov 1st",content="Many have issues with me decorating so early but it allows us to look at the decorations for an extra 20+ days",user_id=2)
p5 = Post(title="Guten Morgen!",user_id=4,content="In der Hoffnung, dass heute der beste Tag für Sie ist und Sie alle Ihre Ziele erreichen")
p6 = Post(title="Kurt Cobain",content="Is the best Artist in American History, wonderful compositions",user_id=3)
p7 = Post(title="Welcome To My App, Blogly!",content="I am happy to introduce this great app for bloging all your thoughts for others to read!",user_id=1)

t1 = Tag(name="Informational")
t2 = Tag(name="Arts")
t3 = Tag(name="Hobbies")
t4 = Tag(name="Sports")
t5 = Tag(name="Music")
t6 = Tag(name="Life")
t7 = Tag(name="Pin")

pt1 = PostTag(post_id=3,tag_id=6)
pt2 = PostTag(post_id=4, tag_id=6)
pt3 = PostTag(post_id=6, tag_id=5)
pt4 = PostTag(post_id=7, tag_id=1)
pt5 = PostTag(post_id=7, tag_id=7)

db.session.add_all([u1,u2,u3,u4,u5])
db.session.add_all([t1,t2,t3,t4,t5,t6,t7])

db.session.commit()

db.session.add_all([p1,p2,p3,p4,p5,p6,p7])

db.session.commit()

db.session.add_all([pt1,pt2,pt3,pt4,pt5])
db.session.commit()