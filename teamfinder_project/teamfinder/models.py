from django.db import models

class Member(models.Model):
    user_num = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user_num = models.ForeignKey(Member, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    class_tag = models.PositiveIntegerField()
    mbti = models.CharField(max_length=4)
    interest = models.CharField(max_length=100)

class TechTag(models.Model):
    tech_tag_id = models.AutoField(primary_key=True)
    tech_tag_name = models.CharField(max_length=50, unique=True)

class ProfileTechTags(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tech_tag = models.ForeignKey(TechTag, on_delete=models.CASCADE)

class Authentication(models.Model):
    user_num = models.OneToOneField(Member, primary_key=True, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)

class Block(models.Model):
    block_num = models.AutoField(primary_key=True)
    from_member = models.ForeignKey(Member, related_name='blocks_sent', on_delete=models.CASCADE)
    blocked_member = models.ForeignKey(Member, related_name='blocks_received', on_delete=models.CASCADE)

class Like(models.Model):
    like_num = models.AutoField(primary_key=True)
    from_member = models.ForeignKey(Member, related_name='likes_sent', on_delete=models.CASCADE)
    liked_member = models.ForeignKey(Member, related_name='likes_received', on_delete=models.CASCADE)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_num = models.ForeignKey(Member, on_delete=models.CASCADE)
    post_tag = models.PositiveIntegerField()
    post_title = models.CharField(max_length=70)
    content = models.CharField(max_length=200)

class PostTechTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tech_tag = models.ForeignKey(TechTag, on_delete=models.CASCADE)
    post_date = models.DateField()
    now_recruit = models.BooleanField()

class Scrap(models.Model):
    scrap_num = models.AutoField(primary_key=True)
    user_num = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)