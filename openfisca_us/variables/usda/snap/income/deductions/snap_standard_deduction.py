from openfisca_us.model_api import *


class snap_standard_deduction(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    documentation = "Standard deduction for calculating SNAP benefit amount"
    label = "SNAP standard deduction"
    unit = USD
    reference = "https://www.law.cornell.edu/uscode/text/7/2014#e_1"

    def formula(spm_unit, period, parameters):
        standard_deductions = parameters(period).usda.snap.standard_deduction
        state_group = spm_unit.household("state_group_str", period)
        capped_household_size = min_(spm_unit.nb_persons(), 6)
        return standard_deductions[state_group][capped_household_size] * 12
