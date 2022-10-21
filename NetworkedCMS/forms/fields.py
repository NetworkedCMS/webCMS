from wtforms import SelectField, StringField, SubmitField, SearchField, SelectMultipleField




class MSelectField(SelectField):
    """Renders and html select field"""
    pass


class MStringField(StringField):
    """Renders and html string field"""
    pass



class MSubmitField(SubmitField):
    """Renders an html submit button"""
    pass



class MSearchField(SearchField):
    """Renders an html search component"""
    pass



class MSelectMultitpleField(SelectMultipleField):
    """Renders a list of items for a select field"""
    pass


