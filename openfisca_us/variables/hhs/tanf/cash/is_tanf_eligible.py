from openfisca_us.model_api import *


class is_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    definition_period = YEAR
    label = "Eligibility for TANF"
    documentation = "Whether the family is eligible for Temporary Assistance for Needy Families benefit."

    def formula(spm_unit, period, parameters):
        demographic_eligible = spm_unit.any(
            spm_unit.members("is_person_demographic_tanf_eligible", period)
        )
        economic_eligible = where(
            spm_unit("is_tanf_enrolled", period),
            spm_unit("continuous_tanf_eligibility", period),
            spm_unit("initial_tanf_eligibility", period),
        )
        return demographic_eligible & economic_eligible
