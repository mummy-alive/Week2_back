from django.contrib import admin
from .models import Member, Profile, TechTag, ProfileTechTags, Authentication, Block, Like, Post, PostTechTags, Scrap

admin.site.register(Member)
admin.site.register(Profile)
admin.site.register(TechTag)
admin.site.register(ProfileTechTags)
admin.site.register(Authentication)
admin.site.register(Block)
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(PostTechTags)
admin.site.register(Scrap)
