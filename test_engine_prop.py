from hypothesis import given, strategies as st
from app.engine import filter_df

@given(age=st.integers(min_value=0, max_value=100))
def test_age_filter_never_errors(age):
    df = filter_df(f"age > {age}")
    assert "age" in df.columns
