from sqlalchemy.types import UserDefinedType

class CITEXT(UserDefinedType):
    def get_col_spec(self, **kw):
        return "CITEXT"