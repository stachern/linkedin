from datetime import date, datetime
import re

__author__ = 'Stanislau_Charniakou'


class Share(object):

    def __init__(self, *args, **kwargs):
        self.author_member_id = kwargs['author'].get('id') if kwargs.get('author') else None
        self.share_id = kwargs.get('id')
        self.comment = kwargs.get('comment')
        self.description = kwargs['content'].get('description') if kwargs.get('content') else None
        self.eyebrow_url = kwargs['content'].get('eyebrowUrl') if kwargs.get('content') else None
        self.resolved_url = kwargs['content'].get('resolvedUrl') if kwargs.get('content') else None
        self.shortened_url = kwargs['content'].get('shortenedUrl') if kwargs.get('content') else None
        self.submitted_url = kwargs['content'].get('submittedUrl') if kwargs.get('content') else None
        self.title = kwargs['content'].get('title') if kwargs.get('content') else None
        self.timestamp = datetime.fromtimestamp(kwargs.get('timestamp') / 1e3) if kwargs.get('timestamp') else None
        self.visibility_code = kwargs['visibility'].get('code') if kwargs.get('visibility') else None

class Location(object):

    def __init__(self, *args, **kwargs):
        self.country_code = kwargs['country'].get('code') if kwargs.get('country') else None
        self.name = kwargs.get('name')


class Position(object):

    def __init__(self, *args, **kwargs):
        self.start_date = date(year=kwargs['startDate']['year'], month=kwargs['startDate']['month'], day=1) if kwargs.get('startDate') else None
        self.end_date = date(year=kwargs['endDate']['year'], month=kwargs['endDate']['month'], day=1) if kwargs.get('endDate') else None
        self.position_id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.is_current = kwargs.get('isCurrent')
        self.summary = kwargs.get('summary')
        self.company = Company(**kwargs['company']) if kwargs.get('company') else None

class Company(object):

    def __init__(self, *args, **kwargs):
        self.company_id = kwargs.get('id')
        self.industry = kwargs.get('industry')
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
        self.size = kwargs.get('size')

class Profile(object):

    def __init__(self, *args, **kwargs):
        self.first_name = kwargs.get('firstName')
        self.last_name = kwargs.get('lastName')
        self.email = kwargs.get('emailAddress')
        self.distance = kwargs.get('distance')
        self.formatted_name = kwargs.get('formattedName')
        self.headline = kwargs.get('headline')
        self.member_id = kwargs.get('id')
        self.industry = kwargs.get('industry')
        self.num_connections = kwargs.get('numConnections')
        self.num_connections_capped = kwargs.get('numConnectionsCapped')
        self.picture_url = kwargs.get('pictureUrl')
        self.public_url = kwargs.get('publicProfileUrl')
        self.private_url = kwargs['siteStandardProfileRequest'].get('url') if kwargs.get('siteStandardProfileRequest') else None
        self.internal_id = re.search(r"(?<=key=)\d+" , self.private_url).group() if self.private_url else None
        self.positions = [Position(**pos) for pos in kwargs['positions']['values']] if kwargs.get('positions') and kwargs['positions']['_total'] > 0 else None
        self.location = Location(**kwargs['location']) if kwargs.get('location') else None
        self.specialties = kwargs.get('specialties')
        self.summary = kwargs.get('summary')
        self.current_share = Share(**kwargs['currentShare']) if kwargs.get('currentShare') else None
