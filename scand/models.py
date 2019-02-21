import os

from comment.models import Comment
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from taggit.models import TagBase, GenericTaggedItemBase

from scandoc.settings import BASE_DIR
from taggit.managers import TaggableManager


class ImageTagManager(models.Manager):
    def new_tasks(self, status):
        queryset = self.model.objects.filter(status=status, is_reverted=False, is_forwarded=False)
        return queryset

    def reverted_tasks(self, status):
        queryset = self.model.objects.filter(status=status, is_reverted=True, is_forwarded=False)
        return queryset

    def forwarded_tasks(self, status):
        queryset = self.model.objects.filter(status=status, is_reverted=True, is_forwarded=True)
        return queryset

    def ordered_images(self):
        queryset = self.model.objects.order_by('id').all()
        return queryset

    def search(self, query_dict):

        if isinstance(query_dict, list):
            queryset = ImageTag.objects.filter(id__in=query_dict)
            if queryset is not None:
                return queryset
            else:
                return False

        # Initially getting all objects
        queryset_initial = ImageTag.objects.filter(status='03')

        queryset = queryset_initial

        searched_for = {}
        for key in query_dict:
            if query_dict[key] not in (None, ''):
                if not isinstance(query_dict[key], list):  # grabbing dictionary of searched fields
                    searched_for[key] = query_dict[key]
                elif isinstance(query_dict[key], list) and len(query_dict[key]) > 0:  # list based filter
                    queryset = queryset.filter(tags__name__in=query_dict[key]).distinct()

        # filtering based on non list criteria
        queryset = queryset.filter(**searched_for)

        if queryset != queryset_initial:
            return queryset
        else:
            return []


# Forcing Taggit to save lower case tags
#######################################
class LowerCaseTag(TagBase):
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(LowerCaseTag, self).save(*args, **kwargs)


class LowerCaseTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(LowerCaseTag, related_name="tagged_items", on_delete=models.CASCADE)
#######################################


STATUS = (
    (0, 'Initial'),
    (1, 'Created'),
    (2, 'Proofread'),
    (3, 'Active'),
)


class ImageTag(models.Model):
    class Meta:
        permissions = (
            ('can_approve', 'Can Approve'),
        )
    # generating upload path
    def get_upload_path(instance, filename):
        path = os.path.join(BASE_DIR, 'media')
        dir_count = 0
        for dirpath, dirnames, filenames in os.walk(path):
            dir_count += len(dirnames)
        test_path = os.path.join(path, 'arch' + str(dir_count-1))
        if os.path.isdir(test_path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(test_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)

            if total_size >= (5*1024*1024):  # Checking if directory size is over 20MB
                os.mkdir(path + '/arch' + str(dir_count))
                return 'arch' + str(dir_count) + '/' + filename
            else:
                return 'arch' + str(dir_count-1) + '/' + filename
        else:
            os.mkdir(path + '/arch' + str(dir_count))
            return 'arch' + str(dir_count) + '/' + filename

    # Model Fields
    company = models.CharField(max_length=200, verbose_name='Company \u274B', help_text='required field')
    accoff = models.CharField(max_length=200, verbose_name='Office / Deptt: \u274B', help_text='required field')
    section = models.CharField(max_length=200, verbose_name='Section \u274B', help_text='required field')
    docref = models.CharField(max_length=10, verbose_name='Document Ref. \u274B', help_text='required field')  # Register Number
    start_date = models.DateField(verbose_name='From Date', blank=True, null=True)
    end_date = models.DateField(verbose_name='Till Date', blank=True, null=True)
    pagenum = models.CharField(max_length=5, blank=True, null=True, verbose_name='Page Number')
    refnum = models.CharField(max_length=15, blank=True, null=True, verbose_name='Reference Number')
    pernum = models.CharField(max_length=8, blank=True, null=True, verbose_name='Personnel Id No.')  # Personnel Number
    attr1 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Extra Attribute')
    attr2 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Extra Attribute')
    attr3 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Extra Attribute')
    attr4 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Extra Attribute')
    attr5 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Extra Attribute')
    tags = TaggableManager(through=LowerCaseTaggedItem, verbose_name='Tags', blank=True)
    image = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True, choices=STATUS)
    is_reverted = models.BooleanField(default=False)
    is_forwarded = models.BooleanField(default=False)
    comments = GenericRelation(Comment)

    objects = ImageTagManager()

    def get_absolute_url(self):
        return reverse('scand:image-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.docref + ' ' + self.company + ' ' + str(self.image)

