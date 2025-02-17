from openfisca_us.model_api import *


class State(Enum):
    # Source: https://gist.github.com/rogerallen/1583593#gistcomment-3699885
    # 50 states and DC.
    AL = "Alabama"
    AK = "Alaska"
    AZ = "Arizona"
    AR = "Arkansas"
    CA = "California"
    CO = "Colorado"
    CT = "Connecticut"
    DE = "Delaware"
    FL = "Florida"
    GA = "Georgia"
    HI = "Hawaii"
    ID = "Idaho"
    IL = "Illinois"
    IN = "Indiana"
    IA = "Iowa"
    KS = "Kansas"
    KY = "Kentucky"
    LA = "Louisiana"
    ME = "Maine"
    MD = "Maryland"
    MA = "Massachusetts"
    MI = "Michigan"
    MN = "Minnesota"
    MS = "Mississippi"
    MO = "Missouri"
    MT = "Montana"
    NE = "Nebraska"
    NV = "Nevada"
    NH = "New Hampshire"
    NJ = "New Jersey"
    NM = "New Mexico"
    NY = "New York"
    NC = "North Carolina"
    ND = "North Dakota"
    OH = "Ohio"
    OK = "Oklahoma"
    OR = "Oregon"
    PA = "Pennsylvania"
    RI = "Rhode Island"
    SC = "South Carolina"
    SD = "South Dakota"
    TN = "Tennessee"
    TX = "Texas"
    UT = "Utah"
    VT = "Vermont"
    VA = "Virginia"
    WA = "Washington"
    WV = "West Virginia"
    WI = "Wisconsin"
    WY = "Wyoming"
    DC = "District of Columbia"
    # Territories.
    GU = "Guam"
    MP = "Northern Mariana Islands"
    PW = "Palau"
    PR = "Puerto Rico"
    VI = "Virgin Islands"
    AA = "Armed Forces Americas (Except Canada)"
    AE = "Armed Forces Africa/Canada/Europe/Middle East"
    AP = "Armed Forces Pacific"


class state_code(Variable):
    value_type = Enum
    possible_values = State
    default_value = State.CA
    entity = Household
    label = "State"
    definition_period = ETERNITY
