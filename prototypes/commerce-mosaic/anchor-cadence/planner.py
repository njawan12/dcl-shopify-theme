"""One bounded rhythm. No product/fixture identity, image inspection or viewport input."""
def plan(count, rhythm='anchor', feature=True, editorial=True, page_start=0):
    if type(count) is not int or count < 0 or page_start < 0:
        raise ValueError('Counts must be nonnegative')
    active = rhythm == 'anchor' and feature and count >= 12 and page_start == 0
    return {'feature_index': 6 if active else None,
            'editorial_after': 9 if active and editorial and count >= 12 else None}
