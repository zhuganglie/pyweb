from fasthtml.common import *
from models import *

app, rt = fast_app()

@rt('/')
def index():
    return Titled("Blog", Div(*[Div(A(post.title, href=f'/post/{post.id}')) for post in posts()]))

@rt('/post/{id}')
def post(id:int):
    post = posts[id]
    return Titled(post.title, Div(post.content))

@rt('/post/new')
def new_post():
    return Titled("New Post", Form(Input(id="title", name="title", placeholder="Title"), Textarea(id="content", name="content", placeholder="Content"), Button("Save"), action="/post/new", method="post"))

@rt('/post/new')
def create_post(post:Post):
    post = posts.insert(post)
    return RedirectResponse(f'/post/{post.id}')

@rt('/post/{id}/edit')
def edit_post(id:int):
    post = posts[id]
    return Titled("Edit Post", Form(Input(id="title", name="title", placeholder="Title", value=post.title), Textarea(id="content", name="content", placeholder="Content", value=post.content), Button("Save"), action=f"/post/{post.id}/edit", method="post"))

@rt('/post/{id}/edit')
def update_post(id:int, post:Post):
    post.id = id
    posts.update(post)
    return RedirectResponse(f'/post/{post.id}')

@rt('/post/{id}/delete')
def delete_post(id:int):
    posts.delete(id)
    return RedirectResponse('/')

@rt('/tag/new')
def new_tag():
    return Titled("New Tag", Form(Input(id="name", name="name", placeholder="Name"), Button("Save"), action="/tag/new", method="post"))

@rt('/tag/new')
def create_tag(tag:Tag):
    tag = tags.insert(tag)
    return RedirectResponse(f'/tag/{tag.id}')

@rt('/tag/{id}')
def tag(id:int):
    tag = tags[id]
    return Titled(tag.name, Div(*[Div(A(post.title, href=f'/post/{post.id}')) for post in posts() if tag.id in [post_tag.tag_id for post_tag in post_tags(post_id=post.id)]]))

@rt('/post/{id}/tag')
def tag_post(id:int):
    post = posts[id]
    return Titled("Tag Post", Form(*[CheckboxX(id=f'tag-{tag.id}', name=f'tag-{tag.id}', label=tag.name, value=tag.id, checked=tag.id in [post_tag.tag_id for post_tag in post_tags(post_id=post.id)]) for tag in tags()], Button("Save"), action=f"/post/{post.id}/tag", method="post"))

@rt('/post/{id}/tag')
def update_post_tags(id:int):
    post = posts[id]
    for tag in tags():
        if request.form.get(f'tag-{tag.id}'):
            post_tags.insert(PostTag(post_id=post.id, tag_id=tag.id))
        else:
            post_tags.delete(post_id=post.id, tag_id=tag.id)
    return RedirectResponse(f'/post/{post.id}')
