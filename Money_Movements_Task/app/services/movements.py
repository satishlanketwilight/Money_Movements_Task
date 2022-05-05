from app.models.movements import db, MoneyMovementModel
from app.exceptions.movements import MovementObjectNotFound


class MoneyMovementsService:
    """Manager class for Money Movement objects"""

    @staticmethod
    def get_all():
        """Read all objects from database"""
        movement_list = MoneyMovementModel.query.all()
        if len(movement_list) == 0:
            items = [
                    {
                        "amount": "1000",
                        "originator_person": "abc",
                        "receiver_person": "xyz"
                    },
                    {
                        "amount": "500",
                        "originator_person": "asdf",
                        "receiver_person": "xyz"
                    }
                ]
            for i in items:
                new_movement=MoneyMovementModel(**i)
                db.session.add(new_movement)
                db.session.commit()
            movement_list = MoneyMovementModel.query.all()

        return movement_list

    @staticmethod
    def get_by_id(movement_id):
        """Read a single objects from database by id"""
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            return movement
        else:
            raise MovementObjectNotFound

    @staticmethod
    def create(data):
        """Create a new object and save to database"""
        new_movement = MoneyMovementModel(**data)
        db.session.add(new_movement)
        db.session.commit()
        return new_movement

    @staticmethod
    def update(movement_id, data):
        """Update a single object fields and save to database"""
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            movement.note = data
            db.session.commit()
        else:
            raise MovementObjectNotFound

    @staticmethod
    def delete(movement_id):
        """Delete a single object from database"""
        movement = MoneyMovementModel.query.filter_by(movement_id=movement_id).first()
        if movement:
            db.session.delete(movement)
            db.session.commit()
        else:
            raise MovementObjectNotFound
