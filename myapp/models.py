from django.db import models
from django.core.urlresolvers import reverse


class OrgList(models.Model):
    company_name = models.CharField(max_length=40)
    company_logo = models.FileField(null='True',blank='True')
    company_website = models.CharField(max_length=40)
    company_address = models.TextField()
    #slist=models.ForeignKey(StatesList, on_delete=models.CASCADE ,default=False)
    CSTATE = (('AndhraPradesh','AndhraPradesh'),('Tamilnadu ','Tamilnadu'),('Maharastra','Maharastra'),('Karnataka','Karnataka'),('Telangana','Telangana'))
    company_state=models.CharField(max_length=40,choices=CSTATE,default='AndhraPradesh')



    def __str__(self):
        return self.company_name + ' - ' + self.company_website + ' - ' + self.company_address

    def get_absolute_url(self):
        return reverse('detail',kwargs={"id":self.id})
    def is_upperclass(self):
        return self.company_state

class EmpDetail(models.Model):
    orglist=models.ForeignKey(OrgList, on_delete=models.CASCADE ,default=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    job_role = models.CharField(max_length=40)


    def __str__(self):  # __unicode__ on Python 2
        return self.first_name  + '-' +  self.last_name
    def get_absolute_url(self):
        return reverse('edetail',kwargs={"id":self.id})


class StatesList(models.Model):
    state_name = models.CharField(max_length=40)

    def __str__(self):
        return self.state_name
