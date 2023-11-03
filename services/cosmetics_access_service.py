from models.cosmetic import Cosmetic

def create_cosmetic(cosmetic: Cosmetic) :
    """Create a new cosmetic to be registered"""

def create_list_of_cosmetics (cosmetics: list<Cosmetic>) :
    """Create cosmetics from the list defined """

def get_all_cosmetics_registered() :
    """ retrieve all list of cosmetics registered"""

def get_all_properties_registered() :
    """ retrieve all properties of cosmetics registered"""

def get_all_cosmetics_expired() :
    """ retrieve all list of cosmetics that have expired and needs to be finished in priority, 
    list should be sorted by ascending expiry date """

def get_cosmetic_by_name(name: str) :
    """ return description of a cosmetic by its name """

def update_cosmetic(name: str, cosmetic: Cosmetic) :
    """update cosmetic description for example, updating current quantity or adding new properties """

def delete_cosmetic_by_name (name: str) :
    """Delete cosmetic that has been trashed"""

def search_cosmetics_per_properties (properties: list<str>) :
    """Return cosmetics that have at least one property in the list defined"""

def search_cosmetics_per_family (family: str) :
    """Return all cosmetics in the family requested"""

def search_cosmetics_per_family_and_properties (family: str, properties: list<str>) :
    """Return all cosmetics in the family requested and that have at least one property in the list defined"""