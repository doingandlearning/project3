from django.db import models

# Create your models here.
class Ticket(models.Model):
    OPEN_STATUS = 1
    RESOLVED_STATUS = 2
    CLOSED_STATUS = 3
    DUPLICATE_STATUS = 4

    STATUS_CHOICES = (
        (1, _('Open')),
        (2, _('Resolved')),
        (3, _('Closed')),
        (4, _('Duplicate')),
    )

    PRIORITY_CHOICES = (
        (1, _('1. Critical')),
        (2, _('2. High')),
        (3, _('3. Normal')),
        (4, _('4. Low')),
        (5, _('5. Very Low')),
    )

    title = models.CharField(_('Title'), max_length=200)
    # queue = models.ForeignKey(Queue, on_delete=models.CASCADE, verbose_name=('Queue'))
    created = models.DateTimeField(('Created'), blank=True, help_text=('Date this ticket was created'))
    modified = models.DateTimeField(('Modified'), blank=True, help_text=('Date this ticket was most recently changed'))
    submitter_email = models.EmailField(('Submitter email'), blank=True, null=True, help_text=('The submitter will receive email for all follow-ups'))
    # assigned_to = models.ForeignKey()
    status = models.IntegerField(('Status'), choices=STATUS_CHOICES, default=OPEN_STATUS)
    on_hold = models.BooleanField(('On hold'), blank=True, default=False, help_text=('Ticket is on hold.'))
    description = models.TextField(('Description'), blank=True, null=True, help_text=('Content of the customers query.'))
    resolution = models.TextField(('Resolution'), blank=True, null=True, help_text=('The resolution provided to the customer'))
    priority = models.IntegerField(('Proirity'), choices=PRIORITY_CHOICES, default=3, blank=3, help_text=('1 = Highest Priority -> 5 = Lowest Priority'))
    due_date = models.DateTimeField(('Due on'), blank=True, null=True,)
    last_escalation = models.DateTimeField(blank=True, null=True, editable=False, help_text=('The date this was last escalated.'))

    class Meta:
        get_latest_by = 'created'
        ordering_by = ('id',)
        verbose_name = ('Ticket')
        verbose_name_plural = ('Tickets')

    def __str__(self):
        return '%s %s' % (self.id, self.title)
        
