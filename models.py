from fasthtml.common import *

db = database('data/blog.db')

posts = db.t.posts
tags = db.t.tags
post_tags = db.t.post_tags

if posts not in db.t:
    posts.create(id=int, title=str, content=str, pk='id')
if tags not in db.t:
    tags.create(id=int, name=str, pk='id')
if post_tags not in db.t:
    post_tags.create(post_id=int, tag_id=int, pk=('post_id', 'tag_id'))

Post = posts.dataclass()
Tag = tags.dataclass()
PostTag = post_tags.dataclass()
