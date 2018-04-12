from django.db import models

# Create A Blog models
class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title # django admin에서의 각 object display방식을 title로 나타내게 설정하기!

	def summary(self):
		return self.body[:100] 

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y') # customizing the date details	


# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the Admin