from wtforms import SelectField, StringField, SubmitField, SearchField, SelectMultipleField
from flask_ckeditor import CKEditorField


class RichTextField(CKEditorField):
    """Displays a rich text field web forms"""

    def __init__(self, label=None, validators=None, filters=..., description="", id=None, default=None, widget=None, render_kw=None, name=None, _form=None, _prefix="", _translations=None, _meta=None):
        super().__init__(label, validators, filters, description,
                         id, default, widget, render_kw, name, _form, _prefix, _translations, _meta)


class MSelectField(SelectField):
    """Renders and html select field"""

    def __init__(self, label=None, validators=None, coerce=..., choices=None, validate_choice=True, **kwargs):
        super().__init__(label, validators, coerce, choices,
                         validate_choice, **kwargs)


class MStringField(StringField):
    """Renders and html string field"""

    def __init__(self, label=None, validators=None, filters=..., description="", id=None, default=None, widget=None, render_kw=None, name=None, _form=None, _prefix="", _translations=None, _meta=None):
        super().__init__(label, validators, filters, description, id, default, widget,
                         render_kw, name, _form, _prefix, _translations, _meta)


class MSubmitField(SubmitField):
    """Renders an html submit button"""

    def __init__(self, label=None, validators=None, false_values=None, **kwargs):
        super().__init__(label, validators, false_values, **kwargs)


class MSearchField(SearchField):
    """Renders an html search component"""

    def __init__(self, label=None, validators=None, filters=..., description="", id=None, default=None, widget=None, render_kw=None, name=None, _form=None, _prefix="", _translations=None, _meta=None):
        super().__init__(label, validators, filters, description, id, default, widget,
                         render_kw, name, _form, _prefix, _translations, _meta)


class MSelectMultitpleField(SelectMultipleField):
    """Renders a list of items for a select field"""

    def __init__(self, label=None, validators=None, coerce=..., choices=None, validate_choice=True, **kwargs):
        super().__init__(label, validators, coerce,
                         choices, validate_choice, **kwargs)
