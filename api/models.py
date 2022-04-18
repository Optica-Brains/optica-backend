import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager , PermissionsMixin
)
from django.utils import timezone

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
        user.save(using=self._db)
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
    ('delivered','DELIVERED')
)


class Batch(models.Model):
    batch_number = models.CharField(max_length=30)
    departure_time = models.DateTimeField(null = True, default=timezone.now)
    delivery_time= models.DateTimeField(null = True)
    status = models.CharField(max_length = 30,choices=STATUS_CHOICES,default='dispatched')
    branch_from = models.ForeignKey(Branch,related_name='batch_branch_from',on_delete=models.CASCADE, null=True)
    branch_to = models.ForeignKey(Branch,related_name='batch_branch_to',on_delete=models.CASCADE, null=True)
    messenger = models.ForeignKey(User, related_name ='batch_messenger', on_delete=models.CASCADE, null=True)
    branch_staff = models.ForeignKey(User,related_name="accepted_batches", on_delete=models.CASCADE, null=True)
    rider_status = models.CharField(max_length = 30,choices=STATUS_CHOICES,default='dispatched')
    rider_delivery_time = models.DateTimeField(null =True)
    manager_status = models.CharField(max_length = 30,choices=STATUS_CHOICES,default='dispatched')
    manager_delivey_time = models.DateTimeField(null = True)
    created_by = models.ForeignKey(User, related_name ='created_batches', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.batch_number

    class Meta:
        ordering = ['-departure_time']

    # total batches summary
    @classmethod
    def total_deliveries(cls,status):
        return cls.objects.filter(status=status).count()


    @classmethod
    def total_batches(cls):
        return cls.objects.count()

    
    

     


    # @classmethod
    # def total_delivered(cls):
    #     return cls.objects.where()


    def rider_delivery(self):
        self.rider_delivery_time = datetime.datetime.now()
        self.rider_status = 'delivered'
        self.save()


    def manager_delivery(self, user,date=None):
        self.manager_delivey_time = date if date is not None else self.rider_delivery_time
        self.delivery_time = date if date is not None else self.rider_delivery_time
        self.manager_status = 'delivered'
        self.status = 'delivered'
        self.branch_staff_id = user.id

        self.save()
    


class Order(models.Model):
    order_number = models.CharField(max_length=250,null= False)
    batch = models.ForeignKey(Batch, related_name='batch_orders',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.order_number

