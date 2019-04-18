from django.db import models
from django.contrib.postgres.fields import ArrayField

from data.models import Dataset
from alyx.base import BaseModel


class CoordinateSystem(BaseModel):
    name = models.CharField(max_length=200)


class BaseBrainCoordinates(BaseModel):
    """
    Abstract base class for brain coordinates. Never used directly.
    Contains a FK to a coordinate system
    """
    coordinate_system = models.ForeignKey(CoordinateSystem, blank=True, null=True,
                                          on_delete=models.SET_NULL,
                                          help_text='Coordinate system, Atlas and origin')


class ProbeTrajectory(BaseBrainCoordinates):
    """
    Contains info about the geometry and probe model of a single probe insertion.
    """

    entry_point = ArrayField(models.FloatField(), size=3,
                             help_text=('Antero-posterior, Dorso-ventral and Left-right'
                                        'cartesian coordinates of the entry point'))

    tip_point = ArrayField(models.FloatField(), size=3,
                           help_text=('Antero-posterior, Dorso-ventral and Left-right'
                                      'cartesian coordinates of the electrode tip'))

    probe_model = models.ForeignKey('ProbeModel', blank=True, null=True,
                                    on_delete=models.SET_NULL,
                                    help_text="model of probe used")

    axial_angle = models.FloatField(blank=True, null=True,
                                    help_text=('Rotation of the probe around its axis'))

    channel_mapping = models.ForeignKey(
        Dataset, blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='probe_insertion_channel_mapping',
        help_text="numerical array of size nSites x 1 giving the row of the raw data file "
                  "for each contact site. You will have one of these files per probe, "
                  "including if you record multiple probes through the same amplifier. "
                  "Sites that were not recorded should have NaN or -1.")

    @property
    def distance_advanced(self):
        pass


class BrainLocation():
    """Allen CCU"""
    """one label (eventually index)"""
    """NB the strings are hierarchical, we need to keep this feature"""
    pass


class RecordingSite(BaseBrainCoordinates):
    """
    Contains estimated anatomical location of each recording site in each probe insertion.
    This is usually figured out using histology, so should override what you might
    compute from ProbeInsertion. Location a
    """

    probe_insertion = models.ForeignKey(
        ProbeTrajectory, on_delete=models.CASCADE, help_text="id of probe insertion")

    site_no = models.IntegerField(help_text="which site on the probe")
