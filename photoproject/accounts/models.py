from django.db import models

# Create your models here.
#AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    User モデルを継承したカスタムユーザーモデル
    '''

    pass