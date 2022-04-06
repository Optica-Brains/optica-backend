from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager , PermissionsMixin
)

class UserManager(BaseUserManager):
    """
    Maintaiining query sets that can be run
    """

    def create_user(self,email, password=None):
        """
        Creating normal user
        """

        if email is None:
            raise TypeError('Users should have email')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email , password=None):
        """
        Creating super user
        """
        if password is None:
            raise TypeError('Password should not be none')


        user = self.create_user(email,password)
        user.is_superuser =True
        user.is_staff =True
        user.save()
        return user

class Branch(models.Model):
    branch_name = models.CharField(max_length= 200)
    branch_location = models.CharField(max_length=200)

    def __str__(self):
        return self.branch_name



class User(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length= 225, unique=True,db_index=True)
    password = models.CharField(max_length=500)
    is_verified = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add =True) 
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE , null = True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[
        'password'
    ]
    objects = UserManager()

    def __str__(self):
        return self.email

    def is_in_group(self,id):
        return self.groups.filter(id__in=[id]).exists()

    def tokens(self):
        
        """
        returns user tokens -add later
        """
        pass         
             


STATUS_CHOICES=(
    ('dispatched','DISPATCHED'),
    ('progress','PROGRESS'),
    ('delivered','DELIVERED')

)

class Order(models.Model):
    order_number = models.CharField(max_length=250,null= False)
    departure_time = models.DateTimeField(null = True)
    delivery_time= models.DateTimeField(null = True)
    status = models.CharField(max_length = 30,choices=STATUS_CHOICES,default='dispatched')
    branch = models.ForeignKey(Branch,related_name='order_branch',on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.order_number



