from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit
from django import forms

from main.health.models import Rule


class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ("name",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": ""}
        self.helper.form_id = "idRuleForm"
        self.helper.form_method = "post"  # get or post method
        self.helper.form_class = "form-group"
        self.helper.form_style = "inline"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.layout = Layout(
            Div(
                Field(
                    "name",
                    css_class="form-control-border",
                    id="idRuleName",
                    style="row=2",
                ),
                css_class="col-sm-10",
            ),
            Div(
                FormActions(Submit("submit", "Submit", css_class="")),
                css_class="col-sm-10",
            ),
        )
