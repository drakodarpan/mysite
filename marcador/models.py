#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    # Influye en como se muestra o se comportan los modelos
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']
        
    # Como se mostrara la información al usuario
    def __str__(self):
        return self.name


class PublicBookmarkManager(models.Manager):
    def get_query_set(self):
        qs = super(PublicBookmarkManager, self).get_query_set()
        return qs.filter(is_public=True)


@python_2_unicode_compatible
class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date create')
    date_updated = models.DateTimeField('date update')
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)
    
    objects = models.Manager()
    # Se asigna un atributo publico
    public = PublicBookmarkManager()
    
    # Influye en como se muestra o se comportan los modelos
    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']
    
    # Como se mostrara la información al usuario
    def __str__(self):
        return '%s (%s)' % (self.title, self.url)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)