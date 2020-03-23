from django.db import models


class Games1(models.Model):
    name = models.CharField(max_length=255, default='adventure games')
    rate = models.FloatField(default=4)
    review = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=2083, default='https://www.google.co.in/imghp?hl=en')
    download_url = models.CharField(max_length=2083, default='https://play.google.com/store?utm_source=apac_Med'
                                                             '&utm_medium=hasem&utm_content=Jan0220&utm_campaign'
                                                             '=Evergreen&pcampaignid=MKT-DR-apac-in-1003227-Med-hasem'
                                                             '-py-Evergreen-Jan0220-Text_Search_BKWS-BKWS'
                                                             '%7cONSEM_kwid_43700012164778770_creativeid_113397194705_'
                                                             'device_c_kwd_kwd-41905086_geoid_9061998_network_g&gclid'
                                                             '=Cj0KCQiA-bjyBRCcARIsAFboWg1PUNWG7Ag2lqbOAMNLdf- '
                                                             '_-8G-gBIpwsWChOTKUSnPylgf691vwP4aAkhgEALw_wcB&gclsrc=aw'
                                                             '.ds')


class Games2(models.Model):
    name = models.CharField(max_length=255, default='action games')
    rate = models.FloatField(default=4)
    review = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=2083, default='https://www.google.co.in/imghp?hl=en')
    download_url = models.CharField(max_length=2083, default='https://play.google.com/store?utm_source=apac_Med'
                                                             '&utm_medium=hasem&utm_content=Jan0220&utm_campaign'
                                                             '=Evergreen&pcampaignid=MKT-DR-apac-in-1003227-Med-hasem'
                                                             '-py-Evergreen-Jan0220-Text_Search_BKWS-BKWS'
                                                             '%7cONSEM_kwid_43700012164778770_creativeid_113397194705_'
                                                             'device_c_kwd_kwd-41905086_geoid_9061998_network_g&gclid'
                                                             '=Cj0KCQiA-bjyBRCcARIsAFboWg1PUNWG7Ag2lqbOAMNLdf- '
                                                             '_-8G-gBIpwsWChOTKUSnPylgf691vwP4aAkhgEALw_wcB&gclsrc=aw'
                                                             '.ds')


class Games3(models.Model):
    name = models.CharField(max_length=255, default='strategy games')
    rate = models.FloatField(default=4)
    review = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=2083, default='https://www.google.co.in/imghp?hl=en')
    download_url = models.CharField(max_length=2083, default='https://play.google.com/store?utm_source=apac_Med'
                                                             '&utm_medium=hasem&utm_content=Jan0220&utm_campaign'
                                                             '=Evergreen&pcampaignid=MKT-DR-apac-in-1003227-Med-hasem'
                                                             '-py-Evergreen-Jan0220-Text_Search_BKWS-BKWS'
                                                             '%7cONSEM_kwid_43700012164778770_creativeid_113397194705_'
                                                             'device_c_kwd_kwd-41905086_geoid_9061998_network_g&gclid'
                                                             '=Cj0KCQiA-bjyBRCcARIsAFboWg1PUNWG7Ag2lqbOAMNLdf- '
                                                             '_-8G-gBIpwsWChOTKUSnPylgf691vwP4aAkhgEALw_wcB&gclsrc=aw'
                                                             '.ds')
