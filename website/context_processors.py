"""from datetime import datetime
from django.conf import settings

# this is a good example of extra
# context you might need across templates


def default(request):
    # you can declare any variable that you would like and pass
    # them as a dictionary to be added to each template's context:
    return dict(
        example = "This is an example string.",
        current_date = datetime.now(),
        MEDIA_URL = settings.MEDIA_URL, # just for the sake of example
    )"""

from blog.models import Post
from django.shortcuts import render


def latest_post_footer(request):
    post = Post.objects.filter(status='published').order_by('-published')[0:3]
    return {'posts': post}


def represent_telephone(request):
    return {'telephone': '020 79930069'}

# Renting essential links

def allergy_uk(request):
    return {'allergy_uk': 'https://www.allergyuk.org/information-and-advice/conditions-and-symptoms'}


def beekeepers(request):
    return {'beekeepers': 'https://www.bbka.org.uk/help/find_a_swarm_coordinator.php'}


def civil_legal_advice_url(request):
    return {'civil_legal_advice_url': 'https://www.gov.uk/civil-legal-advice'}


def crisis_url(request):
    return {'crisis_url': 'https://www.crisis.org.uk/ending-homelessness/housing-resource-centre/prs-database/'}


def find_council_url(request):
    return {'find_council_url': 'https://www.gov.uk/find-local-council'}


def gassafe_url(request):
    return {'gassafe_url': 'https://www.staygassafe.co.uk/'}


def hmcts_fees_url(request):
    return {'hmcts_fees_url': 'http://hmctsformfinder.justice.gov.uk/HMCTS/GetLeaflet.do?court_leaflets_id=264'}


def hmcts_form_ex160a_url(request):
    return {'hmcts_form_ex160a_url': 'http://hmctsformfinder.justice.gov.uk/HMCTS/GetLeaflet.do?court_leaflets_id=2833'}


def hmcts_form_n244_url(request):
    return {'hmcts_form_n244_url': 'http://hmctsformfinder.justice.gov.uk/HMCTS/GetForm.do?court_forms_id=484'}


def housing_ombudsman(request):
    return {'housing_ombudsman': 'http://www.housing-ombudsman.org.uk/resolve-a-complaint/getting-help-from-the-housing-ombudsman/#.WgjLBcZl_IV'}


def hse_gas_tenants_url(request):
    return {'hse_gas_tenants_url': 'http://www.hse.gov.uk/gas/domestic/faqtenant.htm'}


def nhs_carbon_monoxide_poisoning_url(request):
    return {'nhs_carbon_monoxide_poisoning_url': 'https://www.nhs.uk/conditions/carbon-monoxide-poisoning/'}


def pest_control_association(request):
    return {'pest_control_association': 'https://bpca.org.uk/About'}


def rentokil_signs_of_rats(request):
    return {'rentokil_signs_of_rats': 'https://www.rentokil.co.uk/rats/signs-of-rats/'}


def rics_url(request):
    return {'rics_url': 'https://www.rics.org/uk/'}


def right_to_rent_gov(request):
    return {'right_to_rent_gov': 'https://www.gov.uk/government/publications/right-to-rent-document-checks-a-user-guide'}


def rspca_fleas(request):
    return {'rspca_fleas': 'https://www.rspca.org.uk/adviceandwelfare/pets/general/fleas'}




















