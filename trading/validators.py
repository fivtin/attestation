from rest_framework.exceptions import ValidationError


class SellerValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        seller = value.get(self.field)
        level = value.get('level')
        if value.id == seller.id:
            raise ValidationError("Нельзя установить поставщиком тот же самый объект.")
        if level == 'factory' and seller and seller.level != 'factory':
            raise ValidationError("Завод может иметь поставщиком только другой завод.")
        if level == 'retail' and (not seller or seller.level not in ['factory', 'retail']):
            raise ValidationError('Розничная сеть может иметь поставщиком завод или другая розничная сеть.')
        if level == 'trader' and (not seller or seller.level not in ['factory', 'retail', 'trader']):
            raise ValueError('ИП может иметь поставщиком завод, розничную сеть или другого ИП.')
