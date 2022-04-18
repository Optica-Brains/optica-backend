from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Branch, Batch , User , Order

class Branchtest(TestCase):

    def setUp(self):
         self.JunctionMall = Branch(branch_name="JunctionMall",branch_location="Ngong Road")

    def test_instance(self):
        self.assertTrue(isinstance(self.JunctionMall, Branch))

class UserTest(TestCase):
    def setUp(self):
        self.JunctionMall = Branch(branch_name="JunctionMall",branch_location="Ngong Road")
        self.JunctionMall.save()

        self.Nobella = User (full_name = "Nobella Ejiofor", email="nobellanyarari@gmail.com", password="######", is_verified="False",is_active="True", is_staff = "False",created_at="", branch= self.JunctionMall)
        self.Nobella.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.Nobella, User))


class BatchTest(TestCase):
 

    def setUp(self):
        self.JunctionMall = Branch(branch_name="JunctionMall",branch_location="Ngong Road")
        self.JunctionMall.save()

        self.Nobella = User (full_name = "Nobella Ejiofor", email="nobellanyarari@gmail.com", password="######", is_verified="False",is_active="True", is_staff = "False",created_at="", branch= self.JunctionMall)
        self.Nobella.save()

        self.B89R890 = Batch(batch_number="B89R890",departure_time="2022-01-01 13:22",delivery_time="2022-01-01 13:22",status="delivered", messenger=self.Nobella, branch_staff=self.Nobella, rider_status="dispatched", manager_status="dispatched",manager_delivey_time = "2022-01-01 13:22",created_by=self.Nobella, branch_to = self.JunctionMall, branch_from=self.JunctionMall)
        

    def test_instance(self):
        self.assertTrue(isinstance(self.B89R890, Batch))


class OrderTest(TestCase):
    def setUp(self):

        self.JunctionMall = Branch(branch_name="JunctionMall",branch_location="Ngong Road")
        self.JunctionMall.save()

        self.Nobella = User (full_name = "Nobella Ejiofor", email="nobellanyarari@gmail.com", password="######", is_verified="False",is_active="True", is_staff = "False",created_at="", branch= self.JunctionMall)
        self.Nobella.save()

        self.B89R890 = Batch(batch_number="B89R890",departure_time="2022-01-01 13:22",delivery_time="2022-01-01 13:22",status="2022-01-01 13:22", messenger=self.Nobella, branch_staff=self.Nobella, rider_status="dispatched", manager_status="dispatched",manager_delivey_time = "2022-01-01 13:22",created_by=self.Nobella, branch_to = self.JunctionMall, branch_from=self.JunctionMall)
        self.B89R890.save()


        self.order = Order(order_number = "22w123" , batch = self.B89R890)

    def test_instance(self):
        self.assertTrue(isinstance(self.order , Order))

