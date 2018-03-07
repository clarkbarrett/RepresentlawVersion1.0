from blog.models import Post

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


def latest_post_footer(__request__):
    post = Post.objects.filter(status='published').order_by('-published')[0:3]
    return {'posts': post}


def represent_telephone(__request__):
    return {'telephone': '0203 488 3333'}

# Renting essential links


def allergy_uk(__unused__):
    return {'allergy_uk': 'https://www.allergyuk.org/information-and-advice/conditions-and-symptoms'}


def beekeepers(__request__):
    return {'beekeepers': 'https://www.bbka.org.uk/help/find_a_swarm_coordinator.php'}


def civil_legal_advice_url(__request__):
    return {'civil_legal_advice_url': 'https://www.gov.uk/civil-legal-advice'}


def court_fees_url(__request__):
    return {'court_fees_url': 'https://www.gov.uk/court-fees-what-they-are'}


def court_finder_url(__request__):
    return {'court_finder_url': 'https://courttribunalfinder.service.gov.uk/search/'}


def crisis_url(__request__):
    return {'crisis_url': 'https://www.crisis.org.uk/ending-homelessness/housing-resource-centre/prs-database/'}


def find_council_url(__request__):
    return {'find_council_url': 'https://www.gov.uk/find-local-council'}


def gassafe_url(__request__):
    return {'gassafe_url': 'https://www.staygassafe.co.uk/'}


def hmcts_fees_url(__request__):
    return {'hmcts_fees_url': 'http://hmctsformfinder.justice.gov.uk/HMCTS/GetLeaflet.do?court_leaflets_id=264'}


def hmcts_form_ex160a_url(__request__):
    return {'hmcts_form_ex160a_url': 'http://hmctsformfinder.justice.gov.uk/HMCTS/GetLeaflet.do?court_leaflets_id=2833'}


def hmcts_form_n244_url(__request__):
    return {'hmcts_form_n244_url': 'http://hmctsformfinder.justice.gov.uk/HMCTS/GetForm.do?court_forms_id=484'}


def housing_ombudsman(__request__):
    return {'housing_ombudsman': 'http://www.housing-ombudsman.org.uk/resolve-a-complaint/getting-help-from-the-housing-ombudsman/#.WgjLBcZl_IV'}


def hse_gas_tenants_url(__request__):
    return {'hse_gas_tenants_url': 'http://www.hse.gov.uk/gas/domestic/faqtenant.htm'}


def leasehold_service_url(__request__):
    return {'leasehold_service_url': 'https://clients.lease-advice.org/appointments.aspx'}


def nhs_carbon_monoxide_poisoning_url(__request__):
    return {'nhs_carbon_monoxide_poisoning_url': 'https://www.nhs.uk/conditions/carbon-monoxide-poisoning/'}


def nhs_damp_url(__request__):
    return {'nhs_damp_url': 'https://www.nhs.uk/chq/Pages/Can-damp-and-mould-affect-my-health.aspx'}


def N16A_Injunction_Application_url(__unused__):
        return {'N16A_Injunction_Application_url':
                    'http://hmctsformfinder.justice.gov.uk/HMCTS/GetForm.do?court_forms_id=402'}


def pest_control_association(__request__):
    return {'pest_control_association': 'https://bpca.org.uk/About'}


def rentokil_signs_of_rats(__request__):
    return {'rentokil_signs_of_rats': 'https://www.rentokil.co.uk/rats/signs-of-rats/'}


def represent_contact_email(__request__):
    return {'represent_contact_email': 'info@representlaw.com'}


def rics_url(__request__):
    return {'rics_url': 'https://www.rics.org/uk/'}


def right_to_rent_gov(__request__):
    return {'right_to_rent_gov': 'https://www.gov.uk/government/publications/right-to-rent-document-checks-a-user-guide'}


def rspca_fleas(__request__):
    return {'rspca_fleas': 'https://www.rspca.org.uk/adviceandwelfare/pets/general/fleas'}




















