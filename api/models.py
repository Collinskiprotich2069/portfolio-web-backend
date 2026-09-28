from django.db import models
    
class Skills(models.Model):
    image  = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=70)
    
    def __str__(self):
        return f'{self.name}'  
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        
class Projects(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='project image',upload_to='images/project_images')
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        
    def __str__(self):
        return self.name
    
class ProfileImages(models.Model):
    first = models.ImageField(upload_to='profilepic')
    second = models.ImageField(upload_to='profilepic')
    third = models.ImageField(upload_to='profilepic')
    
    class Meta:
        verbose_name = 'Profile Image'
        verbose_name_plural = 'Profile Images '
        
    def __str__(self):
        return 'Profile Images'