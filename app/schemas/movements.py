from marshmallow import fields, Schema


class MoneyMovementSchema(Schema):
    """Money Movement schema class made for serializing/deserializing database model"""
    movement_id = fields.UUID(data_key='movementId', dump_only=True)
    modified_date = fields.Date(data_key='modified_date', dump_only=True)
    amount = fields.String(data_key='amount', required=True)
    currency = fields.String(data_key='currency', required=True)
    originator_person = fields.String(data_key='originator_person', required=True)
    receiver_person = fields.String(data_key='receiver_person', required=True)
    note = fields.String(data_key='note')

    class Meta:
        fields = ('movement_id', 'modified_date', 'amount','currency' ,'originator_person', 'receiver_person', 'note')


class MoneyMovementSingleOutputSchema(Schema):
    """Single Money Movement object output class made for enveloping response"""
    movement = fields.Nested(MoneyMovementSchema)

    class Meta:
        fields = ('movement',)


class MoneyMovementListOutputSchema(Schema):
    """List of Money Movement objects class made for enveloping response"""
    movements = fields.List(fields.Nested(MoneyMovementSchema))

    class Meta:
        fields = ('movements',)
