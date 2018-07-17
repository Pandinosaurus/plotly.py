import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='size', parent_name='contour.contours', **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            implied_edits={'^autocontour': False},
            min=0,
            role='style',
            **kwargs
        )