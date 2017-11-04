import factory
from factory.django import DjangoModelFactory as Factory
from django.contrib.auth.models import User
from django.utils.text import slugify

from marketplace import models


class UserFactory(Factory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')

    last_name = factory.Faker('last_name')

    email = factory.LazyAttribute(
        lambda a: f"{a.first_name.lower()}.{a.last_name.lower()}@gsa.gov"
    )

    username = factory.LazyAttribute(
        lambda a: a.email
    )

    is_active = True


job = factory.Faker('job')


def simple_job():
    j = job.generate({})
    # Some jobs are like "Nurse, adult"; we don't want the part
    # after the comma.
    return j.split(',')[0]


class TeamFactory(Factory):
    class Meta:
        model = models.Team

    name = factory.LazyAttribute(
        lambda a: f"GSA {simple_job()}s"
    )


class BaseProductFactory(Factory):
    class Meta:
        model = models.Product
        abstract = True


class FavroFactory(BaseProductFactory):
    slug = 'favro'

    name = 'Favro'

    category = "Project management"

    description = """
        Favro is a planning and collaboration app which enables
        developers, designers, and clients to all stay on the same
        page and track progress.
    """


class MuralFactory(BaseProductFactory):
    slug = 'mural'

    name = 'Mural'

    category = "Live collaboration"

    description = """
        A web-based solution for small teams that need a virtual
        workspace in which they can brainstorm, plan and collaborate.
    """


class TrelloFactory(BaseProductFactory):
    slug = 'trello'

    name = 'Trello'

    category = "Project management"

    description = """
        This is a card-based tool for managing projects and tasks.
        It uses customizable Kanban-style boards, and offers
        "power ups" such as GitHub integration.
    """


class ZoomFactory(BaseProductFactory):
    slug = 'zoom'

    name = 'Zoom'

    category = "Video conferencing"

    description = """
        This is a video conferencing tool with features such as chat,
        screen sharing, and session recording. No account is required
        to participate in conferences.
    """


class ProductFactory(BaseProductFactory):
    name = factory.Faker('company')

    slug = factory.LazyAttribute(
        lambda a: slugify(a.name)
    )

    category = factory.Faker('catch_phrase')

    description = factory.Faker('paragraph')

    @factory.post_generation
    def licenses(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for license in extracted:
                self.license_types.add(license)


class LicenseTypeFactory(Factory):
    class Meta:
        model = models.LicenseType

    name = factory.Faker('catch_phrase')

    product = factory.SubFactory(ProductFactory)