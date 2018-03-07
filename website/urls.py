from django.conf.urls import url, include
from website.views import HomeView
from django.views.generic import TemplateView

app_name = "website"

urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', TemplateView.as_view(template_name='website/home_temp.html'), name='home_temp'),
    url(r'^about/$', TemplateView.as_view(template_name='website/about.html'), name='about'),
    url(r'^terms-and-conditions/$', TemplateView.as_view(template_name='website/terms-and-conditions.html'),
        name='terms_and_conditions'),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy-policy.html'), name='privacy-policy'),

    # url(r'^contact/$', TemplateView.as_view(template_name='website/contact.html'), name='contact'),

    # url(r'^contact/', include('contact_form.urls'), name='contact_form'),
    # url(r'^contact/',    include('envelope.urls'), name='contact_form'),

    url(r'^cookie-policy/$', TemplateView.as_view(template_name='website/cookie-policy.html'),
        name='cookie-policy'),

    # Conveyancing Commercial
    url(r'^conveyancing-commercial/$',
        TemplateView.as_view(template_name='website/conveyancing-commercial/conveyancing-commercial-home.html'),
        name='conveyancing-commercial-home'),

    # Conveyancing Residential
    url(r'^conveyancing-residential/$',
        TemplateView.as_view(template_name='website/conveyancing-residential/conveyancing-residential-home.html'),
        name='conveyancing-residential-home'),

    # Elderly Client
    url(r'^elderly-client-services/$',
        TemplateView.as_view(template_name='website/elderly-client/elderly-client-home.html'),
        name='elderly-client-home'),

    # Employment
    url(r'^employment-and-tribunals/$',
        TemplateView.as_view(template_name='website/employment/employment-home.html'),
        name='employment-home'),

    # Family
    url(r'^family-and-children/$',
        TemplateView.as_view(template_name='website/family-and-children/family-home.html'),
        name='family-home'),


    # Leasehold
    url(r'^leasehold/$', TemplateView.as_view(template_name='website/leasehold/testing.html'), name='leasehold-home'),

    url(r'^leasehold/what_is_leasehold$',
        TemplateView.as_view(template_name='website/leasehold/what_is_leasehold.html'),
        name='leasehold-what_is_leasehold'),

    # Litigation
    url(r'^litigation-and-disputes/$',
        TemplateView.as_view(template_name='website/litigation-and-disputes/litigation-home.html'),
        name='litigation-home'),

    # Power Attorney
    url(r'^power-attorney-court-protection/$',
        TemplateView.as_view(template_name='website/power-attorney-court-protection/power-attorney-court-protection.html'),
        name='power-attorney-home'),

    # Probate and Estate services
    url(r'^probate-and-estates/$', TemplateView.as_view(template_name='website/probate-and-estates/probate-home.html'),
        name='probate-home'),


    # Renters
    url(r'^renting/$', TemplateView.as_view(template_name='website/renters/renters-home.html'), name='renting-home'),
    url(r'^renting/faqs$', TemplateView.as_view(template_name='website/renters/renters-faqs.html'),
        name='renting-faqs-english'),

    # Will writing services
    url(r'^wills/$', TemplateView.as_view(template_name='website/wills/will-writing.html'), name='wills'),
    url(r'^wills-trusts/$', TemplateView.as_view(template_name='website/wills/wills-trusts.html'), name='wills-trusts'),
    url(r'^wills/make-my-will$', TemplateView.as_view(template_name='website/wills/make-my-will.html'),
        name='make-my-will'),


    # Renting
    url(r'^renters/$', TemplateView.as_view(template_name='website/renters/renters-home.html'), name='renters-home'),
    url(r'^renters/renting-faqs/$', TemplateView.as_view(template_name='website/renters/renters-faqs.html'), name='renters-faqs'),


    # Renting/deposits

    url(r'^renters/assured-shorthold-tenancies$',
        TemplateView.as_view(template_name='website/renters/assured-shorthold-tenancies.html'),
        name='renters-assured-shorthold-tenancies'),

    url(r'^renters/assured_tenancies$',
        TemplateView.as_view(template_name='website/renters/assured_tenancies.html'),
        name='renters-assured_tenancies'),

    url(r'^renters/can_council_tenants_stop_the_bailiffs$',
        TemplateView.as_view(template_name='website/renters/can_council_tenants_stop_the_bailiffs.html'),
        name='renters-can_council_tenants_stop_the_bailiffs'),

    url(r'^renters/can_housing_association_tenants_stop_the_bailiffs$',
        TemplateView.as_view(template_name='website/renters/can_housing_association_tenants_stop_the_bailiffs.html'),
        name='renters-can_housing_association_tenants_stop_the_bailiffs'),

    url(r'^renters/can_private_tenants_stop_the_bailiffs$',
        TemplateView.as_view(template_name='website/renters/can_private_tenants_stop_the_bailiffs.html'),
        name='renters-can_private_tenants_stop_the_bailiffs'),

    url(r'^renters/complain_to_environmental_health_about_rented_housing$',
        TemplateView.as_view(template_name='website/renters/complain_to_environmental_health_about_rented_housing.html'),
        name='renters-complain_to_environmental_health_about_rented_housing'),

    url(r'^renters/complain_about_council_or_housing_association_repairs$',
        TemplateView.as_view(
            template_name='website/renters/complain_about_council_or_housing_association_repairs.html'),
        name='renters-complain_about_council_or_housing_association_repairs'),

    url(r'^renters/complain_to_the_ombudsman_about_repairs_in_social_housing$',
        TemplateView.as_view(
            template_name='website/renters/complain_to_the_ombudsman_about_repairs_in_social_housing.html'),
        name='renters-complain_to_the_ombudsman_about_repairs_in_social_housing'),

    url(r'^renters/damage_or_wear_and_tear$',
        TemplateView.as_view(
            template_name='website/renters/damage_or_wear_and_tear.html'),
        name='renters-damage_or_wear_and_tear'),

    url(r'^renters/damp_and_mould_in_rented_homes$',
        TemplateView.as_view(
            template_name='website/renters/damp_and_mould_in_rented_homes.html'),
        name='renters-damp_and_mould_in_rented_homes'),

    url(r'^renters/deposit-check$', TemplateView.as_view(template_name='website/renters/deposit-check.html'),
        name='renters-deposit-check'),

    url(r'^renters/deposit-check-lookup$',
        TemplateView.as_view(
            template_name='website/renters/deposit-check-lookup.html'),
        name='renters-deposit-check-lookup'),

    url(r'^renters/disrepair-advice$',
        TemplateView.as_view(template_name='website/renters/disrepair-advice.html'),
        name='renters-disrepair-advice'),

    url(r'^renters/doing_the_repairs_if_your_landlord_wont$',
        TemplateView.as_view(
            template_name='website/renters/doing_the_repairs_if_your_landlord_wont.html'),
        name='renters-doing_the_repairs_if_your_landlord_wont'),

    url(r'^renters/deposit-protection-claims$',
        TemplateView.as_view(template_name='website/renters/deposit-protection-claims.html'),
        name='deposit-protection-claims'),

    url(r'^renters/electrical_safety_in_rented_homes$',
        TemplateView.as_view(template_name='website/renters/electrical_safety_in_rented_homes.html'),
        name='renters-electrical_safety_in_rented_homes'),

    url(r'^renters/ending_a_periodic_tenancy$',
        TemplateView.as_view(template_name='website/renters/ending_a_periodic_tenancy.html'),
        name='renters-ending_a_periodic_tenancy'),

    url(r'^renters/energy_costs_in_shared_accommodation$',
        TemplateView.as_view(template_name='website/renters/energy_costs_in_shared_accommodation.html'),
        name='renters-energy_costs_in_shared_accommodation'),

    url(r'^renters/eviction$',
        TemplateView.as_view(template_name='website/renters/eviction.html'),
        name='renters-eviction'),

    url(r'^renters/eviction_documents_the_court_sends_you$',
        TemplateView.as_view(template_name='website/renters/eviction_documents_the_court_sends_you.html'),
        name='renters-eviction_documents_the_court_sends_you'),

    url(r'^renters/eviction_for_rent_arrears$',
        TemplateView.as_view(template_name='website/renters/eviction_for_rent_arrears.html'),
        name='renters-eviction_for_rent_arrears'),

    url(r'^renters/eviction-of-assured-shorthold-tenants$',
        TemplateView.as_view(template_name='website/renters/eviction-of-assured-shorthold-tenants.html'),
        name='renters-eviction-of-assured-shorthold-tenants'),

    url(r'^renters/eviction_of_assured_tenants$',
        TemplateView.as_view(template_name='website/renters/eviction_of_assured_tenants.html'),
        name='renters-eviction_of_assured_tenants'),

    url(r'^renters/eviction_of_lodgers_and_other_excluded_occupiers$',
        TemplateView.as_view(template_name='website/renters/eviction_of_lodgers_and_other_excluded_occupiers.html'),
        name='renters-eviction_of_lodgers_and_other_excluded_occupiers'),

    url(r'^renters/eviction_of_regulated_tenants$',
        TemplateView.as_view(template_name='website/renters/eviction_of_regulated_tenants.html'),
        name='renters-eviction_of_regulated_tenants'),

    url(r'^renters/eviction_of_students_in_halls_and_other_occupiers_with_basic_protection$',
        TemplateView.as_view(template_name='website/renters/eviction_of_students_in_halls_and_other_occupiers_with_basic_protection.html'),
        name='renters-eviction_of_students_in_halls_and_other_occupiers_with_basic_protection'),

    url(r'^renters/eviction_notices_from_private_landlords',
        TemplateView.as_view(template_name='website/renters/eviction_notices_from_private_landlords.html'),
        name='renters-eviction_notices_from_private_landlords'),

    url(r'^renters/eviction_using_the_accelerated_possession_procedure$',
        TemplateView.as_view(template_name='website/renters/eviction_using_the_accelerated_possession_procedure.html'),
        name='renters-eviction_using_the_accelerated_possession_procedure'),

    url(r'^renters/eviction_with_a_section_8_notice$',
        TemplateView.as_view(template_name='website/renters/eviction_with_a_section_8_notice.html'),
        name='renters-eviction_with_a_section_8_notice'),

    url(r'^renters/excluded_occupiers$',
        TemplateView.as_view(template_name='website/renters/excluded_occupiers.html'),
        name='renters-excluded_occupiers'),

    url(r'^renters/fire_safety_advice_for_tenants$',
        TemplateView.as_view(template_name='website/renters/fire_safety_advice_for_tenants.html'),
        name='renters-fire_safety_advice_for_tenants'),

    url(r'^renters/renters-faqs$',
        TemplateView.as_view(template_name='website/renters/renters-faqs.html'),
        name='renters-renters-faqs'),

    url(r'^renters/gas_safety_in_rented_homes$',
        TemplateView.as_view(template_name='website/renters/gas_safety_in_rented_homes.html'),
        name='renters-gas_safety_in_rented_homes'),

    url(r'^renters/get-deposit-protected$',
        TemplateView.as_view(template_name='website/renters/get-deposit-protected.html'),
        name='renters-get-deposit-protected'),

    url(r'^renters/get_help_from_your_council_when_homeless_who_qualifies$',
        TemplateView.as_view(template_name='website/renters/get_help_from_your_council_when_homeless_who_qualifies.html'),
        name='renters-get_help_from_your_council_when_homeless_who_qualifies'),

    url(r'^renters/harassment_by_a_private_landlord$',
        TemplateView.as_view(template_name='website/renters/harassment_by_a_private_landlord.html'),
        name='renters-harassment_by_a_private_landlord'),

    url(r'^renters/health_and_safety_standards_for_rented_homes_hhsrs$',
        TemplateView.as_view(template_name='website/renters/health_and_safety_standards_for_rented_homes_hhsrs.html'),
        name='renters-health_and_safety_standards_for_rented_homes_hhsrs'),

    url(r'^renters/help_from_the_council_after_illegal_eviction$',
        TemplateView.as_view(template_name='website/renters/help_from_the_council_after_illegal_eviction.html'),
        name='renters-help_from_the_council_after_illegal_eviction'),

    url(r'^renters/hmo-claims$',
        TemplateView.as_view(template_name='website/renters/hmo-claims.html'),
        name='renters-hmo-claims'),

    url(r'^renters/houses_in_multiple_occupation_hmo$',
        TemplateView.as_view(template_name='website/renters/houses_in_multiple_occupation_hmo.html'),
        name='renters-houses_in_multiple_occupation_hmo'),

    url(r'^renters/housing_advice$',
        TemplateView.as_view(template_name='website/renters/housing_advice.html'),
        name='renters-housing_advice'),

    url(r'^renters/housing_disrepair_check_if_you_can_claim_compensation$',
        TemplateView.as_view(template_name='website/renters/housing_disrepair_check_if_you_can_claim_compensation.html'),
        name='renters-housing_disrepair_check_if_you_can_claim_compensation'),

    url(r'^renters/housing_help_if_your_home_is_flooded$',
        TemplateView.as_view(
            template_name='website/renters/housing_help_if_your_home_is_flooded.html'),
        name='renters-housing_help_if_your_home_is_flooded'),

    url(r'^renters/housing_standards_in_private_rented_homes$',
        TemplateView.as_view(template_name='website/renters/housing_standards_in_private_rented_homes.html'),
        name='renters-housing_standards_in_private_rented_homes'),

    url(r'^renters/how_long_a_section_21_eviction_takes$',
        TemplateView.as_view(template_name='website/renters/how_long_a_section_21_eviction_takes.html'),
        name='renters-how_long_a_section_21_eviction_takes'),

    url(r'^renters/how_tenants_can_end_a_fixed_term_tenancy$',
        TemplateView.as_view(template_name='website/renters/how_tenants_can_end_a_fixed_term_tenancy.html'),
        name='renters-how_tenants_can_end_a_fixed_term_tenancy'),

    url(r'^renters/how_to_check_and_agree_an_inventory$',
        TemplateView.as_view(template_name='website/renters/how_to_check_and_agree_an_inventory.html'),
        name='renters-how_to_check_and_agree_an_inventory'),

    url(r'^renters/how_to_complain_about_an_unsafe_home$',
        TemplateView.as_view(template_name='website/renters/how_to_complain_about_an_unsafe_home.html'),
        name='renters-how_to_complain_about_an_unsafe_home'),

    url(r'^renters/how_to_deal_with_pests_and_vermin_in_your_home$',
        TemplateView.as_view(template_name='website/renters/how_to_deal_with_pests_and_vermin_in_your_home.html'),
        name='renters-how_to_deal_with_pests_and_vermin_in_your_home'),

    url(r'^renters/how_to_deal_with_rent_arrears$',
        TemplateView.as_view(template_name='website/renters/how_to_deal_with_rent_arrears.html'),
        name='renters-how_to_deal_with_rent_arrears'),

    url(r'^renters/how_to_find_your_landlord$',
        TemplateView.as_view(template_name='website/renters/how_to_find_your_landlord.html'),
        name='renters-how_to_find_your_landlord'),

    url(r'^renters/how_to_get_an_illegal_eviction_injunction$',
        TemplateView.as_view(template_name='website/renters/how_to_get_an_illegal_eviction_injunction.html'),
        name='renters-how_to_get_an_illegal_eviction_injunction'),

    url(r'^renters/how-to-get-your-deposit-back$',
        TemplateView.as_view(template_name='website/renters/how-to-get-your-deposit-back.html'),
        name='renters-how-to-get-your-deposit-back'),

    url(r'^renters/how_to_rent_from_a_private_landlord_or_letting_agent$',
        TemplateView.as_view(template_name='website/renters/how_to_rent_from_a_private_landlord_or_letting_agent.html'),
        name='renters-how_to_rent_from_a_private_landlord_or_letting_agent'),

    url(r'^renters/how_to_report_repairs_to_a_private_landlord$',
        TemplateView.as_view(template_name='website/renters/how_to_report_repairs_to_a_private_landlord.html'),
        name='renters-how_to_report_repairs_to_a_private_landlord'),

    url(r'^renters/how_to_report_repairs_to_a_social_landlord$',
        TemplateView.as_view(template_name='website/renters/how_to_report_repairs_to_a_social_landlord.html'),
        name='renters-how_to_report_repairs_to_a_social_landlord'),

    url(r'^renters/joint_tenancies$',
        TemplateView.as_view(template_name='website/renters/joint_tenancies.html'),
        name='renters-joint_tenancies'),

    url(r'^renters/landlord_and_tenant_responsibilities_for_repairs$',
        TemplateView.as_view(template_name='website/renters/landlord_and_tenant_responsibilities_for_repairs.html'),
        name='renters-landlord_and_tenant_responsibilities_for_repairs'),

    url(r'^renters/legal_action_if_your_landlord_wont_do_repairs$',
        TemplateView.as_view(template_name='website/renters/legal_action_if_your_landlord_wont_do_repairs.html'),
        name='renters-legal_action_if_your_landlord_wont_do_repairs'),

    url(r'^renters/letting_agent_fees_for_tenants$',
        TemplateView.as_view(template_name='website/renters/letting_agent_fees_for_tenants.html'),
        name='renters-letting_agent_fees_for_tenants'),

    # TODO http://england.shelter.org.uk/get_advice/downloads_and_tools/letting_agent_dispute_tool
    url(r'^renters/letting_agent_redress_schemes$',
        TemplateView.as_view(template_name='website/renters/letting_agent_redress_schemes.html'),
        name='renters-letting_agent_redress_schemes'),

    url(r'^renters/lodgers$',
        TemplateView.as_view(template_name='website/renters/lodgers.html'),
        name='renters-lodgers'),

    url(r'^renters/moving_out_during_repairs$',
        TemplateView.as_view(template_name='website/renters/moving_out_during_repairs.html'),
        name='renters-moving_out_during_repairs'),

    url(r'^renters/occupiers_with_basic_protection$',
        TemplateView.as_view(template_name='website/renters/occupiers_with_basic_protection.html'),
        name='renters-occupiers_with_basic_protection'),

    url(r'^renters/overcrowding$',
        TemplateView.as_view(template_name='website/renters/overcrowding.html'),
        name='renters-overcrowding'),

    url(r'^renters/pests_and_vermin_infestations_in_rented_homes$',
        TemplateView.as_view(template_name='website/renters/pests_and_vermin_infestations_in_rented_homes.html'),
        name='renters-pests_and_vermin_infestations_in_rented_homes'),

    url(r'^renters/poor_conditions_in_council_or_housing_association_homes$',
        TemplateView.as_view(template_name='website/renters/poor_conditions_in_council_or_housing_association_homes.html'),
        name='renters-poor_conditions_in_council_or_housing_association_homes'),

    url(r'^renters/priority_need$',
        TemplateView.as_view(
            template_name='website/renters/priority_need.html'),
        name='renters-priority_need'),

    url(r'^renters/private_renting$',
        TemplateView.as_view(template_name='website/renters/private_renting.html'),
        name='renters-private_renting'),

    url(r'^renters/private_renting_pitfalls$',
        TemplateView.as_view(template_name='website/renters/private_renting_pitfalls.html'),
        name='renters-private_renting_pitfalls'),

    url(r'^renters/problems_during_council_or_housing_association_repairs$',
        TemplateView.as_view(template_name='website/renters/problems_during_council_or_housing_association_repairs.html'),
        name='renters-problems_during_council_or_housing_association_repairs'),

    url(r'^renters/reasons_your_landlord_can_evict_you$',
        TemplateView.as_view(
            template_name='website/renters/reasons_your_landlord_can_evict_you.html'),
        name='renters-reasons_your_landlord_can_evict_you'),

    url(r'^renters/regulated_tenancies$',
        TemplateView.as_view(template_name='website/renters/regulated_tenancies.html'),
        name='renters-regulated_tenancies'),

    # TODO Sort out Shelter Links 'renters-rent_in_advance'
    url(r'^renters/rent_in_advance$',
        TemplateView.as_view(template_name='website/renters/rent_in_advance.html'),
        name='renters-rent_in_advance'),

    url(r'^renters/renewing_your_private_tenancy$',
        TemplateView.as_view(template_name='website/renters/renewing_your_private_tenancy.html'),
        name='renters-renewing_your_private_tenancy'),

    url(r'^renters/rent_deposit_bond_and_guarantee_schemes$',
        TemplateView.as_view(template_name='website/renters/rent_deposit_bond_and_guarantee_schemes.html'),
        name='renters-rent_deposit_bond_and_guarantee_schemes.html'),

    url(r'^renters/rent_increases$',
        TemplateView.as_view(template_name='website/renters/rent_increases.html'),
        name='renters-rent_increases'),

    url(r'^renters/rent_reductions_when_repairs_are_a_problem$',
        TemplateView.as_view(template_name='website/renters/rent_reductions_when_repairs_are_a_problem.html'),
        name='renters-rent_reductions_when_repairs_are_a_problem'),

    url(r'^renters/repairs_and_maintenance_in_council_and_housing_association_homes$',
        TemplateView.as_view(template_name='website/renters/repairs_and_maintenance_in_council_and_housing_association_homes.html'),
        name='renters-repairs_and_maintenance_in_council_and_housing_association_homes'),

    url(r'^renters/repossession_by_a_landlords_lender$',
        TemplateView.as_view(template_name='website/renters/repossession_by_a_landlords_lender.html'),
        name='renters-repossession_by_a_landlords_lender'),

    url(r'^renters/responsibility_for_repairs_in_leasehold_flats_and_houses$',
        TemplateView.as_view(template_name='website/renters/responsibility_for_repairs_in_leasehold_flats_and_houses.html'),
        name='renters-responsibility_for_repairs_in_leasehold_flats_and_houses'),

    url(r'^renters/return_of_a_lodgers_deposit$',
        TemplateView.as_view(template_name='website/renters/return_of_a_lodgers_deposit.html'),
        name='renters-return_of_a_lodgers_deposit'),

    url(r'^renters/revenge_eviction_if_you_ask_for_repairs$',
        TemplateView.as_view(template_name='website/renters/revenge_eviction_if_you_ask_for_repairs.html'),
        name='renters-revenge_eviction_if_you_ask_for_repairs'),

    url(r'^renters/right_to_rent_immigration_checks$',
        TemplateView.as_view(template_name='website/renters/right_to_rent_immigration_checks.html'),
        name='renters-right_to_rent_immigration_checks'),

    url(r'^renters/right_to_repair_for_council_tenants$',
        TemplateView.as_view(template_name='website/renters/right_to_repair_for_council_tenants.html'),
        name='renters-right_to_repair_for_council_tenants'),

    url(r'^renters/safety_standards_for_furniture_and_appliances$',
        TemplateView.as_view(template_name='website/renters/safety_standards_for_furniture_and_appliances.html'),
        name='renters-safety_standards_for_furniture_and_appliances'),

    url(r'^renters/section_21_eviction_process$',
        TemplateView.as_view(template_name='website/renters/section_21_eviction_process.html'),
        name='renters-section_21_eviction_process'),

    url(r'^renters/stopping_eviction_by_bailiffs$',
        TemplateView.as_view(template_name='website/renters/stopping_eviction_by_bailiffs.html'),
        name='renters-stopping_eviction_by_bailiffs'),

    url(r'^renters/subtenants$',
        TemplateView.as_view(template_name='website/renters/subtenants.html'),
        name='renters-subtenants'),

    url(r'^renters/tenancy_agreements_in_shared_homes$',
        TemplateView.as_view(template_name='website/renters/tenancy_agreements_in_shared_homes.html'),
        name='tenancy_agreements_in_shared_homes'),

    url(r'^renters/tenancy_checker$',
        TemplateView.as_view(template_name='website/renters/tenancy_checker.html'),
        name='renters-tenancy_checker'),

    url(r'^renters/tenancy-deposits$', TemplateView.as_view(template_name='website/renters/tenancy-deposits.html'),
        name='renters-tenancy-deposits'),

    url(r'^renters/tenancy_deposit_deductions_your_landlord_can_make$',
        TemplateView.as_view(template_name='website/renters/tenancy_deposit_deductions_your_landlord_can_make.html'),
        name='renters-tenancy_deposit_deductions_your_landlord_can_make'),

    url(r'^renters/tenancy_deposit_protection_rules$',
        TemplateView.as_view(template_name='website/renters/tenancy_deposit_protection_rules.html'),
        name='renters-tenancy_deposit_protection_rules'),

    url(r'^renters/tenants_home_improvements$',
        TemplateView.as_view(template_name='website/renters/tenants_home_improvements.html'),
        name='renters-tenants_home_improvements'),

    url(r'^renters/tips_for_viewing_a_home_to_rent$',
        TemplateView.as_view(template_name='website/renters/tips_for_viewing_a_home_to_rent.html'),
        name='renters-tips_for_viewing_a_home_to_rent'),

    url(r'^renters/types-of-renting-agreement$',
        TemplateView.as_view(template_name='website/renters/types_of_renting_agreement.html'),
        name='renters-types-of-renting-agreement'),

    url(r'^renters/university_accommodation_halls_of_residence$',
        TemplateView.as_view(template_name='website/renters/university_accommodation_halls_of_residence.html'),
        name='renters-university_accommodation_halls_of_residence'),

    url(r'^renters/using_a_letting_agent_to_find_and_rent_a_home$',
        TemplateView.as_view(template_name='website/renters/using_a_letting_agent_to_find_and_rent_a_home.html'),
        name='renters-using_a_letting_agent_to_find_and_rent_a_home'),

    url(r'^renters/what_counts_as_a_decent_home$',
        TemplateView.as_view(template_name='website/renters/what_counts_as_a_decent_home.html'),
        name='renters-what_counts_as_a_decent_home'),

    url(r'^renters/what_happens_at_an_eviction_possession_hearing$',
        TemplateView.as_view(template_name='website/renters/what_happens_at_an_eviction_possession_hearing.html'),
        name='renters-what_happens_at_an_eviction_possession_hearing'),

    url(r'^renters/what_happens_when_bailiffs_evict_tenants$',
        TemplateView.as_view(template_name='website/renters/what_happens_when_bailiffs_evict_tenants.html'),
        name='renters-what_happens_when_bailiffs_evict_tenants'),


    url(r'^renters/what_is_a_tenancy_deposit$',
        TemplateView.as_view(template_name='website/renters/what_is_a_tenancy_deposit.html'),
        name='renters-what_is_a_tenancy_deposit'),

    url(r'^renters/what_is_illegal_eviction$',
        TemplateView.as_view(template_name='website/renters/what_is_illegal_eviction.html'),
        name='renters-what_is_illegal_eviction'),

    url(r'^renters/what_happens_at_a_repossession_hearing$',
        TemplateView.as_view(template_name='website/renters/what_happens_at_a_repossession_hearing.html'),
        name='renters-what_happens_at_a_repossession_hearing'),

    url(r'^renters/what_to_do_if_your_landlord_wont_do_repairs$',
        TemplateView.as_view(template_name='website/renters/what_to_do_if_your_landlord_wont_do_repairs.html'),
        name='renters-what_to_do_if_your_landlord_wont_do_repairs'),

    # renters/disrepair
    url(r'^renters/disrepair/$',
        TemplateView.as_view(template_name='website/renters/disrepair-claims.html'),
        name='renters-disrepair-claims'),


]
